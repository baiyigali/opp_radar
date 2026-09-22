"""把 <主名>.md 用 wechat_formatter 渲染成公众号内联样式 HTML。"""
from __future__ import annotations

import os

from wechat_formatter import FormatTweaks, get_template, render_article


def render(base: str, issues_dir: str = "issues") -> str:
    """读取 issues_dir/<base>.md，写出 issues_dir/<base>.html，返回 html 路径。"""
    md_path = os.path.join(issues_dir, f"{base}.md")
    html_path = os.path.join(issues_dir, f"{base}.html")

    with open(md_path, "r", encoding="utf-8") as f:
        md = f.read()

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
    return html_path
