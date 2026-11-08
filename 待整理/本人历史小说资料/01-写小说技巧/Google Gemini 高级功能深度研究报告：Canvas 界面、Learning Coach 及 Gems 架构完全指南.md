# **Google Gemini 高级功能深度研究报告：Canvas 界面、Learning Coach 及 Gems 架构完全指南**

## **1.**  **Google Gemini 生态系统的架构演变与生成式 UI 范式**

人工智能（AI）交互界面的演进正经历从单纯的“对话流”（Chat Stream）向“生成式工作区”（Generative Workspace）的根本性转变。Google Gemini 的最新功能迭代——特别是 Canvas 界面、Gems 个性化智能体以及专为教育设计的 Learning Coach/Guided Learning 架构——标志着这一转变的里程碑。本报告将从技术实现、用户交互逻辑及最佳实践三个维度，对这三大核心功能进行详尽的解构与分析。

在传统的 LLM（大型语言模型）交互中，内容生成与对话指令混合在同一线性时间轴上，导致了“上下文污染”和“迭代困难”等问题。Gemini 通过引入 Canvas，实际上部署了一种“生成式 UI”（Generative UI），将内容的 *创造（Creation）*  与 *指令（Instruction）*  在空间上解耦 1。与此同时，Gems 通过系统级提示词（System Prompting）的封装，解决了大模型“千人一面”的通用性问题，实现了持久化的角色定制 3。而在教育垂直领域，Gemini 引入了基于 LearnLM 模型的 Guided Learning 模式，试图通过苏格拉底式的引导替代传统的直接问答，重塑 AI 辅助学习的教学法 5。

本报告旨在为专业用户、开发者及教育工作者提供一份详尽的操作指南与技术白皮书，全面覆盖从基础操作到高阶指令工程的所有细节。

---

## **2.**  **Gemini Canvas：生成式协作工作区深度解析**

### **2.1 Canvas 的核心设计理念与触发机制**

Gemini Canvas（画布）是 Google 对抗 OpenAI "Canvas" 模式及 Anthropic "Artifacts" 功能的战略性回应。它不仅仅是一个文本编辑器，而是一个具备上下文感知能力的协作层。

#### **2.1.1 界面架构：双流交互**

在 Canvas 模式下，界面被垂直分割为两个独立区域：

- **左侧/底部对话区（Chat Panel）：**  用户在此输入指令、反馈意见或进行多轮对话。
- **右侧/主画布区（Canvas Panel）：**  AI 生成的结构化内容（文章、代码、图表）在此呈现。这是一个持久化的编辑状态，不会随着对话流的滚动而消失 6。

这种设计的核心优势在于**上下文隔离**。用户可以在左侧不断与 AI 探讨修改意见（例如“这一段语气再委婉一点”），而右侧的文档会实时更新，避免了传统聊天界面中每次修改都需要重新生成整篇长文的冗余与 token 浪费。

#### **2.1.2 启动与触发逻辑**

Canvas 的启动机制设计得既显性又隐性，以适应不同用户的意图：

1. **手动触发（Explicit Trigger）：**  用户可以在输入框下方的菜单中直接选择“Canvas”图标，强制模型进入工作区模式。这在用户明确知道自己需要创建一个复杂文档或代码项目时最为有效 6。
2. **意图识别自动触发（Implicit Trigger）：**  Gemini 的意图识别模型会分析用户的提示词。如果 prompt 包含类似“写一篇关于...的博客文章”或“创建一个 Python 脚本来...”等暗示长内容生成的指令，系统会自动开启 Canvas 界面 6。

### **2.2 写作模式（Writing Mode）：精细化编辑与文档工程**

在处理长文本（如报告、论文、营销文案）时，Canvas 提供了一套超越传统文字处理软件的 AI 原生工具链。

#### **2.2.1 颗粒度编辑（Granular Editing）与“高亮”菜单**

Canvas 最具颠覆性的功能在于其对特定文本片段的微操能力。传统的 AI 修改通常是全局性的（Global Edit），而 Canvas 允许**局部重绘（In-painting）** 。

当用户在 Canvas 面板中高亮选中一段文本时，会弹出一个悬浮的 AI 编辑菜单，提供以下核心功能 9：

- **Regenerate（重新生成）：**  仅针对选中的段落进行重写，保持上下文连贯性，但改变措辞或句式。
- **Shorten（精简）：**  压缩选中内容的冗余信息，提高信息密度。这对于将长篇大论转化为摘要至关重要。
- **Lengthen（扩写）：**  对选中观点进行展开，补充细节或论据。这是对抗 AI 生成内容“空洞”问题的有力工具。
- **Remove（移除）：**  删除选中内容，并自动平滑前后文的衔接。
- **Tone Adjustment（语气调整）：**  虽然通常是全局选项，但部分版本允许针对特定段落调整语气（如将某一段改为“更专业”或“更幽默”）1。

#### **2.2.2 格式化与结构化输出**

Canvas 支持标准的 Markdown 渲染，并内置了富文本编辑工具栏：

- **标题层级（H1-H3）：**  用于构建文档骨架。AI 能够理解这种层级结构，用户可以说“在第二章和第三章之间增加一个关于 X 的小节”，AI 会精准定位插入点。
- **列表与强调：**  支持无序/有序列表、加粗、斜体等 9。

### **2.3 编程模式（Coding Mode）：交互式开发与实时预览**

对于开发者而言，Canvas 是一个轻量级的 IDE（集成开发环境），支持从代码生成到调试的完整闭环。

#### **2.3.1 多语言支持与文件管理**

Canvas 支持广泛的编程语言，包括但不限于 Python, JavaScript, Java, C++, Go, SQL 等 11。

- **多文件理解：**  用户可以一次性上传多个代码文件，或者直接连接 GitHub 仓库（支持高达 5,000 个文件，最大 100MB），使 Gemini 能够理解整个项目的架构依赖，而不仅仅是单一大文件的片段 12。
- **代码隔离：**  生成的代码在 Canvas 中有独立的视窗，支持语法高亮和复制功能。

#### **2.3.2 实时预览（Live Preview）与控制台**

针对前端开发（HTML/CSS/JS, React），Canvas 提供了**实时渲染**功能。

- **即时反馈：**  当 AI 生成一段网页代码时，右侧窗口会直接渲染出网页的视觉效果。用户可以一边看效果，一边在对话框中指令“把按钮改成蓝色”或“增加一个搜索框”，Canvas 会实时更新代码并刷新预览 13。
- **内置控制台（Console）：**  为了解决代码运行错误，Canvas 内置了调试控制台。用户点击“Show console”即可查看错误日志（Logs）。这意味着开发者无需离开浏览器，即可完成“编写-运行-报错-修复”的循环。用户甚至可以直接询问 Gemini：“控制台报错了，请修复”，AI 会自动读取 Logs 并提供修正代码 6。

### **2.4 Canvas 的快捷键体系与操作效率**

为了提升专业用户的工作流效率，Canvas 集成了一套快捷键系统。虽然不同操作系统（Windows/Mac）和环境（Web/IDE 插件）略有差异，但核心逻辑一致。

|功能动作|Windows 快捷键|Mac 快捷键|上下文环境|
| :---------| :-----------------------| :------------------------| :-----------------|
|**打开/关闭聊天窗口**|Alt \+ G|Option \+ G|Web/IDE 15|
|**撤销 (Undo)**|Ctrl \+ Z|Cmd \+ Z|Canvas 编辑区 16|
|**重做 (Redo)**|Ctrl \+ Y|Shift \+ Cmd \+ Z|Canvas 编辑区 16|
|**添加选中代码到上下文**|Ctrl \+ Alt \+ X|Cmd \+ Alt \+ X|IDE 插件环境 15|
|**最大化 Canvas**|Ctrl \+ Enter|Cmd \+ Enter|Web 界面 16|
|**取消选择**|Esc|Esc|Canvas 编辑区 16|

*注：快捷键的具体映射可能会随浏览器版本更新而微调，建议参考最新的官方文档或界面提示。*

---

## **3.**  **Gems 功能详解：构建持久化 AI 专家**

### **3.1 Gems 的概念与技术本质**

**Gems** 是 Gemini 生态系统中的“自定义指令集封装器”，类似于 OpenAI 的 GPTs。其核心技术本质是**System Prompt（系统提示词）的持久化**。在普通的 Chat 模式中，一旦开启新对话，之前的角色设定（Persona）就会丢失。而 Gems 允许用户将特定的角色设定、任务约束、知识库（Knowledge Base）和输出风格固化为一个独立的“应用” 1。

### **3.2 Gems 创建全流程指南**

创建一个高效的 Gem 不仅仅是简单的命名，它涉及到精细的提示词工程（Prompt Engineering）。

#### **3.2.1 基础设置与入口**

用户可以通过 Gemini 网页左侧边栏的“Gem Manager”（Gems 管理器）或“Explore Gems”（探索 Gems）进入创建界面 3。

1. 点击  **"New Gem"** （新建 Gem）。
2. **命名（Name）：**  建议使用动宾结构或具象名词，如“Python 代码审查员”而非简单的“助手”。

#### **3.2.2 指令工程（Instruction Engineering）：PTCF 框架**

为了编写高质量的 Gem 指令，专家建议采用 **PTCF 框架** 18：

1. **Persona (角色)：**  定义 AI 是谁。
   - *示例：*  “你是一位拥有 15 年经验的资深产品经理，擅长敏捷开发和用户体验设计。”
2. **Task (任务)：**  定义 AI 需要做什么。
   - *示例：*  “你的任务是帮助我撰写 PRD（产品需求文档），并对我的功能构想提出批判性的反驳意见。”
3. **Context (背景)：**  提供必要的背景信息。
   - *示例：*  “我们的产品是一个面向大学生的社交 App，风格轻松活泼。避免使用过于僵硬的企业术语。”
4. **Format (格式)：**  定义输出的结构。
   - *示例：*  “所有建议必须以表格形式列出，包含‘优点’、‘缺点’和‘改进建议’三列。最后必须附带一个总结段落。”

#### **3.2.3 AI 辅助重写（The "Magic Pencil"）**

Google 在 Gem 创建界面内置了一个极其强大的功能：**指令重写（Use Gemini to re-write instructions）** 。用户只需输入简单的意图（例如“帮我做一个健身教练”），点击“铅笔”图标，Gemini 就会自动将其扩展为一段包含详细角色设定、语气指导和行为规范的复杂 Prompt 3。

- *策略建议：*  先用简单的语言描述核心需求，使用 AI 重写功能生成草稿，然后人工微调（Human-in-the-loop），这是最高效的创建路径。

#### **3.2.4 知识库集成（RAG 增强）**

Gems 支持 **RAG（检索增强生成）**  技术。用户可以在创建界面下方的  **"Knowledge"** （知识）区域上传文件 3。

- **支持源：**  本地文件（PDF, CSV 等）及 Google Drive 文件（Docs, Sheets）。
- **动态链接特性：**  如果连接的是 Google Drive 文件，Gem 会读取该文件的**最新版本**。这意味着如果通过 Gem 管理项目进度，只需更新源 Google Sheet，Gem 的回答就会自动同步最新数据，无需重新配置 3。

### **3.3 预置 Gems 与二次开发**

Gemini 预装了一系列官方 Gems，包括 **Brainstormer**（头脑风暴者）、**Career Guide**（职业向导）、**Coding Partner**（编程伙伴）、**Writing Editor**（写作编辑）和 **Learning Coach**（学习辅导）4。

- **Copy & Customize（复制与定制）：**  用户无法直接修改官方 Gems，但可以使用“Make a copy”（创建副本）功能。这不仅是为了微调，更是学习官方 Prompt 写作技巧的绝佳途径。通过查看官方 Gem 的底层指令，用户可以洞察 Google 提示词工程师是如何构建复杂逻辑的 4。

### **3.4 局限性与协作**

目前，**Gems 无法在 Canvas 界面中直接调用**。这是一个重要的架构限制 22。如果用户在一个 Gem 对话中生成了长代码，无法直接点击“Canvas”进入编辑模式。用户需要手动复制内容到新的 Canvas 对话中，或者等待 Google 未来的功能整合。

---

## **4.**  **教育领域的双重架构：Learning Coach Gem 与 Guided Learning Feature**

在 Gemini 的教育应用中，存在两个容易混淆的概念：“Learning Coach”（学习辅导 Gem）和“Guided Learning”（引导式学习功能）。深刻理解二者的区别对于教育工作者至关重要。

### **4.1 核心差异对比表**

为了清晰区分，我们首先通过表格对比这两个功能的技术实现与应用场景：

|特性维度|Learning Coach (Gem)|Guided Learning (Feature)|
| :---------| :-------------------------------------------------------| :--------------------------------------------------------|
|**技术本质**|**角色实体 (Persona)** ：基于系统提示词的定制化智能体|**系统模式 (System Mode)** ：基于 LearnLM 模型的独立交互引擎 5|
|**核心逻辑**|模拟人类导师的语气，提供建议和计划|强制执行苏格拉底式提问，多模态互动，拒绝直接给出答案 24|
|**灵活性**|**高**：用户可以完全修改其指令（例如改为“严厉的数学老师”）|**低**：遵循固定的教学法流程，不可修改底层逻辑|
|**多媒体支持**|标准：可以生成图片，但主要基于文本|**极高**：原生集成测验 (Quizzes)、交互式图表、视频 5|
|**触发方式**|通过 Gem Manager 选择|通过聊天界面的 "Tools" 菜单激活 25|
|**适用场景**|制定学习计划、模拟面试、特定风格的对话练习|深度概念理解、复习备考、从零开始学习复杂主题|

### **4.2 Guided Learning（引导式学习）：LearnLM 的教学革命**

**Guided Learning** 是 Gemini 教育版图中的旗舰功能，其背后是 Google DeepMind 研发的 **LearnLM** 模型家族 5。

#### **4.2.1 苏格拉底式教学法（Socratic Method）**

与传统 AI 有问必答不同，Guided Learning 被设计为\*\*“反直觉”的。当用户问“光合作用是什么？”时，它不会直接输出定义，而是会反问：“你对植物如何获取能量有什么了解吗？”或者“你听说过叶绿体吗？”。  
这种通过提问引导用户自我构建知识的过程，被称为苏格拉底式教学。其目的是培养深度理解（Deep Understanding）\*\*而非浅层记忆 27。

#### **4.2.2 多模态与测验集成**

Guided Learning 的输出不仅是文本，它会自动生成：

- **交互式测验（Interactive Quizzes）：**  在讲解完一个概念后，直接插入选择题让用户作答，答对才继续 5。
- **视觉辅助：**  自动拉取相关的图表或 YouTube 视频片段，以辅助解释复杂概念（如细胞结构、物理向量）5。

#### **4.2.3 启用方法与平台差异**

目前（2025/2026），Guided Learning 处于分批推送阶段：

- **移动端优先：**  该功能在 Gemini App 上更为普及。
- **Web 端入口：**  用户需点击输入框附近的  **"Tools"** （工具）图标，在下拉菜单中寻找 "Guided Learning"。如果未显示，可能需要通过移动端开启对话后，再在 Web 端接续 29。

### **4.3 Learning Coach Gem：可定制的学伴**

Learning Coach Gem 则更像是一个灵活的助教。它预设的指令是帮助用户拆解复杂话题、制定学习计划。

- **优势：**  用户可以对其进行“魔改”。例如，可以复制官方的 Learning Coach，然后添加指令：“你是一个专门辅导雅思口语的教练，请只用英语和我交流，并纠正我的每一个语法错误。” 这种针对特定考试或学科的定制能力，是 Guided Learning 模式所不具备的 4。

---

## **5.**  **综合工作流与未来展望**

### **5.1 高效工作流范式**

为了最大化利用 Gemini 的这三大功能，建议专业用户采用以下**组合工作流**：

1. **Gems 定义专家：**  首先，利用 Gems 创建或选择一个特定领域的专家（例如“SEO 优化大师”）。在这个 Gem 中进行头脑风暴、策略制定和知识检索。
2. **Canvas 承载产出：**  当 Gems 构思好大纲或核心逻辑后，切换到标准对话或 Canvas 模式（由于目前无法直接集成，可能需要 Copy-Paste），利用 Canvas 的写作/编程模式进行长文档的生成和精细化打磨。利用 Canvas 的“高亮编辑”功能润色细节。
3. **Guided Learning 辅助内化：**  如果在工作过程中遇到不懂的技术概念（例如“什么是 Transformer 架构”），不要直接问 Gem，而是切换到 Guided Learning 模式进行 10 分钟的深度学习，确保自己真正理解了核心原理，从而更好地指挥 AI 工作。

### **5.2 技术规格与限制总结**

- **上下文窗口：**  Gemini Advanced 用户拥有 100 万 token 的上下文窗口，这对于在 Canvas 中处理大型代码库或在 Gems 中上传整本书作为知识库至关重要 32。
- **文件类型支持：**  支持几乎所有主流文本与媒体格式，但要注意 Gems 的知识库文件更新机制（依赖 Drive 链接）与 Canvas 的直接上传机制（一次性 Context）的区别 12。

通过掌握 Canvas 的空间编辑能力、Gems 的角色持久化技术以及 Guided Learning 的深度教学逻辑，用户实际上拥有了一个由 AI 驱动的、可无限扩展的个人智囊团与生产力中心。

#### **引用的著作**

1. New Gemini features: Canvas and Audio Overview \- Google Blog, 访问时间为 十一月 25, 2025， [https://blog.google/products/gemini/gemini-collaboration-features/](https://blog.google/products/gemini/gemini-collaboration-features/)
2. Generative UI: A rich, custom, visual interactive user experience for any prompt, 访问时间为 十一月 25, 2025， [https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)
3. Use Gems in Gemini Apps \- Computer \- Google Help, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop](https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop)
4. 5 tips on getting started with Gems, your custom AI experts \- Google Blog, 访问时间为 十一月 25, 2025， [https://blog.google/products/gemini/google-gems-tips/](https://blog.google/products/gemini/google-gems-tips/)
5. Guided Learning in Gemini: From answers to understanding \- Google Blog, 访问时间为 十一月 25, 2025， [https://blog.google/outreach-initiatives/education/guided-learning/](https://blog.google/outreach-initiatives/education/guided-learning/)
6. Create docs, apps & more with Canvas \- Android \- Gemini Apps Help \- Google Help, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/answer/16047321?hl=en&co=GENIE.Platform%3DAndroid](https://support.google.com/gemini/answer/16047321?hl=en&co=GENIE.Platform%3DAndroid)
7. Gemini Canvas \- Google Gemini, 访问时间为 十一月 25, 2025， [https://gemini.google.com/canvas](https://gemini.google.com/canvas)
8. Google Gemini Canvas Update: Create Presentations in Seconds with One Prompt \- Reddit, 访问时间为 十一月 25, 2025， [https://www.reddit.com/r/aicuriosity/comments/1oo26x5/google_gemini_canvas_update_create_presentations/](https://www.reddit.com/r/aicuriosity/comments/1oo26x5/google_gemini_canvas_update_create_presentations/)
9. Create docs, apps and more with Canvas \- Computer \- Gemini Apps Help \- Google Help, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/answer/16047321?hl=en-NZ&co=GENIE.Platform%3DDesktop](https://support.google.com/gemini/answer/16047321?hl=en-NZ&co=GENIE.Platform%3DDesktop)
10. Google Gemini's latest update lets you highlight and fine-tune its responses, 访问时间为 十一月 25, 2025， [https://www.xda-developers.com/google-gemini-highlight-tune-responses/](https://www.xda-developers.com/google-gemini-highlight-tune-responses/)
11. Supported languages, IDEs, and interfaces | Gemini for Google Cloud, 访问时间为 十一月 25, 2025， [https://docs.cloud.google.com/gemini/docs/codeassist/supported-languages](https://docs.cloud.google.com/gemini/docs/codeassist/supported-languages)
12. Upload & analyze files in Gemini Apps \- Computer \- Google Help, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop](https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop)
13. Gemini Canvas for Beginners: A Step-by-Step Guide \- Hugging Face, 访问时间为 十一月 25, 2025， [https://huggingface.co/blog/proflead/gemini-canvas](https://huggingface.co/blog/proflead/gemini-canvas)
14. How to Use Gemini Canvas Mode: From Docs to Dynamic Web Apps \- YouTube, 访问时间为 十一月 25, 2025， [https://www.youtube.com/watch?v=r7QbrtmNNTI](https://www.youtube.com/watch?v=r7QbrtmNNTI)
15. Keyboard shortcuts for Gemini Code Assist features \- Google for Developers, 访问时间为 十一月 25, 2025， [https://developers.google.com/gemini-code-assist/docs/keyboard-shortcuts](https://developers.google.com/gemini-code-assist/docs/keyboard-shortcuts)
16. Gemini Explore \- Working with the Canvas : Geminidata Support, 访问时间为 十一月 25, 2025， [https://support.geminidata.com/support/solutions/articles/73000158385-gemini-explore-working-with-the-canvas](https://support.geminidata.com/support/solutions/articles/73000158385-gemini-explore-working-with-the-canvas)
17. New in Gemini: Custom Gems and improved image generation with Imagen 3 \- Google Blog, 访问时间为 十一月 25, 2025， [https://blog.google/products/gemini/google-gemini-update-august-2024/](https://blog.google/products/gemini/google-gemini-update-august-2024/)
18. How to Use Google Gems \- The New School, 访问时间为 十一月 25, 2025， [https://services.newschool.edu/TDClient/32/Portal/KB/PrintArticle?ID=1364](https://services.newschool.edu/TDClient/32/Portal/KB/PrintArticle?ID=1364)
19. The Ultimate Guide to Google Gemini Gems | by Leon Nicholls \- Medium, 访问时间为 十一月 25, 2025， [https://leonnicholls.medium.com/the-ultimate-guide-to-google-gemini-gems-78182be784af](https://leonnicholls.medium.com/the-ultimate-guide-to-google-gemini-gems-78182be784af)
20. Tips for creating custom Gems \- Gemini Apps Help, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/answer/15235603?hl=en](https://support.google.com/gemini/answer/15235603?hl=en)
21. Supported input files and requirements | Firebase AI Logic \- Google, 访问时间为 十一月 25, 2025， [https://firebase.google.com/docs/ai-logic/input-file-requirements](https://firebase.google.com/docs/ai-logic/input-file-requirements)
22. Canvas with Gems? : r/Bard \- Reddit, 访问时间为 十一月 25, 2025， [https://www.reddit.com/r/Bard/comments/1jxezbq/canvas_with_gems/](https://www.reddit.com/r/Bard/comments/1jxezbq/canvas_with_gems/)
23. Canvas doesnt work if using Gems? \- Google Help, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/thread/343170030/canvas-doesnt-work-if-using-gems?hl=en](https://support.google.com/gemini/thread/343170030/canvas-doesnt-work-if-using-gems?hl=en)
24. Google Gemini's Guided Learning feature makes AI actually check if you understand — here's how it works, 访问时间为 十一月 25, 2025， [https://www.tomsguide.com/ai/google-gemini/google-geminis-guided-learning-feature-makes-ai-actually-check-if-you-understand-heres-how-it-works](https://www.tomsguide.com/ai/google-gemini/google-geminis-guided-learning-feature-makes-ai-actually-check-if-you-understand-heres-how-it-works)
25. 访问时间为 十一月 25, 2025， [https://www.tomsguide.com/ai/google-gemini/google-geminis-guided-learning-feature-makes-ai-actually-check-if-you-understand-heres-how-it-works#:~:text=Open%20the%20Gemini%20app%20or,any%20topic%20using%20natural%20language.](https://www.tomsguide.com/ai/google-gemini/google-geminis-guided-learning-feature-makes-ai-actually-check-if-you-understand-heres-how-it-works#:~:text=Open%20the%20Gemini%20app%20or,any%20topic%20using%20natural%20language.)
26. 访问时间为 十一月 25, 2025， [https://www.tomsguide.com/ai/google-gemini/google-geminis-guided-learning-feature-makes-ai-actually-check-if-you-understand-heres-how-it-works#:~:text=Activate%20Guided%20Learning%20mode&text=Open%20the%20Gemini%20app%20or,activate%20the%20interactive%20tutoring%20mode.](https://www.tomsguide.com/ai/google-gemini/google-geminis-guided-learning-feature-makes-ai-actually-check-if-you-understand-heres-how-it-works#:~:text=Activate%20Guided%20Learning%20mode&text=Open%20the%20Gemini%20app%20or,activate%20the%20interactive%20tutoring%20mode.)
27. How Gemini's Guided Learning can help you study more effectively \- Google Blog, 访问时间为 十一月 25, 2025， [https://blog.google/products/gemini/guided-learning-google-gemini/](https://blog.google/products/gemini/guided-learning-google-gemini/)
28. ‎Gemini Apps' release updates & improvements, 访问时间为 十一月 25, 2025， [https://gemini.google/release-notes/](https://gemini.google/release-notes/)
29. Guided Learning Feature Not Showing In Web Version Of Gemini\! \- Google Help, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/thread/369163376/guided-learning-feature-not-showing-in-web-version-of-gemini?hl=en](https://support.google.com/gemini/thread/369163376/guided-learning-feature-not-showing-in-web-version-of-gemini?hl=en)
30. Gemini Guided Learning Mode \- Unavailable on web/desktop, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/thread/365308818/gemini-guided-learning-mode-unavailable-on-web-desktop?hl=en](https://support.google.com/gemini/thread/365308818/gemini-guided-learning-mode-unavailable-on-web-desktop?hl=en)
31. Guided learning dost work on gemini web, 访问时间为 十一月 25, 2025， [https://support.google.com/gemini/thread/372485291/guided-learning-dost-work-on-gemini-web?hl=en](https://support.google.com/gemini/thread/372485291/guided-learning-dost-work-on-gemini-web?hl=en)
32. 5 ways Gemini can help students study smarter \- Google Blog, 访问时间为 十一月 25, 2025， [https://blog.google/products/gemini/google-gemini-learning-features/](https://blog.google/products/gemini/google-gemini-learning-features/)
33. Which model should I use? And what's the difference between them? : r/GeminiAI \- Reddit, 访问时间为 十一月 25, 2025， [https://www.reddit.com/r/GeminiAI/comments/1k6ldfz/which_model_should_i_use_and_whats_the_difference/](https://www.reddit.com/r/GeminiAI/comments/1k6ldfz/which_model_should_i_use_and_whats_the_difference/)
