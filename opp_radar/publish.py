"""把本期 HTML + 封面推到微信公众号草稿箱（只存草稿，不群发）。"""
from __future__ import annotations

import json
import os

from wechat_publish import WeChatAPIError, push_articles


def push_draft(
    base: str,
    title: str,
    digest: str,
    config_path: str = "config.json",
    issues_dir: str = "issues",
) -> str | None:
    """读 config.json 凭据，建草稿。无论成功/报错都只调用一次，绝不重试。"""
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    try:
        media_id = push_articles(
            appid=cfg["appid"],
            secret=cfg["secret"],
            articles=[{
                "html_path": os.path.join(issues_dir, f"{base}.html"),
                "title": title,
                "cover_path": os.path.join(issues_dir, f"{base}.png"),
                "digest": digest,
            }],
            author=cfg["author"],
            open_comment=False,
            publish_now=False,  # 个人未认证号无 freepublish 发布权限，发表由人工完成
        )
        print("DRAFT_MEDIA_ID:", media_id)
        return media_id
    except WeChatAPIError as e:
        # 常见 40164 = 出口 IP 未加白。无论什么错都不重试。
        print("WECHAT_ERROR:", e)
        return None
