"""opp-radar 命令行入口。

安装后提供两个子命令：
  opp-radar render  "<主名>"                  # issues/<主名>.md -> .html
  opp-radar publish "<主名>" "<标题>" "<摘要>"  # 推到公众号草稿箱
两者都在当前工作目录下读写 issues/ 与 config.json。
"""
from __future__ import annotations

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="opp-radar",
        description="开发者机会观察：渲染公众号 HTML 并推草稿箱。",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    pr = sub.add_parser("render", help="把 issues/<主名>.md 渲染成公众号 HTML")
    pr.add_argument("base", help="文件名主名，如 开发者机会观察-第6期")

    pp = sub.add_parser("publish", help="把 issues/<主名>.html+.png 推到公众号草稿箱")
    pp.add_argument("base", help="文件名主名")
    pp.add_argument("title", help="文章标题")
    pp.add_argument("digest", help="摘要（120 字内）")

    args = parser.parse_args()

    if args.cmd == "render":
        from .render import render
        render(args.base)
        return 0
    if args.cmd == "publish":
        from .publish import push_draft
        push_draft(args.base, args.title, args.digest)
        return 0
    parser.error("未知子命令")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
