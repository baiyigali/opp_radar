# opp-radar

面向个人开发者 / 技术创业者的"机会雷达"：从公开技术信号里筛出小团队能做的中小产品机会，自动写成公众号专栏，渲染排版后推到草稿箱（发表由人工在后台完成）。

专栏名：**开发者机会观察**（公众号：程序员白大力）。觉得有用欢迎关注。

## 目录结构

```
opp-radar/
  opp_radar/        # 安装后的 Python 包（render / publish / cli）
    render.py · publish.py · cli.py · __init__.py · py.typed
  prompts/
    dev.md          # 开发者机会观察（dev 领域）完整提示词
    # 以后加 marketing.md、xxx.md 等其他领域，复用 opp_radar/
  scripts/
    render.py       # 薄壳：转发到 opp_radar render（兼容旧调用，无需安装）
    publish.py      # 薄壳：转发到 opp_radar publish
  examples/
    开发者机会观察-第5期.md/.png/.html   # 一篇成稿样例
  tests/            # 冒烟测试
  .github/workflows/publish.yml   # CI：构建 + TestPyPI/PyPI（OIDC 免密）
  pyproject.toml    # 打包配置，提供 `opp-radar` 命令
  issues/           # 各期产出，gitignore，只在本地（用于去重）
  config.json       # 微信凭据，gitignore，不进版本库
```

## 跑一期

安装（开发模式）：
```bash
pip install -e .
```
然后：
1. 按 `prompts/dev.md` 的流程：找信号 → 反向验证 → 写 `.md` → 出 `.png`（都落在 `issues/`）；
2. 渲染：`opp-radar render "开发者机会观察-第N期"`；
3. 推草稿：`opp-radar publish "开发者机会观察-第N期" "<标题>" "<摘要>"`，再去公众号后台草稿箱点"发表"。

> 不想安装时也可直接用薄壳脚本，效果一样：
> `python3 scripts/render.py "..."` / `python3 scripts/publish.py "..."`。

## 样例

看 `examples/开发者机会观察-第5期.html` 可直接在浏览器打开预览最终排版效果（科技风、经典蓝 #2563eb）。

## 依赖

```bash
pip install -e .
# 或手动：pip install wechat-formatter wechat-publish
```

## 本地凭据

根目录 `config.json`：
```json
{ "appid": "...", "secret": "...", "author": "..." }
```
该文件已在 `.gitignore` 中，**不要提交到公开仓库**。

## 铁律

推草稿脚本只执行一次，无论返回成功/报错/超时都绝不重试，避免重复建草稿。
