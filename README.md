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
    开发者机会观察-第5期.md/.png/.html   # 一篇成稿样例
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

看 `examples/开发者机会观察-第5期.html` 可直接在浏览器打开预览最终排版效果（科技风、经典蓝 #2563eb）。

## 设计原则

- **提示词只讲"做什么"**，调度/定时是外层平台壳，不写进提示词；
- **生成与分发分离**：opp-radar 出文本，wechat-auto-publish 负责渲染和发布；
- 文章产出与代码仓库隔离，不随仓库分发。
