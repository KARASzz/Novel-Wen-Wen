# Chinese Novel Writing Skills

一套面向中文小说与番茄式网文的 Codex Skills 流水线，覆盖多阶段路由、章节正文、人物对白和末轮去 AI 腔。

这套工具的目标不是“绕过 AI 检测”，而是减少模板化、解释性和过度整齐的文字，同时保护情节事实、人物声音与作者原有习惯。

## 包含的 skills

| Skill | 用途 | 触发边界 |
|---|---|---|
| `novel-writer-cn` | 协调多阶段中文小说项目和文件交接 | 仅用于跨阶段、跨文件任务 |
| `fanqie-webnovel-prose` | 创作、续写、改写番茄式中文网文正文 | 负责完整章节与章级质检 |
| `dialogue` | 创作、重写、诊断人物对白 | 只处理对白及必要动作节拍 |
| `fiction-humanizer-zh` | 对稳定成稿做克制的末轮去 AI 腔 | 默认不隐式触发，需明确点名 |

四个 skills 的职责已经分开：正文 skill 不替代全书结构，对白 skill 不抢完整章节，去 AI skill 不改写情节，路由 skill 不重复执行专项工作。

## 推荐流水线

1. 用 `novel-writer-cn` 识别当前阶段并维护事实交接。
2. 用 `fanqie-webnovel-prose` 生成或修订完整章节。
3. 对关键谈判、争吵或感情场景，调用 `dialogue` 做声线与潜台词专项。
4. 结构、情节和人物关系稳定后，明确调用 `fiction-humanizer-zh` 做末轮清理。

单项任务直接调用对应 skill，不需要每次启动整条流水线。

## 安装

使用 Agent Skills CLI：

```bash
npx skills add https://github.com/aa15107688191-collab/chinese-novel-writing-skills
```

按提示选择需要安装的 skills。也可以克隆仓库后，将 `skills/` 下对应目录复制到 Codex 的个人 skills 目录。

安装后可这样使用：

```text
使用 $novel-writer-cn 接手这个长篇项目，从现有大纲继续写三章。
使用 $fanqie-webnovel-prose 把这份章纲扩成可连载正文。
使用 $dialogue 重写这场争吵，让两个人声线不同并加强潜台词。
使用 $fiction-humanizer-zh 对这章做末轮去 AI，但不要改变事实和人物动机。
```

## 可选协作 skills

总路由可以和其他专项 skills 协作，例如 `story-init`、`plot-structure`、`character-management`、`worldbuilding`、`scene-sequencing`、`chapter-writing`、`prose-style`、`cliche-transcendence` 与 `novel-revision`。这些不是本仓库的必装内容；缺少时仍可使用本仓库的四个核心 skills。

## 质量检查

正文、对白和去 AI skill 各自附带零第三方依赖的 Python 检查脚本。脚本只报告候选风险，不给出“AI 百分比”，也不会替代人工语境判断。

## 开源边界

仓库只包含可复用的写作流程、模板与检查脚本，不包含小说正文、私人项目资料、排行榜抓取结果、缓存或生成文件。

项目采用 MIT License。方法来源和上游署名见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
