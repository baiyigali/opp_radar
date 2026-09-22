#!/usr/bin/env python3
"""把 ROOT 下 <主名>.html + <主名>.png 推到微信公众号草稿箱（只存草稿，不群发）。
用法: python3 scripts/publish.py "<主名>" "<标题>" "<摘要120字内>"

铁律：整个动作只调用一次。无论成功/报错/超时/看似失败，都绝不重试，避免重复建草稿。
（本号为个人未认证主体，freepublish/submit 发布接口无权限，发表由人工在后台完成。）
凭据从 ROOT/config.json 读取（该文件已 gitignore，不进版本库）。
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISSUES = os.path.join(ROOT, "issues")


def main() -> int:
    if len(sys.argv) != 4:
        print('usage: python3 scripts/publish.py "<主名>" "<标题>" "<摘要>"',
              file=sys.stderr)
        return 2
    base, title, digest = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(os.path.join(ROOT, "config.json"), "r", encoding="utf-8") as f:
        cfg = json.load(f)

    from wechat_publish import push_articles, WeChatAPIError

    # 【铁律】这一行 push_articles 从头到尾只执行一次，绝不放在循环/重试里
    try:
        media_id = push_articles(
            appid=cfg["appid"],
            secret=cfg["secret"],
            articles=[{
                "html_path": os.path.join(ISSUES, f"{base}.html"),
                "title": title,
                "cover_path": os.path.join(ISSUES, f"{base}.png"),
                "digest": digest,
            }],
            author=cfg["author"],
            open_comment=False,
            publish_now=False,  # 只存草稿箱，不群发（个人未认证号无 freepublish 发布权限）
        )
        print("DRAFT_MEDIA_ID:", media_id)
    except WeChatAPIError as e:
        # 常见 40164 = 出口 IP 未加白。无论什么错都不重试。
        print("WECHAT_ERROR:", e)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
