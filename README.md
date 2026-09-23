# opp-radar

面向个人开发者 / 技术创业者的"机会雷达"提示词仓库：从公开技术信号里筛出小团队能做的中小产品机会，写成渠道无关的文章 `.md` + 封面 `.png`。

**本仓库只负责"生成"**——渲染排版和推送到公众号草稿箱由独立项目 [wechat-auto-publish](https://github.com/baiyigali/wechat-auto-publish) 负责。

专栏名：**开发者机会观察**（公众号：程序员白大力）。觉得有用欢迎关注。

## 目录结构

```
opp-radar/
  prompts/
    dev.md          # 开发者机会观察（dev 领域）完整提示词：找信号→反向验证→写稿→封面
    # 以后加 marketing.md、xxx.md 等其他领域提示词
  examples/
    开发者机会观察-第5期.md/.png          # 一篇成稿样例（纯生成产物）
  tests/            # 冒烟测试
  .github/workflows/publish.yml         # CI：构建 + TestPyPI/PyPI（OIDC 免密）
  pyproject.toml    # 打包配置
```

## 跑一期（生成）

按 `prompts/dev.md` 的流程：找信号 → 反向验证 → 写 5-8 个全新方向 → 出一张封面。
产出 `<主名>.md` 和 `<主名>.png`，落在本地文章目录（不进本仓库）。

渲染和推草稿请交给 wechat-auto-publish：
```bash
pip install wechat-auto-publish
wechat-auto-publish draft "<主名>.md" "<主名>.png" "<标题>" "<摘要>"
```

## 样例

`examples/开发者机会观察-第5期.md` + `.png` 是一期纯生成产物的样子（科技风经典蓝的最终排版由 wechat-auto-publish 渲染）。

## 相关项目

- [wechat-auto-publish](https://github.com/baiyigali/wechat-auto-publish)：最外层发布流水线，一条命令把排版、推草稿串起来
- [wechat-formatter](https://github.com/baiyigali/wechat-formatter)：Markdown → 公众号内联样式 HTML
- [wechat-publish](https://github.com/baiyigali/wechat-publish)：公众号草稿箱接口，图片自动转存微信 CDN

## 技术交流

扫码添加微信，交流使用问题、定制与合作：

<p align="center">
  <img src="docs/images/wechat-contact-qr.jpg" alt="微信二维码" width="240" />
</p>

## 项目赞助

本项目由以下微信公众号提供赞助，感谢支持：

**「程序员白大力」** —— 法律科技 / 自动化内容创作

<p align="center">
  <img src="docs/images/wechat-official-account-qr.png" alt="程序员白大力公众号二维码" width="240" />
</p>

**「法啊」** —— 法律科普 / 普法内容

<p align="center">
  <img src="docs/images/fa-official-account-qr.png" alt="法啊公众号二维码" width="240" />
</p>

**「极速法考」** —— 法考备考 / 法律职业资格考试

<p align="center">
  <img src="docs/images/jisu-fakao-official-account-qr.png" alt="极速法考公众号二维码" width="240" />
</p>

## License

MIT
