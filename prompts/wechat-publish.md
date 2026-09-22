# 分发流水线 · 微信公众号（wechat-publish）

> 用法：在 `prompts/dev.md`（或其它领域雷达）已经在 `issues/` 下产出 `<主名>.md` 和 `<主名>.png` 之后，对 agent 说一句"按 `prompts/wechat-publish.md` 把 `<主名>` 发到公众号草稿箱"。
>
> 本提示词**不生成内容**，只做分发：把已有的 `.md` 渲染成公众号 HTML，再推到公众号草稿箱。发表由人工在后台完成（本号个人未认证，无 freepublish 发布权限）。

---

## 【提示词正文】

# 角色
你是一条微信公众号分发流水线的执行者。给定一个主名 `<base>`，仓库 `issues/` 下已经存在 `<base>.md`（文章）和 `<base>.png`（封面），你负责渲染和推草稿，不做任何内容改写。

# 工作目录
ROOT 指本仓库 clone 下来的根目录（操作前先 `pwd` 确认就在仓库根目录）。所有文件都在 `ROOT/issues/` 下。

# 步骤

## 第一步：取出标题和摘要
读 `issues/<base>.md`：
- **标题**：取正文第一行 H1（`# ` 开头），去掉 `# ` 后作为文章标题；
- **摘要**：取开头第一段里的趋势性两三句，压到 120 字以内，作为 digest。

## 第二步：MD → 公众号 HTML
在 ROOT 下运行：
```bash
python3 scripts/render.py "<base>"
```
（若已 `pip install -e .`，等价于 `opp-radar render "<base>"`。）
脚本用 wechat_formatter 的"科技风 / 经典"（主题色 #2563eb）把 `<base>.md` 渲染成内联样式的 `issues/<base>.html`。
- 生成后校验：HTML 里 `<img>` 数量应为 1，各小节正文都在。

## 第三步：推到公众号草稿箱（只存草稿，不群发）
在 ROOT 下运行，**只执行这一次，绝不重试**：
```bash
python3 scripts/publish.py "<base>" "<标题>" "<摘要>"
```
（等价于 `opp-radar publish "<base>" "<标题>" "<摘要>"`。）
- 凭据从 ROOT 下 `config.json` 读取（appid / secret / author），不写进提示词；
- 脚本会自动把正文外链图转存微信 CDN、封面传永久素材，再调 `draft/add` 建草稿；
- **【铁律】这条命令从头到尾只执行一次。** 无论输出成功、报错、超时还是看似失败，都**绝不重跑第二次**，避免重复建草稿；
- 常见错误 `40164` = 出口 IP 未加白，如实报告即可，不要重试。

# 交付
把脚本输出（草稿 media_id / 错误信息）原样报告；不生成新文件，不改写 `.md`。提醒用户去 mp.weixin.qq.com → 草稿箱预览、点"发表"。

---

# 本地凭据（不进 git）
ROOT 下 `config.json`（已 gitignore）：
```json
{
  "appid": "在公众号后台获取",
  "secret": "在公众号后台获取",
  "author": "程序员白大力"
}
```
