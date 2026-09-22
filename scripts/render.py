#!/usr/bin/env python3
"""把 ROOT 下 <主名>.md 用 wechat_formatter 渲染成公众号内联样式 HTML。
用法: python3 scripts/render.py "<主名>"
ROOT = 本仓库根目录（scripts/ 的上一级）。
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISSUES = os.path.join(ROOT, "issues")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 scripts/render.py <主名>", file=sys.stderr)
        return 2
    base = sys.argv[1]
    md_path = os.path.join(ISSUES, f"{base}.md")
    html_path = os.path.join(ISSUES, f"{base}.html")

    with open(md_path, "r", encoding="utf-8") as f:
        md = f.read()

    from wechat_formatter import get_template, render_article, FormatTweaks

    template = get_template("科技风", "经典")  # 科技风 + 经典蓝 #2563eb
    tweaks = FormatTweaks(
        fontSize=15,
        lineHeight=1.8,
        paragraphSpacing=18,
        imageRadius=6,
    )
    body = render_article(md, template, tweaks)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{base}</title>
<style>
  body {{ margin:0; background:#f2f3f5; padding:24px 0; }}
  .wechat-article {{ max-width:677px; margin:0 auto; background:#fff;
                     padding:24px 16px; box-sizing:border-box; }}
</style>
</head>
<body>
<div class="wechat-article">
{body}
</div>
</body>
</html>"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML_OK:", html_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
