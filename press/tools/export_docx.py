#!/usr/bin/env python3
"""
export_docx.py — 책 한 권(또는 전체)을 그림 포함 DOCX로 변환.

사용법:
  python3 press/tools/export_docx.py data-literacy
  python3 press/tools/export_docx.py ai-for-marketers
  python3 press/tools/export_docx.py all          # 두 책 모두

출력: books/<slug>/final/<slug>.docx
필요 도구: pandoc, mmdc (mermaid-cli), cairosvg (pip)
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PUPPETEER_CFG = REPO / "press/tools/puppeteer-no-sandbox.json"

# ── puppeteer config (root 환경용 --no-sandbox) ─────────────────────────────
def ensure_puppeteer_cfg():
    PUPPETEER_CFG.parent.mkdir(parents=True, exist_ok=True)
    if not PUPPETEER_CFG.exists():
        PUPPETEER_CFG.write_text('{"args": ["--no-sandbox"]}')

# ── mmd → PNG ────────────────────────────────────────────────────────────────
def render_mmd(mmd_path: Path, out_png: Path) -> bool:
    mmdc = shutil.which("mmdc") or "/opt/node22/bin/mmdc"
    result = subprocess.run(
        [mmdc, "-i", str(mmd_path), "-o", str(out_png),
         "--puppeteerConfigFile", str(PUPPETEER_CFG),
         "--backgroundColor", "white"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  ⚠️  mmd 렌더 실패: {mmd_path.name}\n     {result.stderr[:200]}")
        return False
    return True

# ── SVG → PNG ────────────────────────────────────────────────────────────────
def convert_svg(svg_path: Path, out_png: Path) -> bool:
    try:
        import cairosvg
        cairosvg.svg2png(url=str(svg_path), write_to=str(out_png), scale=2.0)
        return True
    except Exception as e:
        print(f"  ⚠️  SVG 변환 실패: {svg_path.name} — {e}")
        return False

# ── art 디렉터리 전체 렌더링 ─────────────────────────────────────────────────
def render_all_art(art_dir: Path, img_dir: Path) -> dict:
    """art/ 안의 모든 .mmd/.svg를 PNG로 변환. {원본stem: PNG경로} 반환."""
    img_dir.mkdir(parents=True, exist_ok=True)
    rendered = {}

    for f in sorted(art_dir.glob("*.mmd")):
        out = img_dir / f.with_suffix(".png").name
        print(f"  → mmd: {f.name}")
        if render_mmd(f, out):
            rendered[f.stem] = out

    for f in sorted(art_dir.glob("*.svg")):
        out = img_dir / f.with_suffix(".png").name
        print(f"  → svg: {f.name}")
        if convert_svg(f, out):
            rendered[f.stem] = out

    return rendered

# ── 원고 전처리: 그림 참조를 실제 이미지 마크다운으로 교체 ───────────────────
def process_manuscript(src: Path, img_dir: Path, rendered: dict) -> str:
    text = src.read_text(encoding="utf-8")

    # 패턴 1: > [그림 N-M | `art/chNN-figMM.mmd`] 캡션
    # 패턴 2: > [그림 N-M | `art/chNN-figMM.svg`] 캡션
    def replace_blockquote_fig(m):
        fig_label = m.group(1).strip()   # 예: 그림 1-1
        art_path  = m.group(2).strip()   # 예: art/ch01-fig01.mmd
        caption   = m.group(3).strip()
        stem = Path(art_path).stem       # 예: ch01-fig01
        png  = rendered.get(stem)
        if png:
            rel = os.path.relpath(png, src.parent)
            return f"![{fig_label}. {caption}]({rel})\n\n*{fig_label}. {caption}*"
        return f"> **[{fig_label}]** {caption}\n> *(도판 렌더링 실패: {art_path})*"

    text = re.sub(
        r'^\s*>\s*\[([그림a-zA-Z0-9\-\s]+?)\s*\|\s*`([^`]+)`\]\s*(.+)$',
        replace_blockquote_fig,
        text,
        flags=re.MULTILINE
    )

    # 패턴 3: > [그림 N-M] 캡션 (art 경로 없음)
    def replace_blockquote_no_art(m):
        fig_label = m.group(1).strip()
        caption   = m.group(2).strip()
        num_m = re.match(r'그림\s*(\d+)[–-](\d+)', fig_label)
        if num_m:
            ch  = int(num_m.group(1))
            fig = int(num_m.group(2))
            stem = f"ch{ch:02d}-fig{fig:02d}"
            png  = rendered.get(stem)
            if png:
                rel = os.path.relpath(png, src.parent)
                return f"![{fig_label}. {caption}]({rel})\n\n*{fig_label}. {caption}*"
        return f"> **[{fig_label}]** {caption}"

    text = re.sub(
        r'^\s*>\s*\[([그림a-zA-Z0-9\-\s]+?)\]\s*(.+)$',
        replace_blockquote_no_art,
        text,
        flags=re.MULTILINE
    )

    # 패턴 4: ![alt](../art/chNN-figMM.svg) — 직접 삽입형
    def replace_direct_svg(m):
        alt      = m.group(1)
        art_path = m.group(2)
        stem = Path(art_path).stem
        png  = rendered.get(stem)
        if png:
            rel = os.path.relpath(png, src.parent)
            return f"![{alt}]({rel})"
        return m.group(0)

    text = re.sub(
        r'!\[([^\]]*)\]\((\.\./art/[^\)]+\.svg)\)',
        replace_direct_svg,
        text
    )

    return text

# ── 메인 변환 ────────────────────────────────────────────────────────────────
def export_book(slug: str):
    book_dir = REPO / "books" / slug
    if not book_dir.exists():
        print(f"❌ 책 디렉터리 없음: {book_dir}")
        return

    art_dir   = book_dir / "art"
    final_dir = book_dir / "final"
    manuscript = final_dir / "manuscript.md"

    if not manuscript.exists():
        print(f"❌ 원고 없음: {manuscript}")
        return

    print(f"\n{'='*60}")
    print(f"📖 {slug}")
    print(f"{'='*60}")

    img_dir = final_dir / "_images"
    print("1) 도판 렌더링...")
    rendered = render_all_art(art_dir, img_dir) if art_dir.exists() else {}
    print(f"   완료: {len(rendered)}점")

    print("2) 원고 전처리...")
    processed = process_manuscript(manuscript, img_dir, rendered)
    tmp_md = final_dir / "_manuscript_tmp.md"
    tmp_md.write_text(processed, encoding="utf-8")

    out_docx = final_dir / f"{slug}.docx"
    print("3) pandoc 변환...")
    result = subprocess.run(
        ["pandoc", str(tmp_md), "-o", str(out_docx),
         "--from", "markdown",
         "--to", "docx",
         "--toc", "--toc-depth=2",
         "-V", "lang=ko"],
        capture_output=True, text=True,
        cwd=str(final_dir)
    )
    if result.returncode != 0:
        print(f"❌ pandoc 실패:\n{result.stderr}")
    else:
        size_kb = out_docx.stat().st_size // 1024
        print(f"✅ 완료: {out_docx.relative_to(REPO)}  ({size_kb} KB)")

    tmp_md.unlink(missing_ok=True)

# ── 진입점 ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    slugs_arg = sys.argv[1] if len(sys.argv) > 1 else "all"

    ensure_puppeteer_cfg()

    if slugs_arg == "all":
        books_dir = REPO / "books"
        slugs = [d.name for d in sorted(books_dir.iterdir()) if d.is_dir()]
    else:
        slugs = [slugs_arg]

    for slug in slugs:
        export_book(slug)

    print("\n완료. books/<slug>/final/<slug>.docx 를 확인하세요.")
