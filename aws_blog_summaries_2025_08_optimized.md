# AWS机器学习博客摘要 - 2025-08 (智能筛选版本)

本文档包含了AWS机器学习博客中2025-08发布的文章摘要。
基于客户信息智能筛选感兴趣的文章，使用AWS Knowledge MCP Server获取内容。

## 1. Enhance Geospatial Analysis and GIS Workflows with Amazon Bedrock Capabilities

**发布日期：** 22 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/enhance-geospatial-analysis-and-gis-workflows-with-amazon-bedrock-capabilities/
**兴趣度评分：** ✓ 感兴趣

# 增强地理空间分析与GIS工作流的Amazon Bedrock功能

随着数据量激增和信息系统日益复杂，组织机构急需能够提供高质量洞察的解决方案。传统的地理信息系统(GIS)处理地理空间数据(如矢量数据、栅格数据和表格数据)的能力有限，尤其在实时决策、深度分析和长期规划方面存在效率瓶颈。

本文介绍了如何利用Amazon Bedrock的大语言模型(LLM)能力来增强地理空间分析和GIS工作流。Amazon Bedrock提供了两种关键方法来实现这一目标：首先是检索增强生成(RAG)技术，它能将城市发展计划、情报报告或政策法规等非结构化文档信息动态注入到模型响应中；其次是工具和代理功能，可以执行坐标距离计算、数据集过滤、获取实时地理数据、可视化信息点等结构化操作。

这些功能解决了传统GIS系统在处理复杂查询、整合非结构化数据和自动化决策流程方面的局限性。通过将Amazon Bedrock与现有GIS系统集成，组织能够简化数据分析与探索，发现新的洞察，并提升决策制定效率，使技术人员、非技术人员和领导层都能从中受益。文章还提供了一个地震分析代理的实例演示，展示了这些技术在实际应用中的价值。

---

## 2. Beyond the basics: A comprehensive foundation model selection framework for generative AI

**发布日期：** 22 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/beyond-the-basics-a-comprehensive-foundation-model-selection-framework-for-generative-ai/
**兴趣度评分：** ✓ 感兴趣

# 《超越基础：全面的生成式AI基础模型选择框架》摘要

当前大多数组织在评估基础模型时仅关注精确度、延迟和成本三个维度，这种简化方法忽略了影响真实世界模型性能的复杂因素。随着基础模型数量增加，企业在为应用选择合适模型时面临更复杂的决策场景。许多早期生成式AI项目仅基于有限的手动测试或声誉而非系统性评估来选择模型，导致资源过度配置、性能不佳、运营成本高和开发后期才发现生产性能问题。

本文介绍了一个专为Amazon Bedrock用户设计的多维评估框架，将理论框架与实践策略相结合。该框架从四个核心维度评估基础模型：任务性能(包括任务特定准确性、少样本学习能力、指令遵循度等)、架构特性(参数数量、训练数据组成、模型架构等)、运营考量(吞吐量和延迟、成本结构、可扩展性等)以及负责任AI属性。

这一全面的评估方法使用Amazon Bedrock Evaluations工具帮助数据科学家和机器学习工程师摆脱简单评估指标的限制，系统性地选择最适合特定应用场景的基础模型，同时满足业务需求和运营约束，最终实现更高效、更经济的生成式AI应用部署。

---

## 3. Accelerate intelligent document processing with generative AI on AWS

**发布日期：** 22 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/accelerate-intelligent-document-processing-with-generative-ai-on-aws/
**兴趣度评分：** ✓ 感兴趣

# 文章摘要：使用AWS上的生成式AI加速智能文档处理

在当今组织中，文档处理是一项关键任务，但估计80-90%的文档数据是非结构化的，难以有效利用。尽管技术不断进步，许多组织仍依赖费时且容易出错的人工数据录入，无法实现业务扩展和快速响应。虽然生成式AI使构建概念验证解决方案变得容易，但从概念验证到生产环境的转变仍面临诸多挑战，如无法处理大量文档、缺乏错误处理机制、扩展成本高等问题。

为解决这些挑战，AWS推出了开源的GenAI IDP Accelerator（生成式AI智能文档处理加速器），这是一个经过验证的解决方案，可帮助各行业客户应对文档处理挑战。该解决方案结合了Amazon Bedrock Data Automation的开箱即用文档处理功能和Amazon Bedrock的先进基础模型，创建了一个灵活、可扩展的文档自动化起点。

这一解决方案已在多个行业展示了显著成效：市场情报公司Competiscan利用它实现了85%的分类和提取准确率，每天处理35,000-45,000个营销活动；文档管理公司Ricoh通过该解决方案每年节省超过1,900人工时，并实现了高准确率的医疗文档处理。GenAI IDP Accelerator采用模块化、无服务器架构，能自动将非结构化文档转换为结构化数据，具备企业级可扩展性、安全性和成本效益，同时设置和维护需求最小化。

---

## 4. Amazon SageMaker HyperPod enhances ML infrastructure with scalability and customizability

**发布日期：** 22 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-hyperpod-enhances-ml-infrastructure-with-scalability-and-customizability/
**兴趣度评分：** ✓ 感兴趣

# Amazon SageMaker HyperPod增强机器学习基础设施的可扩展性和定制性

在大规模基础模型训练和推理过程中，企业面临着构建和维护复杂ML基础设施的挑战，尤其是当需要遵循组织的安全策略和运营标准时。Amazon SageMaker HyperPod正是为解决这一痛点而生，它提供了一个专为优化基础模型训练和推理而构建的基础设施，可将训练时间减少高达40%。

本文介绍了SageMaker HyperPod的两项重要新功能：连续配置和自定义AMI。连续配置功能通过部分配置、滚动更新、并发扩展和持续重试等特性增强了集群的可扩展性，使用户能够在资源持续配置的同时开始工作负载运行。自定义AMI功能则允许用户基于HyperPod公共AMI创建定制映像，预先配置软件堆栈、安全代理和专有依赖项，从而满足组织的特定安全和合规要求，避免复杂的启动后引导过程。

这些功能为大型企业提供了前所未有的灵活性和运营效率，使AI团队能够在面临紧迫期限和资源限制时显著减少等待时间，并能利用立即可用的计算能力开始模型训练和部署，同时系统在后台努力配置剩余请求的资源，加速AI创新进程。

---

## 5. Fine-tune OpenAI GPT-OSS models using Amazon SageMaker HyperPod recipes

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/fine-tune-openai-gpt-oss-models-using-amazon-sagemaker-hyperpod-recipes/
**兴趣度评分：** ✓ 感兴趣

# 微调OpenAI GPT-OSS模型：SageMaker HyperPod配方解决方案

随着大型语言模型的普及，企业对模型定制化的需求日益增长，但设置分布式训练环境复杂且成本高昂。本文介绍了使用Amazon SageMaker HyperPod配方微调OpenAI GPT-OSS模型的解决方案，作为GPT-OSS系列的第二部分。

SageMaker HyperPod配方为用户提供预构建、经过验证的配置，大大简化了微调Meta's Llama、Mistral和DeepSeek等流行开源基础模型的流程。这些配方消除了设置分布式训练环境的复杂性，同时保持企业级性能和可扩展性。

该解决方案支持两种部署方式：通过Amazon EKS协调的HyperPod或直接使用训练作业。文章详细介绍了如何在多语言推理数据集(HuggingFaceH4/Multilingual-Thinking)上微调GPT-OSS模型，使其能够跨多种语言处理结构化、思维链推理。系统使用Amazon FSx for Lustre作为HyperPod的持久文件系统，或Amazon S3用于训练作业，将准备好的数据保存后提交微调任务，最后将训练好的模型部署到SageMaker端点进行测试和评估。

这一解决方案使企业能够在短时间内实现强大的模型定制，无需深入了解分布式训练的技术细节，从而加速AI应用的开发和部署。

---

## 6. Inline code nodes now supported in Amazon Bedrock Flows in public preview

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/inline-code-nodes-now-supported-in-amazon-bedrock-flows-in-public-preview/
**兴趣度评分：** ✓ 感兴趣

# Amazon Bedrock Flows新增内联代码节点功能预览

AWS宣布Amazon Bedrock Flows现已支持内联代码节点功能的公开预览。在此前的开发流程中，开发者必须为简单的逻辑处理创建单独的AWS Lambda函数，增加了开发复杂度和维护成本，限制了生成式AI应用程序的快速迭代和广泛参与。

这项新功能允许开发者直接在工作流中编写Python脚本，简化了预处理和后处理任务，如数据规范化和响应格式化。开发者现在可以在Amazon Bedrock环境内完全设计和部署工作流，无需设置单独的Lambda函数。内联代码节点支持多种应用场景，包括：输入数据转换、模型输出处理、复杂多步骤生成式AI工作流管理，并提供通过Amazon Bedrock API和AWS管理控制台的便捷操作体验。

以Thomson Reuters为例，该公司管理着大量复杂的生成式AI工作流，内联代码功能帮助他们简化流程管理，降低了维护成本，并使数据处理更加灵活，同时让16,000多名用户能够通过自助服务界面构建复杂工作流，不必接触底层基础设施的复杂性。这一功能有效解决了企业级生成式AI应用开发中的关键障碍，加速了迭代周期并促进了更广泛的AI应用构建参与。

---

## 7. Accelerate enterprise AI implementations with Amazon Q Business

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/accelerate-enterprise-ai-implementations-with-amazon-q-business/
**兴趣度评分：** ✓ 感兴趣

# Amazon Q Business助力企业AI实施加速

随着企业探索如何利用生成式AI改善业务流程，提升客户体验并推动创新，选择合适的AI工具成为一个挑战。本文介绍了Amazon Q Business如何帮助企业加速AI实施过程。

企业通常面临的痛点包括数据分散在多个仓库和格式中、员工需要快速准确获取机构知识、严格的安全合规要求、跨部门协作需求以及复杂工作流程等。这些挑战使得选择合适的AI工具变得困难，特别是当需要考虑定制化需求、集成复杂性、未来可扩展性、数据隐私和成本效益等因素时。

Amazon Q Business作为一款AI驱动的助手，能够帮助员工通过自然对话方式快速查找信息、解决问题并完成工作。它的独特优势包括提供统一体验、与AWS架构无缝集成、连接多种企业系统的灵活性、可扩展性、强大的安全合规功能以及按用量付费的成本优势。

文章建议采用分阶段实施方法：从试点案例开始证明价值，如IT帮助台或HR工作流程；评估下一个用例；利用现有数据源；实施准确性测试；迭代扩展成功实施；测量和跟踪结果。同时提供了AWS架构建议，包括IAM身份管理、账户结构、访问渠道、数据源和插件等方面的最佳实践。

通过Amazon Q Business，企业能够在多系统环境中提供一致的AI体验，简化工作流程，提高员工生产力，同时确保数据安全和合规。

---

## 8. Speed up delivery of ML workloads using Code Editor in Amazon SageMaker Unified Studio

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/speed-up-delivery-of-ml-workloads-using-code-editor-in-amazon-sagemaker-unified-studio/
**兴趣度评分：** ✓ 感兴趣

# Amazon SageMaker Unified Studio中Code Editor功能简介

Amazon SageMaker Unified Studio最近推出了Code Editor功能和多空间支持，旨在解决ML团队在开发过程中面临的环境配置复杂、工具分散和资源管理不灵活等痛点。

Code Editor基于Visual Studio Code开源版本(Code-OSS)打造，为数据科学家和开发者提供了熟悉的轻量级IDE环境。该功能集成了多项实用特性：完全托管的基础设施自动处理安全更新；灵活的计算资源调整能力使团队能根据工作负载需求动态改变实例类型；预配置的SageMaker分发镜像包含常用ML框架和SDK；内置Amazon Q Developer提供AI辅助编码功能；支持通过Open VSX访问数千个扩展；具备与GitHub等版本控制系统的集成能力。

同时，多空间支持功能使用户能在同一项目中同时运行多个工作环境，每个空间可使用不同的IDE和计算资源。这解决了数据科学家需要同时进行多个工作流但又需要隔离环境和资源的难题。

这些新功能共同加速了ML工作负载的交付，让开发团队能在统一环境中享受熟悉的IDE体验、强大的开发工具和精确的资源控制，从而提高工作效率和简化ML项目管理。

---

## 9. How Infosys Topaz leverages Amazon Bedrock to transform technical help desk operations

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/how-infosys-topaz-leverages-amazon-bedrock-to-transform-technical-help-desk-operations/
**兴趣度评分：** ✓ 感兴趣

# Infosys Topaz如何利用Amazon Bedrock改革技术帮助台运营

这篇文章探讨了能源供应商面临的技术帮助台运营挑战。当前，现场计量技术人员每月约有20,000次咨询电话，寻求技术支持。支持人员面临信息检索困难、平均处理时间超过5分钟、60-70%问题重复出现等痛点，而扩大人力支持既昂贵又难以扩展。

文章介绍了Infosys Topaz如何利用Amazon Bedrock构建生成式AI应用程序，通过摄取和处理历史通话记录创建知识库，为技术支持提供智能辅助。该解决方案整合了AWS Step Functions、Amazon DynamoDB和Amazon OpenSearch等服务，通过实时处理通话记录，使AI助手能基于历史数据提供解决方案。

这一AI驱动的技术帮助台可提供全天候支持，大幅减少人工搜索时间，缩短通话时长，自动化后台分析操作，同时显著提高技术支持质量。文章还详细介绍了系统实现细节，包括基于用户的访问控制、高效FAQ检索机制、用户指标跟踪以及具有时间追踪功能的响应生成，为企业提供了一种高效且可扩展的技术支持解决方案。

---

## 10. Create personalized products and marketing campaigns using Amazon Nova in Amazon Bedrock

**发布日期：** 20 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/create-personalized-products-and-marketing-campaigns-using-amazon-nova-in-amazon-bedrock/
**兴趣度评分：** ✓ 感兴趣

# Amazon Nova在Amazon Bedrock中实现个性化产品和营销活动

在当今竞争激烈的商业环境中，企业不断寻求通过超个性化和增强客户体验来实现差异化。AWS在2025年戛纳创意节上展示的"香水实验室"(The Fragrance Lab)项目展示了生成式AI如何支持超个性化消费品开发和加速广告创意概念及营销资产的创建。该项目凭借其创新性赢得了国际商业大奖的金奖和银奖。

"香水实验室"是基于Amazon Bedrock中的Amazon Nova构建的端到端应用程序，它通过多种技术实现个性化体验:首先利用Amazon Nova Sonic进行自然语音对话，了解用户个性和偏好;随后通过集成Amazon Nova Pro的自定义RAG系统分析互动并提取关键词,确定最佳香水成分组合;最后使用Amazon Nova Canvas和Nova Reel生成个性化营销创意,包括香水名称、宣传语和图像视频内容。整个过程还应用了Amazon Bedrock Guardrails来确保内容安全。

这一解决方案成功将传统香水定制过程从数小时缩短到几分钟,同时为消费者提供真正个性化的体验。虽然示例聚焦于香水开发和广告活动创建,但其底层架构和方法可应用于从时尚到食品饮料等多个领域,为零售、消费品、广告和营销领域带来变革性的个性化客户体验解决方案。

---

## 11. Tyson Foods elevates customer search experience with an AI-powered conversational assistant

**发布日期：** 20 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/tyson-foods-elevates-customer-search-experience-with-an-ai-powered-conversational-assistant/
**兴趣度评分：** ✓ 感兴趣

# Tyson Foods利用AI助手提升客户搜索体验

Tyson Foodservice作为美国最大的蛋白质供应商之一，通过B2B模式向餐饮服务领域提供产品。然而，公司面临一个显著挑战:他们与超过100万通过分销商购买产品的终端运营商缺乏直接沟通渠道，这限制了他们对客户需求的理解和销售扩展能力。

为解决这一问题，Tyson Foods与AWS生成式AI创新中心合作，在其网站上集成了一个基于Amazon Bedrock的AI对话助手。该解决方案主要由两个关键组件构成:一个增强的语义搜索系统和一个智能对话助手。与传统的关键词搜索相比，新的语义搜索能够理解行业术语之间的概念关联，使餐饮专业人士即使使用与目录描述不完全匹配的语言也能找到所需产品。例如，搜索"拉丝鸡肉"的厨师现在也能找到标记为"碎鸡肉"的相关产品。

该解决方案使用Amazon OpenSearch Serverless实现可扩展的搜索基础设施，并通过Amazon Titan文本嵌入模型和Anthropic's Claude 3.5 Sonnet提供自然语言理解能力。这不仅提升了客户体验，还帮助Tyson Foods建立了与之前无接触运营商的直接沟通渠道，获取更多客户洞察，并实现了销售团队的规模化运营。

---

## 12. Enhance AI agents using predictive ML models with Amazon SageMaker AI and Model Context Protocol (MCP)

**发布日期：** 20 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/enhance-ai-agents-using-predictive-ml-models-with-amazon-sagemaker-ai-and-model-context-protocol-mcp/
**兴趣度评分：** ✓ 感兴趣

# AWS SageMaker AI与MCP协议增强AI代理的预测能力

传统机器学习(ML)模型在销售预测、客户分群和流失预测等领域仍然发挥着不可替代的作用，而生成式AI则在创意任务上表现出色。企业面临的痛点是如何将这两种技术有效结合，既利用传统ML的精确预测能力，又发挥生成式AI的交互优势。

本文介绍了通过Amazon SageMaker AI和Model Context Protocol(MCP)增强AI代理能力的解决方案。该方案允许AI代理直接调用部署在SageMaker上的预测ML模型，使其能够做出数据驱动的业务决策。文章提出了两种集成方式：一是通过Strands Agents SDK直接调用SageMaker端点，二是利用MCP协议实现AI代理与ML模型的标准化交互。

这一方案解决了企业在使用AI系统时难以整合传统ML预测能力的问题。通过将生成式AI的交互能力与传统ML的精确预测结合，企业能够构建更智能、更全面的AI应用。例如，当用户询问"2025年下半年的销售预测是多少?"时，AI代理可以自动调用适当的预测模型并提供准确回答，而不仅仅依赖于生成式AI的推理能力，从而实现对复杂业务场景的更精准支持。

---

## 13. Benchmarking document information localization with Amazon Nova

**发布日期：** 19 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/benchmarking-document-information-localization-with-amazon-nova/
**兴趣度评分：** ✓ 感兴趣

# 《基于Amazon Nova的文档信息定位基准测试》摘要

企业每天需处理成千上万包含关键业务信息的文档，而准确定位和提取特定字段一直是文档处理流程中最复杂的挑战之一。传统方法依赖规则系统和专门的计算机视觉模型，需要大量训练数据、精细模板匹配和持续维护，使扩展性成为重大挑战。

本文介绍了如何利用Amazon Bedrock上的基础模型，特别是Amazon Nova Pro，实现高精度的文档字段定位，同时大幅简化实现过程。与传统方法相比，这些多模态大语言模型(LLM)将先进的视觉理解与自然语言处理能力相结合，提供了突破性优势：无需专业计算机视觉架构，具备零样本能力，通过自然语言界面指定定位任务，并能灵活适应不同文档类型。

文章提出的解决方案采用两种不同的提示策略进行文档字段定位：图像尺寸策略(使用绝对像素坐标)和缩放坐标策略(使用0-1000的标准化坐标系统)。通过FATURA数据集的全面基准测试，该方案证明了其高性能和实用性，为企业提供了一种简化文档处理流程、减少处理错误和人工干预的有效方法。

---

## 14. How Infosys built a generative AI solution to process oil and gas drilling data with Amazon Bedrock

**发布日期：** 19 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/how-infosys-built-a-generative-ai-solution-to-process-oil-and-gas-drilling-data-with-amazon-bedrock/
**兴趣度评分：** ✓ 感兴趣

# Infosys借助Amazon Bedrock构建石油和天然气钻探数据处理的生成式AI解决方案

石油和天然气行业在钻探作业过程中产生大量复杂的技术数据，包括详细的井完工报告、钻井日志和复杂的岩性图表。这些文档包含关键信息，但传统的文档处理方法难以处理多模态数据的特殊性质，如高度技术性术语、复杂的多模态数据格式以及分散在各种文档类型中的相互关联信息。这导致数据提取效率低下、洞察力不足，以及耗时的手动处理过程，阻碍了组织的生产力和决策制定。

针对这一挑战，Infosys利用Infosys Topaz™ AI能力，基于Amazon Bedrock构建了一个先进的检索增强生成(RAG)解决方案。该解决方案专为石油和天然气行业设计，擅长处理多模态数据源，无缝处理文本、图表和数值数据，同时保持不同数据元素之间的上下文和关系。

解决方案核心组件包括：PyMuPDF用于PDF解析，Amazon Bedrock上的Cohere Embed English生成文档内容和用户查询的向量嵌入，Amazon OpenSearch Serverless进行混合搜索，以及Amazon Nova模型进行领域特定的响应生成。该方案采用了层次化的父子分块架构，可保留文档结构和上下文关系，并使用多向量检索机制维护文本和视觉数据之间的上下文。

这一解决方案帮助石油和天然气企业从技术文档中解锁有价值的洞察，简化工作流程，并基于全面的数据分析做出更明智的决策。

---

## 15. Streamline employee training with an intelligent chatbot powered by Amazon Q Business

**发布日期：** 19 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/streamline-employee-training-with-an-intelligent-chatbot-powered-by-amazon-q-business/
**兴趣度评分：** ✓ 感兴趣

# Amazon Q Business 智能聊天机器人简化员工培训

本文介绍了一种利用 Amazon Q Business 构建的智能聊天机器人解决方案，旨在解决企业员工培训过程中的效率和支持问题。传统员工培训面临的主要痛点包括培训资源分散、新员工需要花费大量时间查找信息、培训团队负担重等问题，导致员工培训过程缓慢且资源密集。

文章详细介绍了如何构建一个基于 Amazon Q Business 的智能聊天机器人解决方案，该方案利用检索增强生成(RAG)技术处理员工提问，直接从企业培训材料中提取准确答案。系统不仅能理解并回答员工问题，还可以通过自定义插件将复杂查询直接升级发送到培训支持团队邮箱，实现无缝衔接的支持流程。

该解决方案通过集成 Amazon S3、AWS Lambda、Amazon Cognito 等服务，可以处理多种文档格式，索引多达10万份文档，并通过 CloudFormation 模板实现快速部署。根据案例研究，这种解决方案能将员工获取信息的速度提高10倍，减少高达30%的支持工单，每月为员工节省20-30小时的文档搜索时间，并可自动处理80%的常规问题，使员工培训流程提速50%。这一综合性解决方案有效地减轻了培训团队的压力，同时为新员工提供了更加高效、自助的学习体验。

---

## 16. Create a travel planning agentic workflow with Amazon Nova

**发布日期：** 18 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/create-a-travel-planning-agentic-workflow-with-amazon-nova/
**兴趣度评分：** ✓ 感兴趣

# 创建旅行规划代理工作流：亚马逊Nova让旅行计划更智能

旅行虽然愉快，但旅行规划过程通常复杂繁琐，需要预订住宿、安排活动和当地交通，让人感到不堪重负。虽然旅行专业人士长期以来一直帮助管理这些复杂事务，但生成式AI的突破为我们带来了全新可能——能够理解自然对话、访问实时数据并直接与预订系统和旅行工具对接的智能助手。

本文介绍了如何利用Amazon Nova构建旅行规划解决方案。Amazon Nova作为亚马逊Bedrock平台上的新一代基础模型，在性能与成本之间提供最佳平衡。结合LangGraph编排功能，该解决方案构建了一个实用的旅行助手，能够在保持运营成本可控的同时处理复杂的规划任务。

该解决方案基于无服务器AWS Lambda架构，采用三层方法：前端交互、核心处理和集成服务。核心系统采用图形架构，其中路由节点通过LLM分析用户查询并协调14个行动节点之间的信息流。系统集成了多种数据源和服务，包括Amazon产品广告API、Google自定义搜索API、OpenWeather API、Amazon Bedrock知识库和DynamoDB。整套架构支持简单查询和复杂多步骤交互，可以横向扩展，并且能够通过引入其他行动节点和API集成来添加新功能。

这一旅行规划代理展示了如何利用生成式AI和代理工作流解决现实世界中的复杂问题，为用户提供个性化、便捷的旅行规划体验。

---

## 17. Introducing Amazon Bedrock AgentCore Gateway: Transforming enterprise AI agent tool development

**发布日期：** 15 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/
**兴趣度评分：** ✓ 感兴趣

# Amazon Bedrock AgentCore Gateway：革新企业AI代理工具开发

随着企业扩展AI计划，AI代理需要访问各种工具、数据存储和其他代理，却面临着M×N集成难题：每个代理需要连接多个工具，导致开发复杂度指数级增长。虽然Model Context Protocol (MCP)等协议能解决互操作性问题，但实施这些解决方案需要大量工程努力，包括构建MCP服务器、转换现有API、管理基础架构等。

为解决这一挑战，AWS推出了Amazon Bedrock AgentCore Gateway，这是一项完全托管的服务，彻底改变了企业连接AI代理与工具的方式。Gateway作为集中式工具服务器，提供统一接口，让代理可以发现、访问和调用工具。

AgentCore Gateway的核心功能包括：安全防护（管理OAuth授权）、协议转换（将MCP请求转换为API请求）、组合功能（将多个API整合为单一MCP端点）、目标可扩展性（支持Lambda函数、OpenAPI规范等）、基础设施管理（无需维护底层基础设施）和语义工具选择（解决工具过载问题）。同时，Gateway实现了双边安全架构，处理入站访问和出站连接的认证需求。

通过AgentCore Gateway，企业可以专注于构建智能代理体验，而不必担心与工具和服务的连接问题，大大加速了AI代理开发并降低了维护成本。

---

## 18. Optimizing Salesforce’s model endpoints with Amazon SageMaker AI inference components

**发布日期：** 15 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/optimizing-salesforces-model-endpoints-with-amazon-sagemaker-ai-inference-components/
**兴趣度评分：** ✓ 感兴趣

# Salesforce利用Amazon SageMaker AI推理组件优化模型端点

Salesforce AI平台的模型服务团队面临着在部署大语言模型(LLM)时的资源优化挑战。他们的大型模型(20-30GB)在高性能GPU上运行时存在资源利用不足的问题，而中型模型(约15GB)在处理高流量工作负载时又因过度配置而导致成本增加。这种情况下，GPU资源既未得到充分利用，又产生了不必要的成本支出。

为解决这些问题，Salesforce团队采用了Amazon SageMaker AI的推理组件(inference components)功能，该功能允许在单一SageMaker端点上部署多个基础模型，并能精确控制每个模型的加速器数量和内存分配。通过这种方式，多个模型可以共享相同的GPU实例，同时仍能根据各自的流量模式单独扩展。

推理组件带来的关键优势包括：自动优化模型放置以最大化资源利用率、支持每个模型根据自定义配置独立扩展、动态增减实例以保持可用性同时减少闲置计算资源，以及按需将模型缩减至零副本以释放资源。这种方案既解决了Salesforce的即时部署挑战，又为其不断发展的AI计划创建了灵活的基础，成功地在保持性能的同时优化了基础设施成本和资源效率。

---


## 统计信息

- 总共处理文章数：20
- 客户感兴趣文章数：18
- 筛选效率：90.0%
