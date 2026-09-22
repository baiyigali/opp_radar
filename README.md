# opp-radar

面向个人开发者 / 技术创业者的"机会雷达"：从公开技术信号里筛出小团队能做的中小产品机会，自动写成公众号专栏，渲染排版后推到草稿箱（发表由人工在后台完成）。

专栏名：**开发者机会观察**（公众号：程序员白大力）。觉得有用欢迎关注。

## 目录结构

```
opp-radar/
  prompts/
    dev.md          # 开发者机会观察（dev 领域）完整提示词
    # 以后加 marketing.md、xxx.md 等其他领域，复用 scripts/
  scripts/
    render.py       # issues/ 下 MD -> 公众号内联样式 HTML（科技风/经典蓝）
    publish.py      # 把 issues/ 下本期推到公众号草稿箱（只存草稿，不群发）
  examples/
    开发者机会观察-第5期.md/.png/.html   # 一篇成稿样例
  issues/           # 各期产出，gitignore，只在本地（用于去重）
  config.json       # 微信凭据，gitignore，不进版本库
```

## 跑一期

1. 按 `prompts/dev.md` 的流程：找信号 → 反向验证 → 写 `.md` → 出 `.png`（都落在 `issues/`）；
2. 渲染：`python3 scripts/render.py "开发者机会观察-第N期"`；
3. 推草稿：`python3 scripts/publish.py "开发者机会观察-第N期" "<标题>" "<摘要>"`，然后去公众号后台草稿箱点"发表"。

## 样例

看 `examples/开发者机会观察-第5期.html` 可直接在浏览器打开预览最终排版效果（科技风、经典蓝 #2563eb）。

## 依赖

```bash
pip install wechat-formatter wechat_publish
```

## 本地凭据

根目录 `config.json`：
```json
{ "appid": "...", "secret": "...", "author": "..." }
```
该文件已在 `.gitignore` 中，**不要提交到公开仓库**。

## 铁律

推草稿脚本只执行一次，无论返回成功/报错/超时都绝不重试，避免重复建草稿。
