#  **“作家-工程师”蓝图：构建百万字科幻连载小说的AI协作工作流与提示词工程大师课**

## **报告导言：重新定义“作者”——“作家-工程师”的崛起**

在当代，创作一百万字的起点中文网（以下简称“起点”）科幻连载小说，已不仅仅是一个文学创作问题，更是一个复杂的工业生产与项目管理挑战。您所面对的，是如何在长达数百个更新日内，维持高速、高质量、高吸引力的内容输出。这其中涉及三大核心难题：

1. **规模的诅咒（The Curse of Scale）：**  百万字（约等于标准纸质小说的十卷）的体量对情节、角色和世界观的一致性（Consistency）提出了极端考验 。
2. **AI的局限（The AI Limitation）：**  以Gemini 2.5 Pro为代表的大型语言模型（LLM）虽然功能强大，但在长篇叙事中存在“叙事漂移”和“记忆缺失”的固有问题 。
3. **平台的算法（The Platform Algorithm）：**  起点模式的精髓在于其对“爽点”（Shuangdian）和“钩子”（Hooks）的算法级依赖，这要求内容生产必须高度工程化和可复制 。

因此，本次任务的交付成果，并非一份传统的写作指南，而是一套 **“作家-工程师”（Author-Engineer）** 的工作流蓝图。  
传统的人机协作模型（如“AI辅助30%”）已然过时 。我们将采用一个**多维框架** ，将您（人类作者）的角色从“执笔者”提升为“**项目架构师**”和“**创意总监**”。在此框架中，您将负责定义**内容生成、结构辅助、创意输入**和**分析贡献**四大轴线 ，而AI（Gemini 2.5 Pro）则扮演您的“**首席技术执行官**”（CTO）和“**7x24小时的助理团队**”。  
本报告将分为七个部分，系统化地为您构建从“零”到“一百万字”的完整工业化生产管线。

## **第一部分：阶段一：战略脚手架——定义三大核心挑战**

在启动这个宏伟项目之前，必须精确评估我们将要克服的结构性障碍。

### **1.1 百万字叙事的结构性挑战**

一百万字不是一部“长篇小说”，它是一个**系列（Series）**  。传统的线性写作方法（从第一章写到最后一章）在这种规模下面临着极高的失败风险，主要体现在精疲力竭和结构崩溃 。正如研究所指出的，这是一个“哥斯拉级别的情节”（Godzilla-sized plot） ，任何没有预先规划的尝试，都可能导致作者在中途迷失，使草稿变得混乱不堪，修订工作比初稿写作还要艰巨 。

### **1.2 Gemini 2.5 Pro的“长上下文”局限**

Gemini 2.5 Pro拥有高达100万Token的上下文窗口（Context Window），这在理论上可以容纳约75万英文单词或1500页文本 。然而，必须清醒地认识到“**输入上下文**”和“**有效长篇生成**”是两个截然不同的概念：

1. **输出限制：**  模型的单次最大输出（Output Token Limit）远小于其输入窗口（例如约65,535 Token） 。这意味着您不能“一次性”生成百万字。
2. **叙事漂移（Narrative Drift）：**  即便拥有长上下文，AI在连续生成几十万字后，也会不可避免地“忘记”早期的设定和微妙的情感铺垫 。研究表明，AI在长篇生成中难以进行高级“规划”（Planning） 。
3.  **“2000词障碍”：**  此前对LLM的研究发现，模型在生成超过2000词的连贯输出时会遇到困难 。虽然Gemini 2.5 Pro已远超此限，但原理相通：AI擅长“补完”，不擅长“构建”。

因此，我们的工作流*不能*依赖AI的“记忆”，而必须建立一个**外部化的、AI可读的“记忆宫殿”** 。

### **1.3 “起点算法”的逆向工程**

起点小说的核心不是“故事”，而是“**读者留存系统**”。其成功的关键在于两个可工程化的组件：

1. **爽点（Shuangdian）：**  爽点是起点小说的存在方式 。它是一种精心设计的“读者效果”，通过情节上**从“逆境”快速（甚至反复）转向“顺境”** 来达成 。这种“爽”的实现，依赖于“金手指”（Golden Finger）的设定，它以最小的逻辑代价，支撑了主角的成功 。
2. **钩子（Hook）：**  即**章节悬念（Chapter Cliffhangers）** 。在连载模式下，每一章的结尾都必须是下一章的“付费入口”。

我们的工作流必须将“爽点”和“钩子”从“灵感”变为“**可量产的工业组件**”。

## **第二部分：阶段二（上）：奠定基石——构建“中心世界数据库”（CWD）**

针对第一部分中的“一致性”和“AI记忆”挑战，我们的核心解决方案是**中心世界数据库（Central World Database, CWD）** 。

### **2.1 CWD：AI的“单一事实来源”（SSOT）**

CWD是您项目的“单一事实来源”（Single Source of Truth）。它是一个外部化的、结构化的“第二大脑”，用于解决LLM的“叙事漂移”问题 。AI在任何时候都不需要“记住”设定，它只需要“**读取**”您提供的CWD文件。  
这种方法已被证实在长篇AI辅助写作中极为有效。一位作者使用**Markdown参考文件**作为上下文管理系统，成功在8天内撰写了12.6万字的小说，完美解决了AI在第45章忘记第3章设定的问题 。

### **2.2 CWD的工程化构建（结构与格式）**

CWD必须是**AI可读的（AI-Readable）** 。这意味着它不应是随意的笔记，而应是结构化的**Markdown（.md）文件**（或JSON/XML）。Gemini 2.5 Pro可以轻松解析这些格式。  
您的CWD应包含以下文件结构：

- CWD/
  - project_bible.md: (记录小说的核心风格、基调、目标受众和“不可违背”的元规则)。
  - plot_macro.md: (您的高层宏观情节大纲，即“雪花法”的第一层 )。
  - characters/
    - char_001_protagonist.md: (主角的详细档案：动机、目标、口癖、能力、*声音* )。
    - char_002_antagonist.md: (反派档案)。
  - world/
    - lore_001_physics.md: (科幻设定：物理法则、超光速原理)。
    - lore_002_factions.md: (势力设定：星际帝国、公司)。
  - locations/
    - loc_001_capital_city.md: (首都的感官细节：气味、声音、建筑风格)。
  - series_continuity.md: (一个动态更新的日志，记录已发生的关键事件、埋下的伏笔，防止“吃书”)。

在执行**第四部分（每日生产循环）** 时，您不需要AI“记住”主角，您只需在提示词中“**附加**”char_001_protagonist.md文件。

## **第三部分：阶段二（下）：宏观规划与“起点算法”设计**

在CWD建立之后，我们进入宏观规划阶段。这里，我们将人类的“灵感”与AI的“算力”相结合，并将其对齐“起点”的商业模式。

### **3.1 传统规划与AI的结合**

您（人类）必须提供小说的核心创意骨架。AI无法从零开始创造一个伟大的百万字结构 。

1. **人类优先的“堆肥”** ：采用一种结构化大纲方法，如“**雪花法**”（Snowflake Method） ，从一句话总结开始，逐步扩展为段落、人物简介和场景列表。或者，撰写一份“**长篇概要**”（Long-Form Synopsis） ，在动笔前就解决掉所有重大的情节漏洞。这个人类主导的“堆肥”（Composting）阶段是不可或缺的 。
2. **AI辅助的“头脑风暴”** ：一旦有了基本骨架，就使用AI作为“**无限的‘是的，而且’（Yes, and）伙伴**” 进行创意爆发。使用如Sudowrite的“画布”（Canvas）功能 或直接向Gemini 2.5 Pro提问，进行“**What-If情景推演**” 。
   - *提示词示例*：“基于我的大纲第5点[粘贴大纲]，生成5种可能的黑暗转折。哪一种最具戏剧张力？”

### **3.2 设计可复制的“起点算法”**

这是项目的核心工程。我们必须将“爽点”和“钩子”工业化。

#### **3.2.1 循环“爽点”模型（The Cyclic "Shuangdian" Model）**

您的百万字小说将由约10个“**主线篇章**”（Main Arcs）构成，每个“主线篇章”由5-10个“**微型篇章**”（Mini-Arcs）构成。  
每一个“微型篇章”（约5-10章）**必须**遵循以下循环 ：

1. **逆境（Adversity）** ：主角遇到问题、受到羞辱、处于劣势。
2. **过程（Process）** ：主角运用“金手指” 或学习新技能以应对挑战。
3. **转折（Reversal）** ：主角正面解决问题。
4. **爽点（Shuangdian）** ：即“**回报场景**”（Reward Scene） 。这是高光时刻，是公众的震惊、反派的错愕、主角的胜利宣言。**这是读者付费的根本原因**。
5. **悬念（Cliffhanger）** ：一个更大的威胁、一个新问题或一个未解之谜被引入，立即启动下一个“微型篇章”的“逆境”阶段。

#### **3.2.2 章节悬念（Cliffhanger）的精通**

在连载模式中，章节结尾*不是*休息站，而是“**加速器**” 。您的目标是让读者无法停止。我们必须建立一个“悬念库”，基于研究 ，至少包括：

- **挑衅性问题（The Provocative Question）** ：通常是主角的内心独白。（“……但如果他在这里，那艘船上的人是谁？”）
- **事实陈述/指控（The Statement of Fact）** ：一个震惊的揭露。（“我知道你不是来自这个时空。”）
- **未完成的行动（The Unfinished Action）**  ：（起点最常用的）主角举起了枪，瞄准了目标……（本章完）。
- **行动需求（The Demand for Action）**  ：外部事件强行介入。（“警报声响彻了整个基地。”）

## **第四部分：阶段三：每日生产循环（AI辅助的“流水线”）**

这是将“规划”转化为“日更”战术执行的核心。

### **4.1 核心教条：“迭代分层”法**

我们**永远不会**向AI发出“写第五章”这样的指令。这种指令只会产生“通用的废话”（Generic Fluff） ，导致您需要花费更多时间去“编辑”AI的糟糕产出。  
我们将采用一种“**迭代分层**”（Iterative Layering）的方法 。这种方法将一个复杂的任务（写一个3000字的章节）分解为一系列更简单、更可控的子任务。这在技术上被称为“**提示词链**”（Prompt Chaining） 。  
“提示词链”的逻辑是，**第一个提示的输出（Output）成为第二个提示的输入（Input）/上下文（Context）**  。我们像渲染3D模型一样，一层一层地“渲染”我们的章节。

### **4.2 每日章节“渲染”清单（5步流程）**

这是您的每日“流水线”清单。

- **步骤 0：上下文准备（人类 + AI）**
  - *人类（架构师）* ：为您要写的章节，从CWD中选取**相关**的上下文文件。（例如：char_001.md，char_004.md，loc_007.md，以及您的宏观大纲）。
  - *AI（执行者）* ：将这些文件（以及为保持风格一致性的前5-10个章节）加载到Gemini 2.5 Pro的100万Token上下文窗口中 。
- **步骤 1：“动作骨架”层（AI生成，人类指导）**
  - *人类提示*：“根据宏观大纲第10.3点（‘主角与叛徒对峙’），生成一个500字的 **‘动作骨架’（Action Skeleton）** 。**只**关注物理动作、运动和事件顺序。不要包含任何对话、内心想法或感官描写。” 。
- **步骤 2：“感官细节”层（AI生成，人类调整）**
  - *人类提示*：“[粘贴步骤1的‘动作骨架’]。现在，将其扩展到1000字，添加一个 **‘感官层’（Sensory Layer）** 。根据loc_007.md文件，详细描述这个场景的气味、声音、光照和材质。” 。
- **步骤 3：“对话”层（AI生成，人类润色）**
  - *人类提示*：“[粘贴步骤2的场景]。现在，填入角色1和角色4之间的对话。严格遵守char_001.md和char_004.md中的**声音（Voice）** 和口癖。对话必须围绕[主题]，并揭示[隐藏动机]。” 。
- **步骤 4：“内部独白与情感”层（人类主导）**
  - **这是最关键的一步。**  研究表明，AI在生成深刻、微妙、非陈词滥调的内部情感方面表现不佳 。AI生成的文本缺乏“人味”（Human Narrative） 。
  - 此时，*您*，作为**人类作者**，介入这个AI生成的“脚手架”（Scaffold）。您来撰写那些赋予故事灵魂的批判性内心思想、情感反应和犹豫不决 。**AI负责构建舞台，人类负责登台表演。**
- **步骤 5：“悬念”层（AI辅助，人类选择）**
  - *人类提示*：“[粘贴步骤4的完整章节]。下一章的情节是[‘主角被捕’]。请为此章节生成3个备选的悬念结尾，分别使用‘**挑衅性问题**’和‘**未完成的行动**’类型。” 。

### **4.3 表格1：人机协作“流水线”分工表**

此表格总结了您的每日生产流程，将抽象的“写作”转变为具体的、工业化的“生产”。

|阶段|任务|人类角色（架构师）|AI角色（执行者）|关键提示词（示例）|
| :-----| :-----------| :----------------------------| :------------------------------| :--------------------------------------------|
|**0. 准备**|上下文注入|选择相关的CWD文件和大纲点。|加载数据到1M Token窗口 。|（无提示词，操作层面）|
|**1. 骨架**|动作层|定义情节节点。|生成纯动作/事件流 。|"生成‘动作骨架’。只许动作，不许对话。"|
|**2. 感官**|环境层|提供CWD中的地点文件。|用感官细节丰富“骨架” 。|"拿[骨架]添加‘感官层’，使用loc_00[span_25](start_span)​[span_25](end_span)7.md。"|
|**3. 对话**|交互层|提供CWD中的角色文件和动机。|生成符合角色“声音”的对话 。|"拿[场景]填入对话。遵循char_001.md的口癖。"|
|**4. 情感**|灵魂层| **（核心贡献）**  编写内心独白。|（仅提供脚手架）|（人类亲自撰写）|
|**5. 悬念**|钩子层|定义下一章的目标。|生成多种类型的悬念选项 。|"生成3个‘未完成的行动’型悬念。"|

## **第五部分：阶段四：修订与分析（AI作为诊断工程师）**

### **5.1 问题：速度的代价**

第四部分中的“每日生产循环”专为**速度**而设计。但速度不可避免地会导致错误：情节漏洞、角色OOC（Out of Character）、设定前后矛盾，以及糟糕的节奏 。  
等到一百万字写完再回头修订，是一个不可能完成的任务 。

### **5.2 解决方案：“敏捷修订”与AI驱动的“逆向大纲”**

我们将借鉴软件开发中的“**敏捷（Agile）** ”方法论。我们不进行“瀑布式”开发（写完再改），而是进行“**迭代冲刺**”（Sprints）。

- **冲刺（Sprint）** ：设定一个工作单元，例如每10个章节（或5万字）为一个“冲刺”。
- **诊断（Diagnostics）** ：在每个“冲刺”结束时，我们不立即开始下一个冲刺，而是运行一次**AI驱动的诊断**。

这个诊断的核心技术叫做“**逆向大纲**”（Reverse Outlining） 。  
“逆向大纲”不是你*计划*要写什么，而是AI通过阅读你*已经写*的内容，为你生成一份大纲 。这对于那些在写作中途偏离了原始大纲的“随性”作者（Pantser）或“半规划半随性”作者（Plantser）来说，是至关重要的 。

### **5.3 “敏捷修订”流程**

1. 完成一个10章（5万字）的“冲刺”。
2. 将这10个章节的**全部文本**，连同您的**整个CWD**，加载到Gemini 2.5 Pro的100万Token上下文窗口中 。
3. **运行“诊断大师”提示词（人类）** ：  
   “你是一位顶级的**情节分析师**和**连续性编辑** 。请阅读我附加的[10个章节]和我整个。请执行以下任务：
   1. 为每一章的每一个场景，生成**一句话的摘要** 。 > 2. 列出在这10章中**新引入**的所有情节线索。
   2. 列出在CWD中提到、但在这10章中**被遗忘**或**未推进**的情节线索。
   3. 将所有角色的行为与他们在CWD中的**动机和性格**进行交叉对比，报告任何**OOC或不一致**的地方。
   4. 分析这10章的**叙事节奏** ：指出哪些章节**过慢**（过多的描写/解释），哪些**过快**（过多的动作而缺乏情感反应）。”
4. **分析结果**：您将收到一份高维度的“**诊断报告**”。这份报告让您能“**见森林**”（整体结构），而不仅仅是“见树木”（日常章节）。您可以立即修复逻辑谬误 ，在它们被后续的5万字内容掩盖之前。

## **第六部分：提示词工程大师课——成为叙事工程师**

要完美执行上述流程，您需要的不是“好的提示词”，而是“**工程化的提示词设计**”。

### **6.1 基础原则：从“提问”到“指令”**

- **新手**向AI“提问”。
- **专家**向AI“**下达指令**”（Instructions） 。
- **大师**为AI提供一个“**框架**”（Frameworks），让AI去填充 。

AI不是“读心者” 。您必须对**长度、格式、风格、语气和目标受众**做出*明确*的规定 。  
**迭代是关键**：*永远不要接受第一个答案* 。从一个简单的提示开始，观察AI在哪里失败，然后*迭代地*优化您的提示词以纠正那个失败 。

### **6.2 核心模型：精通PTCF四要素**

每一个强大的提示词，无论多复杂，都由四个核心部件构成 。

1. **P - Persona（角色/身份）** ：定义AI*是谁*。这是设定语气和专业知识最快的方法 。
2. **T - Task（任务）** ：具体的、以**动作动词**开头的目标 。
3. **C - Context（上下文）** ：AI执行任务所需的所有背景信息。这包括CWD文件、之前的文本、情感状态等 。
4. **F - Format（格式）** ：您希望输出的*结构*。要求结构化数据（如JSON或Markdown）是一种高级技巧 。

### **6.3 表格2：PTCF提示词设计矩阵**

此参考表将PTCF理论 转化为实战指南。

|组件|功能（为什么使用它）|新手示例（糟糕的）|大师级示例（工程化的）|
| :-----| :---------------------------------| :-----------------------| :--------------------------------------------------------------------------------------------------------------------------|
|**Persona**|设定AI的专业知识、语气和风格。|(无)|"你是一位[威廉·吉布森]风格的硬核科幻作家，语言精炼、冷峻。"|
|**Task**|定义一个清晰的、可执行的动作。|"给我写点关于战斗的。"|"**重写**以下段落，使其**张力提升**。专注于角色的物理反应和短促的句子。"|
|**Context**|提供AI做出正确判断所需的信息。|"主角很生气。"|"主角[李牧]刚刚得知了他的伙伴[王海]的背叛（见char_001.md）。他处于震惊和愤怒的压抑状态。他正试图在敌人面前隐藏这种情绪。"|
|**Format**|约束AI的输出，使其可预测、可用。|"写出他们的对话。"|"以**JSON列表**格式提供对话。每个条目包含：{'character': '名字', 'line': '台词', 'subtext': '潜台词'}。"|

### **6.4 “作家-工程师”的高级策略**

1. **提示词链（Prompt Chaining）**  ：
   - 如第四部分所述。这是构建复杂性的关键。Prompt 1（骨架）的输出，成为Prompt 2（感官）的**上下文**。这使您能够分层控制质量 ，并绕过输出长度限制 。
2. **少样本提示（Few-Shot Prompting）**  ：
   - “零样本”（Zero-Shot，只有指令）在风格上不可靠。“少样本”（提供2-3个例子）是**训练AI模仿您风格**的最有效方法。
   - *提示词示例*：“任务：重写以下[场景]。**风格示例**：[在此粘贴300字您自己的、风格鲜明的写作片段]。现在，用这种风格重写：[粘贴AI生成的平淡文本]。”
3. **框架提示（Framework Prompting）**  ：
   - **最强大的工程方法**。不要让AI“写作”，而是给它一个**模板（Template）**  ，让它“**填空**”。这强制AI进入您想要的结构，也是我们“起点提示词武库”的支柱。

### **6.5 表格3：可复用的“起点提示词武库”（模板库）**

这是您为百万字小说准备的、可**即插即用**的“函数库”。

|模板名称|目标|大师级提示词模板（[变量]为待填充项）|
| :---------| :--------------------------------------------| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**1. “爽点”爆发器**|生成高潮的、令读者满足的“回报”场景 。|**Persona**: 你是顶级的起点网文大神。 **Context**: 主角[主角名]刚刚使用[金手指能力]战胜了[逆境/反派]。[观众/配角]正在围观。 **Task**: 撰写一个1000字的场景，将**80%的笔墨用于描述旁观者的[震惊反应]** 、**反派的[错愕与崩溃]** ，以及**主角的[内心满足与低调宣示]** 。必须极大化“爽”感。|
|**2. 高速对话生成器**|生产快节奏、充满潜台词、推动情节的对话 。|**Persona**: 你是一位金牌编剧。 **Context**: [角色A]（情绪：[A的情绪]）正在就[事件]质问（情绪：）。他们之间隐藏的**潜台词**是。 **Task**: **只**写出这场戏的对话。**台词必须简短**（每句不超过20字）。专注于冲突、节奏和潜台词。**禁止**任何描述性文字。|
|**3. 多视角（POV）切换器**|从多个角度描绘同一关键事件，增加叙事深度 。|*Task*: 撰写以下场景[场景简介]： 1. 使用[角色A]的第一人称视角 **。严格遵循char_003.md的“声音”。聚焦于。 2. 使用的**第一人称视角**。严格遵循char_005.md的“声音”。聚焦于。 **Format**: 两个视角之间用---POV BREAK---分隔。|
|**4. 章节悬念（钩子）生成器**|制造“下一章，快点”的付费冲动 。|**Context**: 本章在[主角的最后一个动作]处结束。下一章的**核心情节**是[下一章的事件]。 **Task**: 生成3个**备选的**章节结尾段落，每个结尾段落不超过100字。 1. 必须包含一个“**挑衅性问题**”类型（主角的内心思考）。<br />2. 必须包含一个“**未完成的行动**”类型（动作在最高点中断）。|
|**5. 紧张/氛围营造器**|减慢节奏，通过感官细节构建悬念和恐怖感 。|**Persona**: 你是恐怖小说大师。 **Context**: [角色名]刚刚进入[一个黑暗/未知的地点，见loc_009.md]。 **Task**: 撰写一个500字的段落。**禁止**让任何“事件”发生。**只**专注于[角色]的**感官细节**（他听到的滴水声、闻到的铁锈味、黑暗中的视觉错觉）和他**无法控制的物理反应**（心跳、汗水、鸡皮疙瘩）。**只**构建“期待感”。|

## **第七部分：结论性战略建议与伦理考量**

### **7.1 警惕“创意的让渡”（Creative Abdication）**

使用此工作流最大的危险，不是AI会失败；而是AI在产生 **“还行”的、平庸的**内容时**太成功了**。您将时时刻刻面临接受AI“第一稿”的诱惑 。  
您必须抵抗这种诱惑。您作为“作家-工程师”的职责，是成为一个**挑剔的策展人**和**无情的编辑**。AI是您的学徒，而您（人类）**永远**是那个拥有最终决定权的大师。

### **7.2 根除“AI主义”（AI-isms）**

AI模型有其风格“指纹”，它们会过度依赖某些陈词滥调 。您必须主动搜寻并销毁这些“AI主义”词汇，例如：

- “……的交响乐”
- “……的挂毯”
- “……的核心”
- “心在胸膛里狂跳”
- “一场……的舞蹈”
- 以及过度使用短句和片段来制造虚假紧张感 。

您作为人类的最终价值，是注入您的“**独特声音**”和“**原创的、新鲜的语言**” 。

### **7.3 关键的最后警告：数据隐私与所有权**

这是法律和伦理的底线：**谨慎选择您使用的AI服务**。  
如研究中所警告的，存在一种真实风险：您上传的任何内容（您的CWD、您的百万字手稿）都可能成为“**AI‘知道’的一部分**”，并被用于训练未来的模型 。  
**您绝对不能使用任何“免费”或“公共”版本的AI来执行此工作流。**   
您必须使用Gemini 2.5 Pro的“**企业版**”或“**专业版**”，并仔细阅读服务条款，确保您的数据**永远不会**被用于训练。将您百万字的知识产权上传到免费服务中，无异于“**智力自杀**”。

### **7.4 最终结论：您是导演，而非打字员**

完成这个项目，需要您转变身份。您不再是那个面对空白文档的“作家” 。  
您是一位**创意总监** ，一位**作家-工程师**。您负责指挥一个复杂的、技术与创意结合的系统，管理一个不知疲倦的数字助理团队，并最终做出那成千上万个微小而关键的、**只有人类才能做出的**艺术决策。  
AI将负责处理*数量*；而您，必须交付*质量*。

#### **引用的文献**

1. What are some ways to properly plan out a 1000000 word fanfiction? - Reddit, https://www.reddit.com/r/FanFiction/comments/wcnrwz/what_are_some_ways_to_properly_plan_out_a_1000000/ 2. How to Write Speculative Fiction of Truly Epic Proportions - Story Embers, https://storyembers.org/how-to-write-speculative-fiction-of-truly-epic-proportions/ 3. Write a Novel with AI: Stop Truncated Text with Gemini Pro - Arsturn, https://www.arsturn.com/blog/how-to-write-a-novel-with-ai-and-avoid-truncated-text 4. NexusSum: Hierarchical LLM Agents for Long-Form Narrative Summarization - arXiv, https://arxiv.org/html/2505.24575v1 5. LongEval: A Comprehensive Analysis of Long-Text Generation Through a Plan-based Paradigm - arXiv, https://arxiv.org/html/2502.19103v1 6. “爽”及其完成：网络类型小说的存在方式--网络文学--中国作家网, https://www.chinawriter.com.cn/n1/2024/1128/c404027-40370888.html 7. Human-AI Collaboration in Writing: A Multidimensional Framework ..., https://digitalcommons.lindenwood.edu/cgi/viewcontent.cgi?article=1727&context=faculty-research-papers 8. How to Write a Science Fiction Novel Series: 6 Tips - Writer's Digest, https://www.writersdigest.com/write-better-fiction/write-science-fiction-novel-series-6-tips 9. How to Write a Novel Outline | Writers.com, https://writers.com/how-to-write-a-novel-outline 10. Gemini 2.5 Pro Preview | Hacker News, https://news.ycombinator.com/item?id=43906018 11. LongWriter: Breaking the 2000-Word Barrier in Long Context LLMs | ml-news - Wandb, https://wandb.ai/byyoung3/ml-news/reports/LongWriter-Breaking-the-2-000-Word-Barrier-in-Long-Context-LLMs--Vmlldzo5MTI5Mjgy 12. How I Used AI Tools to Write a 126,000-Word Novel in Just Over a ..., https://www.reddit.com/r/WritingWithAI/comments/1mjwiuk/how_i_used_ai_tools_to_write_a_126000word_novel_in/ 13. How I Used AI Tools to Write a 126000-Word Novel in Just Over a Week. - Reddit, https://www.reddit.com/r/WritingWithAI/comments/1mjwiuk/how_i_used_ai_tools_to_write_a_126000word_novel/ 14. How To Write A Novel Using The Snowflake Method, https://www.advancedfictionwriting.com/articles/snowflake-method/ 15. Please share your writing prompts to get the best prose from AI : r/WritingWithAI - Reddit, https://www.reddit.com/r/WritingWithAI/comments/1kq9yti/please_share_your_writing_prompts_to_get_the_best/ 16. How to Use a Long-Form Synopsis to Plan Your Novel | Jane Friedman, https://janefriedman.com/how-to-use-a-long-form-synopsis-to-plan-your-novel/ 17. Sudowrite - Best AI Writing Partner for Fiction, https://sudowrite.com/ 18. How Writers Can Use AI to Brainstorm Stories - Inkling Creative Strategies, https://www.inklingcreative.work/post/how-writers-can-use-ai-to-brainstorm-stories 19. Using AI to Develop and Workshop Your Characters - Writer's Digest, https://www.writersdigest.com/write-better-fiction/using-ai-to-develop-and-workshop-your-characters 20. How to Use Chapter Cliffhangers in Your Fiction - Helping Writers ..., https://www.helpingwritersbecomeauthors.com/chapter-cliffhangers/ 21. How To Write Cliffhangers That Make Readers Click 'Next Chapter' | by Jennifer Ibhafidon, https://medium.com/@JenniferIbhafidon/how-to-write-cliffhangers-that-make-readers-click-next-chapter-d633b9f80138 22. 8 Ways to End a Chapter With a Cliffhanger – WriteOnSisters.com, http://writeonsisters.com/writing-craft/8-ways-to-end-a-chapter-with-a-cliffhanger/ 23. AI Prompting Tips from a Power User: How to Get Way Better Responses - Reddit, https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/ai_prompting_tips_from_a_power_user_how_to_get/ 24. What is prompt chaining? - IBM, https://www.ibm.com/think/topics/prompt-chaining 25. Prompt Chaining | Prompt Engineering Guide, https://www.promptingguide.ai/techniques/prompt_chaining 26. Getting Started with Prompt Chaining, https://promptengineering.org/getting-started-with-prompt-chaining/ 27. AI for Editing Novels - Colin's Notes, https://colinsblog.net/2025-05-15-AI-as-editor/ 28. 10 ChatGPT Prompt Templates That Help You With Story Writing | by Shushant Lakhyani, https://medium.com/@slakhyani20/10-chatgpt-prompt-templates-that-help-you-with-story-writing-5917315943b1 29. 10 AI Prompts for Better Scriptwriting - Magai, https://magai.co/10-ai-prompts-for-better-scriptwriting/ 30. Best ChatGPT Prompts for Story & Fiction Writing - Intellectual Lead, https://intellectualead.com/chatgpt-story-writing/ 31. Story writing - change in writing style - ChatGPT - OpenAI Developer Community, https://community.openai.com/t/story-writing-change-in-writing-style/1115400 32. AI and Creative Collaboration: How Machines and Humans Co-Create - Dragonfly AI, https://dragonflyai.co/resources/blog/ai-and-creative-collaboration-dragonfly-ai 33. A Stepwise AI-Assisted Long-Form Fiction Method - Papercut Post, https://www.papercutpost.com/a-stepwise-ai-assisted-long-form-fiction-method/ 34. Is it wrong to use AI to make more detailed chapter outlines off of ones I have already made?, https://www.reddit.com/r/writers/comments/1ievxzt/is_it_wrong_to_use_ai_to_make_more_detailed/ 35. Reverse Outlining Your Story - YouTube, https://www.youtube.com/watch?v=q_F7XW9gN60 36. Creating a Reverse Outline - The Writing Center - University of Wisconsin–Madison, https://writing.wisc.edu/handbook/reverseoutlines/ 37. Reverse Outlines: “Finding” your story during revisions - Chelsea Abdullah, https://www.chelseaabdullah.com/blog/reverse-outlines 38. Reverse Outlining With AI - AuthorMedia.social, https://authormedia.social/c/ai/reverse-outlining-with-ai 39. Reverse Outlining with Language Models - Maggie Appleton, https://maggieappleton.com/reverse-outline 40. Prompt Engineering for AI Guide | Google Cloud, https://cloud.google.com/discover/what-is-prompt-engineering 41. The ultimate guide to writing effective AI prompts - Work Life by Atlassian, https://www.atlassian.com/blog/artificial-intelligence/ultimate-guide-writing-ai-prompts 42. Google just released a 68-page guide on prompt engineering. Here are the most interesting takeaways - Reddit, https://www.reddit.com/r/ChatGPTPromptGenius/comments/1kpvvvl/google_just_released_a_68page_guide_on_prompt/ 43. Getting started with prompts for text-based Generative AI tools | Harvard University Information Technology, https://www.huit.harvard.edu/news/ai-prompts 44. Effective Prompts for AI: The Essentials - MIT Sloan Teaching & Learning Technologies, https://mitsloanedtech.mit.edu/ai/basics/effective-prompts/ 45. Iterative Prompt Development. Any prompt to the LLM(Large Language… | by Aanshsavla | Medium, https://medium.com/@aanshsavla2453/iterative-prompt-development-14252e0597f5 46. How to write effective AI prompts | Help center - Formaloo, https://help.formaloo.com/en/articles/9797669-how-to-write-effective-ai-prompts 47. Elements of a Prompt - Prompt Engineering Guide, https://www.promptingguide.ai/introduction/elements 48. Understanding Prompt Structure: Key Parts of a Prompt, https://learnprompting.org/docs/basics/prompt_structure 49. Overview of prompting strategies | Generative AI on Vertex AI, https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies 50. Prompt Engineering Techniques✨ | by Anusha | Oct, 2025, https://medium.com/@athatikonda12/prompt-engineering-techniques-ac87b245b542 51. A 3-Step Prompt Template That Is Ready for Copying and Pasting to Any Task - Reddit, https://www.reddit.com/r/ChatGPTPromptGenius/comments/1mo62z1/a_3step_prompt_template_that_is_ready_for_copying/ 52. LangChain Prompt Templates: Complete Guide with Examples - Latenode, https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-prompt-templates-complete-guide-with-examples 53. Prompt Templates - LangChain.js, https://js.langchain.com/docs/concepts/prompt_templates/ 54. Prompt Engineering For storytelling: From Chaos to Characters Building | by Karthikeya Suppa | Medium, https://medium.com/@karthikeyasuppa01/prompt-engineering-for-storytelling-from-chaos-to-characters-building-6550cd35ee7d 55. 9 Ways to Overcome Writer's Block Using Generative AI - Wordtune, https://www.wordtune.com/blog/how-to-overcome-writers-block
