# AWS机器学习博客摘要 - 2025年8月

本文档包含了AWS机器学习博客中2025年8月发布的 60 篇文章的摘要。

## 1. Enhance Geospatial Analysis and GIS Workflows with Amazon Bedrock Capabilities

**发布日期：** 22 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/enhance-geospatial-analysis-and-gis-workflows-with-amazon-bedrock-capabilities/

# AWS 地理空间分析和 GIS 工作流利用 Amazon Bedrock 能力增强

随着数据量增长和信息系统复杂性提高，相关机构需要能够提供高质量洞察的解决方案。本文探讨了如何将 Amazon Bedrock 的大语言模型(LLM)能力与现有地理空间信息系统(GIS)整合，创建全新工作流程来释放效率和洞察。

文章介绍了地理空间数据的基本类型(矢量数据、栅格数据和表格数据)，以及如何通过两种主要方法将 Amazon Bedrock 能力融入地理空间分析：一是检索增强生成(RAG)，通过知识库为模型提供上下文信息；二是通过工具和代理控制 GIS 系统执行特定任务，如坐标距离计算、兴趣点查询或数据可视化。

文章展示了一个实际案例：利用 Amazon Bedrock 代理与 Amazon Redshift 构建地震分析助手。该解决方案能够处理包含地震数据和县界多边形的表格，通过自然语言理解用户意图并生成地理空间查询，回答如"哪个县最近发生地震"或"过去20年哪个县地震最多"等问题。这种集成方案极大简化了地理数据分析流程，支持实时决策、深入研究和长期规划，使技术和非技术人员都能更直观地与复杂地理数据交互。

---

## 2. Beyond the basics: A comprehensive foundation model selection framework for generative AI

**发布日期：** 22 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/beyond-the-basics-a-comprehensive-foundation-model-selection-framework-for-generative-ai/

# 超越基础：全面的生成式AI基础模型选择框架

当前大多数组织在评估基础模型时仅关注准确性、延迟和成本三个维度，这种简化无法反映真实世界中模型性能的复杂性。随着基础模型数量激增，企业在选择适合其应用的模型时面临着复杂的决策挑战。

本文提出了一个专为Amazon Bedrock用户设计的系统化评估方法论，结合理论框架和实践策略，帮助数据科学家和机器学习工程师做出最佳模型选择。文章详细阐述了一个四阶段的评估方法：需求工程、候选模型选择、系统性能评估和决策分析。同时提出了基础模型能力矩阵，从四个核心维度评估模型：任务表现、架构特性、运营考量和负责任AI属性。

针对日益流行的智能代理应用，文章还特别增加了代理特定的评估维度，包括规划和推理能力、工具与API集成能力、代理间通信能力等。文章还讨论了A/B测试、对抗性测试、多模型集成评估等高级评估技术，以及不同行业的特殊考量。

这一全面的评估框架帮助企业在性能、成本和运营需求之间取得平衡，确保模型选择不是一次性工作，而是一个随业务需求和技术能力变化而演进的过程。正确的模型选择能避免资源过度配置、性能次优、运营成本过高和生产环境中的后期问题。

---

## 3. Accelerate intelligent document processing with generative AI on AWS

**发布日期：** 22 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/accelerate-intelligent-document-processing-with-generative-ai-on-aws/

# 利用AWS上的生成式AI加速智能文档处理

在当今商业环境中，组织每天需处理海量文档，但约80-90%的文档数据因非结构化而无法有效利用。尽管技术不断进步，许多组织仍依赖手动数据录入，这种方法不仅耗时、易错，更阻碍了业务扩展和快速响应。虽然生成式AI简化了文档处理概念验证，但从原型到生产环境的转化仍面临诸多挑战，如无法应对大规模处理、缺乏错误处理、成本效益低下等问题。

针对这些痛点，AWS推出了开源的GenAI IDP加速器——一个经过验证的智能文档处理解决方案。该方案提供了多种处理模式，包括使用Amazon Bedrock数据自动化功能进行开箱即用的文档处理，以及利用Amazon Bedrock基础模型处理复杂文档的定制逻辑。其核心功能包括：无服务器架构、生成式AI驱动的文档分类与拆分、高级信息提取、多种处理模式选项、少样本学习、置信度评估以及人工介入审核等。

该解决方案已在多家企业中取得显著成效。例如，营销情报公司Competiscan通过此方案实现了85%的分类和提取准确率，每日处理3.5-4.5万个营销活动；文档管理公司Ricoh则在医疗文档处理中每年节省近1900工时，同时提高了处理准确率。GenAI IDP加速器大幅减少了文档处理所需的时间和成本，使企业能够在数天而非数月内构建高效的文档处理工作流程。

---

## 4. Amazon SageMaker HyperPod enhances ML infrastructure with scalability and customizability

**发布日期：** 22 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-hyperpod-enhances-ml-infrastructure-with-scalability-and-customizability/

# Amazon SageMaker HyperPod: 增强机器学习基础设施的可扩展性和自定义能力

随着人工智能向多领域和场景部署的趋势发展，企业在训练大型基础模型时面临基础设施构建和优化的重大挑战。大型企业需要确保GPU集群符合组织政策和安全规则，而关键AI/ML工作负载则要求与组织软件栈和运营标准一致的专业环境。

针对这些痛点，Amazon SageMaker HyperPod提供了专为大规模基础模型训练和推理优化的基础设施。它通过持久性集群和内置弹性功能，减少了多达40%的训练时间，同时允许用户SSH连接到底层EC2实例，实现深度基础设施控制。本文重点介绍了HyperPod的两项新功能：

1. 连续配置功能：增强集群可扩展性，支持部分配置、滚动更新、并发扩展操作和持续重试。这使团队能够立即使用可用计算资源开始模型训练，同时系统在后台继续配置剩余资源，大大缩短等待时间。

2. 自定义AMI功能：允许企业基于HyperPod公共AMI构建自定义镜像，预先安装安全代理、合规工具、专有软件和专业库，从而减少运行时安装延迟，加快集群初始化速度，同时满足企业级安全和合规要求。

这些功能共同解决了大规模ML工作负载的弹性扩展和企业级控制需求，帮助组织在保持安全标准的同时加速AI创新进程。

---

## 5. Fine-tune OpenAI GPT-OSS models using Amazon SageMaker HyperPod recipes

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/fine-tune-openai-gpt-oss-models-using-amazon-sagemaker-hyperpod-recipes/

# 使用SageMaker HyperPod配方微调OpenAI GPT-OSS模型

在大型语言模型(LLM)日益普及的背景下，企业面临的一大痛点是如何高效地微调开源大型模型以满足特定业务需求。传统微调方法通常需要复杂的分布式训练环境配置，技术门槛高，资源需求大。

本文介绍了如何利用Amazon SageMaker HyperPod配方(recipes)来微调OpenAI GPT-OSS模型。这些预先构建和验证的配方可以大幅简化分布式训练环境的设置过程，同时保持企业级的性能和可扩展性。文章详细展示了两种微调GPT-OSS模型的方法：使用SageMaker HyperPod集群(通过Amazon EKS编排)或使用SageMaker训练作业。

这一解决方案专门针对需要为大型语言模型定制化训练的企业用户。通过SageMaker HyperPod配方，用户可以：
1. 在几分钟内开始微调Meta的Llama、Mistral和DeepSeek等流行的开源基础模型
2. 避免复杂的分布式训练环境配置
3. 根据需求灵活选择持久集群(HyperPod)或临时计算资源(训练作业)
4. 实现多语言推理能力的模型微调

文章还提供了完整的代码示例，从数据准备、模型训练到最终部署到SageMaker端点的全流程指导，使AI工程师能够更加高效地定制大型语言模型以满足特定业务场景的需求。

---

## 6. Inline code nodes now supported in Amazon Bedrock Flows in public preview

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/inline-code-nodes-now-supported-in-amazon-bedrock-flows-in-public-preview/

# Amazon Bedrock Flows现已支持内联代码节点功能

AWS今天宣布Amazon Bedrock Flows推出内联代码节点功能公开预览版。此前，开发人员在构建生成式AI应用流程时，即使是简单的数据处理逻辑也需要创建单独的AWS Lambda函数，增加了开发复杂度和维护成本。

这项新功能允许开发者直接在工作流中编写Python脚本，简化了数据预处理和后处理任务。用户可以在不离开Amazon Bedrock环境的情况下完成数据转换、格式化、应用业务规则等操作，无需管理额外的Lambda函数。该功能支持多种常用Python库(如opencv、scipy和pypdf)，并提供完整的可观察性，使用户能够跟踪每个节点的输入和输出。

Thomson Reuters等企业客户已经开始受益于这一功能，简化了工作流管理，降低了运营开销，并使非技术用户也能通过自助服务界面构建复杂工作流。内联代码节点功能通过消除基础架构复杂性，帮助企业加速采用生成式AI解决方案，实现更快的迭代周期和更广泛的AI应用开发参与。

该功能目前在美国东部(弗吉尼亚北部、俄亥俄)、美国西部(俄勒冈)和欧洲(法兰克福)区域公开预览。

---

## 7. Accelerate enterprise AI implementations with Amazon Q Business

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/accelerate-enterprise-ai-implementations-with-amazon-q-business/

# 《使用Amazon Q Business加速企业AI实施》摘要

企业在探索生成式AI应用时，面临从众多工具中选择合适解决方案的挑战，尤其是在数据分散、系统复杂的环境中。选择合适的AI工具需考虑定制需求、集成复杂度、未来扩展性等多个因素。

Amazon Q Business是一款AI驱动的助手，能帮助员工通过自然对话快速找到信息、解决问题并完成工作。它能访问企业内部的各种文档、网站和资源，并可用于自动化跨企业系统的工作流程，同时严格遵守组织现有的权限和访问控制，确保信息安全。

这一服务特别适合数据复杂、知识依赖度高、安全要求严格的组织，提供了统一体验、架构优势、灵活性、可扩展性和成本效益。文章建议企业采用分阶段实施方法：先通过试点案例证明价值；评估后续用例；利用现有数据源；实施准确性测试；迭代扩展成功实施。

多家企业已利用Amazon Q Business改善知识管理、员工入职培训、IT支持、人力资源管理等领域的效率，有案例显示员工每天可节省约两小时的信息检索时间，减少对专家的依赖，加速决策过程。

---

## 8. Speed up delivery of ML workloads using Code Editor in Amazon SageMaker Unified Studio

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/speed-up-delivery-of-ml-workloads-using-code-editor-in-amazon-sagemaker-unified-studio/

# Amazon SageMaker Unified Studio的代码编辑器加速机器学习工作流程

在机器学习开发过程中，数据科学家和开发人员常常需要在不同工具间切换，导致工作效率降低且环境配置复杂。为解决这一痛点，AWS最近在Amazon SageMaker Unified Studio中引入了Code Editor和多空间(multiple spaces)功能。

Code Editor基于Code-OSS(Visual Studio Code开源版)构建，为用户提供了熟悉的IDE布局和快捷键，同时集成了强大的调试功能、代码重构工具和终端访问能力。该编辑器预配置了SageMaker分发版，包含流行的机器学习框架，并支持通过Open VSX扩展库访问数千个兼容扩展。此外，它还整合了由Amazon Q Developer提供的生成式AI功能，可提供内联代码建议和开发辅助。

多空间功能则允许用户在同一项目中创建多个工作环境，每个环境可以运行不同类型的IDE(如Code Editor或JupyterLab)，并配置不同的计算资源。这使团队能够并行处理不同的工作流程，根据需求灵活调整资源，同时保持数据和设置的持久性。

通过这些新功能，AWS帮助机器学习团队加速从开发到部署的全流程，简化环境管理，并提高跨团队协作效率，使数据科学家能更专注于构建和优化模型，而非处理基础设施问题。

---

## 9. How Infosys Topaz leverages Amazon Bedrock to transform technical help desk operations

**发布日期：** 21 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/how-infosys-topaz-leverages-amazon-bedrock-to-transform-technical-help-desk-operations/

# Infosys Topaz如何利用Amazon Bedrock改革技术支持服务台运营

在当今企业环境中，AI驱动的应用和服务已成为关键竞争优势。技术支持服务台面临的主要挑战包括：寻找合适信息解决客户问题耗时长、高达60-70%的重复性问题处理、维持足够的人力成本高昂且缺乏可扩展性。特别是对于能源供应商而言，每月约有20,000通电表技术人员的支持请求需要处理，而高频问题的平均处理时间超过5分钟。

Infosys Topaz与Amazon Bedrock合作开发了一个AI驱动的技术支持服务台解决方案。该系统通过摄取过去的通话记录构建知识库，利用Anthropic的Claude Sonnet模型分析、分类和总结对话内容，将相关信息存储在Amazon OpenSearch Serverless向量数据库中。系统采用高效的RAG(检索增强生成)管道，结合Amazon Titan文本嵌入模型，帮助支持代理迅速检索历史解决方案。

该解决方案的实施显著提升了技术支持效率，包括全天候可用性、缩短等待时间和通话时长、自动化后端操作、提高响应质量。同时，系统通过AWS Secrets Manager、IAM和KMS实现了全面的安全措施，并通过基于角色的访问控制满足不同用户需求。这使技术支持人员能够专注于新问题，同时显著提高客户服务质量和整体运营效率。

---

## 10. Create personalized products and marketing campaigns using Amazon Nova in Amazon Bedrock

**发布日期：** 20 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/create-personalized-products-and-marketing-campaigns-using-amazon-nova-in-amazon-bedrock/

# 创新香水实验室：用Amazon Nova打造个性化产品与营销

在当前市场环境下，企业迫切寻求通过超个性化和增强客户体验来实现差异化。AWS在戛纳创意节上展示的"香水实验室"(The Fragrance Lab)正是解决这一痛点的创新方案，该项目获得了国际商业大奖的金奖和银奖。

这个由Amazon Bedrock中的Amazon Nova驱动的实验室，展示了生成式AI在零售、消费品和营销领域的变革力量。整个体验流程分为两个核心部分：个性化香水配方创建和广告营销素材生成。系统首先通过Amazon Nova Sonic的语音对话模型与用户交流，了解其个性和喜好；然后通过Amazon Nova Pro结合RAG系统分析数据，提取关键词并确定最佳香水成分组合；最后使用Amazon Nova Canvas和Nova Reel生成个性化营销创意，包括香水名称、标语和视觉素材。

这一解决方案将传统上需要数小时的香水师工作缩短至几分钟，同时保持了高度个性化，让现场香水师能够每天定制数百种独特香水。虽然展示以香水为例，但该架构和方法可应用于从时尚到食品饮料等多个行业，为企业提供了一种通过AI打造个性化消费体验的新路径，满足了当代消费者对定制化产品和服务日益增长的需求。

---

## 11. Tyson Foods elevates customer search experience with an AI-powered conversational assistant

**发布日期：** 20 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/tyson-foods-elevates-customer-search-experience-with-an-ai-powered-conversational-assistant/

# Tyson Foods利用AI助手提升客户搜索体验

泰森食品服务部(Tyson Foodservice)作为美国最大蛋白质供应商之一，一直面临着与超过100万未直接服务的餐饮经营者建立联系的挑战。由于其B2B模式主要通过分销商销售产品，公司与终端用户的互动有限，难以获取客户洞察并建立直接沟通渠道。

针对这一痛点，Tyson Foods与AWS生成式AI创新中心合作，开发了一款基于Amazon Bedrock的AI助手，并将其集成到公司网站中。该解决方案主要包括两大核心功能：一是改进的语义搜索系统，利用Amazon Titan文本嵌入模型和OpenSearch Serverless服务，能够理解厨师专业术语的语义关系，即使搜索词与产品目录描述不完全匹配，也能返回相关结果；二是基于Anthropic的Claude 3.5 Sonnet模型打造的交互式AI助手，可提供个性化搜索、详细产品信息、分销商服务、采购协助等功能。

这一AI驱动的解决方案成功解决了传统关键词搜索的局限性，帮助Tyson Foods扩展销售渠道，收集宝贵的客户见解，并与之前未直接服务的餐饮经营者建立联系。同时，该系统通过理解烹饪术语、制备方法和产品应用之间的概念关系，极大地改善了食品服务专业人员的产品发现体验，使他们能够更高效地找到所需的特定食材。

---

## 12. Enhance AI agents using predictive ML models with Amazon SageMaker AI and Model Context Protocol (MCP)

**发布日期：** 20 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/enhance-ai-agents-using-predictive-ml-models-with-amazon-sagemaker-ai-and-model-context-protocol-mcp/

# 机器学习与AI代理的融合：通过Amazon SageMaker AI和MCP增强决策能力

在当今企业环境中，尽管生成式AI备受瞩目，传统机器学习模型在销售预测、客户细分和流失预测等特定预测任务中仍然不可或缺。这篇文章介绍了如何通过Amazon SageMaker AI和模型上下文协议(MCP)将预测性机器学习模型与AI代理无缝集成，使AI代理能够做出更精准的数据驱动型业务决策。

文章展示了一个全面的工作流程，允许AI代理利用部署在SageMaker上的机器学习模型。通过Strands Agents SDK(一个开源SDK，可用几行代码构建和运行AI代理)，开发者可以采用两种集成方式：直接端点访问或通过MCP协议。MCP方法提供了更加安全和可扩展的工具调用逻辑，实现了代理与工具执行的解耦。

这种集成解决了AI代理在做出业务决策时缺乏精准预测能力的问题。例如，当用户询问"2025年下半年的销售预测是什么？"时，系统可以调用训练好的时间序列预测模型(如XGBoost)生成准确预测，而不仅仅依赖生成式AI的能力。这种结合传统机器学习与生成式AI的方法，使组织能够构建更智能、更具成本效益的解决方案，在保持对话能力的同时提供准确的预测分析。

---

## 13. Simplify access control and auditing for Amazon SageMaker Studio using trusted identity propagation

**发布日期：** 19 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/simplify-access-control-and-auditing-for-amazon-sagemaker-studio-using-trusted-identity-propagation/

# AWS SageMaker Studio引入可信身份传播功能简化访问控制与审计

AWS推出了"可信身份传播"功能支持Amazon SageMaker Studio，解决了企业在机器学习环境中面临的身份认证与访问控制复杂性问题。传统上，企业需要为不同用户维护复杂的IAM策略，不仅管理繁琐，还难以追踪和审计数据访问情况。

这项功能允许用户的身份信息安全地跨服务边界传播，实现基于实际用户身份的细粒度访问控制，而非仅依赖IAM角色。通过与IAM Identity Center集成，SageMaker Studio可以简化权限管理，组织可以直接向现有的IAM Identity Center身份授予权限。该功能还支持长时间运行的用户后台会话，使用户可以在后台作业继续运行的同时登出交互式ML应用程序。

这一解决方案使企业能够实现多项关键功能：通过Amazon S3 Access Grants和AWS Lake Formation实现精细的数据访问控制；在AWS CloudTrail中记录详细的用户操作审计日志；支持用户在不同服务间使用统一身份。实际应用场景包括在笔记本中实验S3数据和通过Athena访问Lake Formation等。

对于拥有大量用户且需要管理不同数据源访问权限的企业，可信身份传播显著降低了运营开销，同时加强了安全性和可审计性，从而简化了数据访问管理。

---

## 14. Benchmarking document information localization with Amazon Nova

**发布日期：** 19 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/benchmarking-document-information-localization-with-amazon-nova/

# 文档信息定位的革新：Amazon Nova的性能基准测试

企业每天需要处理大量包含关键业务信息的文档，从发票到合同，准确定位和提取特定字段一直是文档处理流程中最复杂的挑战之一。虽然光学字符识别(OCR)可以识别文本内容，但确定特定信息的具体位置通常需要复杂的计算机视觉解决方案。传统方法需要大量训练数据、复杂模型架构和专业知识来实现和维护。

本文介绍了如何利用Amazon Bedrock中的基础模型，特别是Amazon Nova Pro，来实现高精度的文档字段定位。这些多模态大语言模型(LLMs)将先进的视觉理解与自然语言处理能力相结合，代表了文档处理领域的范式转变。文章提出了两种不同的提示策略：使用绝对像素坐标的图像维度策略和使用标准化0-1000坐标系统的比例坐标策略。

在FATURA数据集的基准测试中，Amazon Nova Pro展现出出色的性能，平均精度(mAP)达到0.8331。它在50个不同模板中的45个上实现了超过0.80的mAP，对结构化字段(如发票号码和日期)表现尤为出色。这种基于多模态LLM的解决方案显著简化了实现，减少了技术开销，提高了对新文档类型的适应性，使组织能够高效处理从发票到表单等各种文档，实现自动化质量检查、敏感数据编辑和智能文档比较等关键业务操作。

---

## 15. How Infosys built a generative AI solution to process oil and gas drilling data with Amazon Bedrock

**发布日期：** 19 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/how-infosys-built-a-generative-ai-solution-to-process-oil-and-gas-drilling-data-with-amazon-bedrock/

# 如何利用Amazon Bedrock处理石油和天然气钻井数据：Infosys的生成式AI解决方案

石油和天然气行业面临着处理大量复杂技术数据的挑战，传统文档处理方法难以有效应对这些包含文本、图表和专业术语的多模态数据。这类文档如钻井报告、钻井日志和岩性图表，往往包含关键决策信息，但由于技术术语复杂、数据格式多样且信息相互关联，常规处理方法效率低下，导致数据提取不完整、洞察不足，最终影响组织生产力和决策。

针对这一痛点，Infosys基于Amazon Bedrock构建了一个先进的RAG（检索增强生成）解决方案，结合Infosys Topaz™ AI技术，专为石油和天然气行业定制。该方案集成了Amazon Bedrock Nova Pro、Knowledge Bases、Amazon OpenSearch Serverless等AWS服务，并使用了层次化父子分块架构、多向量检索机制和混合搜索技术。系统能够同时处理文本和图像数据，保持它们之间的上下文关联，实现高精度检索和智能问答。

通过多种技术方法的探索与优化，最终采用的混合搜索方案实现了不到2秒的查询响应时间，92%的检索准确率，有效解决了石油和天然气行业复杂文档处理的难题。该解决方案帮助企业从技术文档中提取有价值的见解，简化工作流程，并基于全面的数据分析做出更明智的决策。

---

## 16. Streamline employee training with an intelligent chatbot powered by Amazon Q Business

**发布日期：** 19 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/streamline-employee-training-with-an-intelligent-chatbot-powered-by-amazon-q-business/

# 利用Amazon Q Business打造智能培训聊天机器人

本文介绍了一种基于Amazon Q Business的智能培训聊天机器人解决方案。在企业环境中，新员工培训往往面临效率低下、支持人员负担重、知识获取困难等痛点。传统培训方式需要员工手动搜索文档，或直接联系培训团队，这不仅耗时且资源密集。

文章提出的解决方案是一个基于Amazon Q Business的智能培训聊天机器人，它利用检索增强生成(RAG)技术处理用户问题并从已索引的培训材料中提供上下文相关的回答。该方案通过Amazon Cognito实现安全访问控制，可处理多种格式文档(PDF、DOC、DOCX、TXT)，单文档最大支持50MB，每个知识库可索引高达10万文档。当系统无法找到所需信息时，用户可通过自定义插件一键发送邮件联系培训支持团队。

根据AWS案例研究，该解决方案能显著提升培训效率：员工查找答案的速度提高10倍，支持工单减少30%，员工每月在文档搜索和总结任务上节省20-30小时，80%的常规重复问题可自动处理，使员工入职培训流程加速50%。这种智能培训系统不仅减轻了人工培训师的负担，还为员工提供了高效的自助服务体验，实现了企业培训资源的优化配置。

---

## 17. Create a travel planning agentic workflow with Amazon Nova

**发布日期：** 18 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/create-a-travel-planning-agentic-workflow-with-amazon-nova/

# 创建旅行规划智能工作流：Amazon Nova解决方案

旅行计划往往是一个复杂且繁琐的过程，需要预订住宿、规划活动和安排交通，这些决策常让人感到不知所措。虽然传统上可以依靠旅行顾问，但生成式AI的进步为我们提供了全新可能——能理解自然对话、访问实时数据并直接与预订系统交互的智能助手。

该博客介绍了一个基于Amazon Nova构建的旅行规划智能代理解决方案。方案采用无服务器AWS Lambda架构和Docker容器，实现了三层架构：前端交互、核心处理和集成服务。核心层使用LangGraph编排框架创建了一个图形架构，由路由节点和14个行动节点组成。系统灵活利用Amazon Nova Lite和Nova Pro模型，前者处理路由和简单任务，后者处理复杂的多步骤操作。

这个旅行助手能够解决旅行规划的复杂性，整合多种数据源，包括Amazon产品广告API、Google自定义搜索API、OpenWeather API以及Amazon Bedrock知识库。它不仅可以理解用户需求，还能保持对话上下文，提供个性化的旅行建议、天气预报和产品推荐。系统通过DynamoDB维护用户状态，使对话具有连贯性。

这个解决方案展示了如何利用生成式AI创建实用的智能助手，为用户提供无缝的旅行规划体验，同时平衡性能与成本。

---

## 18. Introducing Amazon Bedrock AgentCore Gateway: Transforming enterprise AI agent tool development

**发布日期：** 15 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/

# Amazon Bedrock AgentCore Gateway: 革新企业AI代理工具开发

在企业扩展AI计划时，将多个AI代理连接到各种工具和服务会导致复杂的M×N集成问题，大大减缓开发速度并增加复杂性。虽然有MCP和A2A等协议解决互操作性问题，但企业仍需投入大量工程资源来构建服务器、转换API、管理基础设施和实现安全控制，同时还要随着协议快速演变维护这些集成。

为解决这一挑战，AWS推出了Amazon Bedrock AgentCore Gateway，这是一个全托管服务，作为集中化的工具服务器，为AI代理提供统一接口来发现、访问和调用工具。该服务原生支持MCP协议，同时抽象了安全性、基础设施和协议级复杂性，让企业能专注于构建智能代理体验。

AgentCore Gateway的关键功能包括：将REST API和Lambda函数无代码转换为MCP工具；智能工具发现；内置入站和出站授权；双面安全架构支持多种身份验证方法；以及完全托管的无服务器基础设施。此外，还提供语义工具选择功能，解决代理在大规模工具环境中的"工具过载"问题，有效提高AI代理性能和决策质量。这一服务极大简化了企业AI工具集成，加速了AI应用部署。

---

## 19. Build a scalable containerized web application on AWS using the MERN stack with Amazon Q Developer – Part 1

**发布日期：** 15 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/build-a-scalable-containerized-web-application-on-aws-using-the-mern-stack-with-amazon-q-developer-part-1/

# AWS机器学习博客摘要：使用MERN堆栈和Amazon Q Developer构建可扩展容器化Web应用

随着现代Web应用开发需求不断增长，开发者面临着提高开发效率、确保代码质量和实现可扩展性的挑战。本文介绍了如何利用Amazon Q Developer这一生成式AI编码助手来构建基于MERN(MongoDB, Express, React, Node.js)堆栈的可扩展Web应用。

文章主要展示了Amazon Q Developer如何在软件开发生命周期(SDLC)的各个阶段提供支持，包括：在规划阶段快速提供AWS架构方案、在设计阶段根据详细需求生成应用代码框架、在构建阶段实现工作解决方案、在测试阶段生成单元测试，以及在审查阶段自动检查代码问题。通过Amazon Q Developer，开发者能够大幅提升开发效率，同时确保应用遵循AWS最佳实践。

这一解决方案直接解决了开发者在构建可扩展应用时面临的效率和质量问题：减少了在不同开发阶段的研究时间，简化了代码编写过程，并提供了从本地测试到AWS部署的完整指导。此方案还为开发者提供了坚实基础，可进一步扩展为具有实时视频会议(使用Amazon Chime SDK)和AI聊天机器人(调用Amazon Bedrock基础模型)的功能丰富应用。

---

## 20. Optimizing Salesforce’s model endpoints with Amazon SageMaker AI inference components

**发布日期：** 15 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/optimizing-salesforces-model-endpoints-with-amazon-sagemaker-ai-inference-components/

# Salesforce 利用 Amazon SageMaker AI 推理组件优化模型端点

Salesforce 的 AI 平台模型服务团队面临两大挑战：大型模型(20-30GB)在高性能 GPU 上利用率低下，而中型模型(约15GB)在多 GPU 设置上过度配置导致成本增加。为了解决这些资源优化问题，他们需要一个能够在保持性能的同时提高 GPU 利用率的解决方案。

亚马逊推出的 SageMaker AI 推理组件提供了解决方案，它允许在同一个端点上部署多个基础模型，并为每个模型精确分配加速器和内存资源。通过这项技术，Salesforce 将其专有的 CodeGen 和其他模型整合到同一端点，实现了资源的智能共享和动态扩展。

这种方案带来了显著成效：优化了资源分配，多个模型高效共享 GPU 资源；通过智能 GPU 资源管理和动态扩展，大幅降低了基础设施成本；小型模型现在可以使用高性能 GPU 满足其延迟和吞吐量需求，且不会产生过高成本。Salesforce 最终实现了高达八倍的部署和基础设施成本降低，同时保持了高性能标准，为未来更多 AI 创新奠定了基础。

---

## 21. Building a RAG chat-based assistant on Amazon EKS Auto Mode and NVIDIA NIMs

**发布日期：** 15 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/building-a-rag-chat-based-assistant-on-amazon-eks-auto-mode-and-nvidia-nims/

# 基于AWS EKS Auto Mode和NVIDIA NIMs构建RAG聊天助手

随着企业对能够快速提供准确答案的聊天助手需求增长，基于检索增强生成(RAG)技术的解决方案成为关键。然而，部署这些系统时，企业常面临模型部署复杂性、基础设施管理困难及性能优化挑战。

本文介绍了一个在Amazon EKS Auto Mode上利用NVIDIA NIM微服务构建的RAG聊天助手方案。该方案将EKS的弹性基础设施与NVIDIA NIM的简化模型部署相结合，通过NVIDIA NIM Operator管理模型服务和缓存，同时利用Amazon OpenSearch Serverless进行向量搜索。方案的关键优势在于EKS Auto Mode支持GPU加速镜像，无需手动配置GPU软件组件，同时提供了多种计算选项以平衡性能与成本。

这一方案解决了RAG系统的核心痛点：简化了大型语言模型部署流程，消除了手动选择和配置运行时环境、设置推理服务器及实现模型优化的复杂工作；通过NIM Operator自动化管理模型服务和缓存，显著降低了管理负担；同时提供可扩展架构，既满足稳定需求又能应对波动工作负载。该解决方案为企业构建以自身数据为基础的高效智能聊天助手提供了完整框架。

---

## 22. Introducing Amazon Bedrock AgentCore Identity: Securing agentic AI at scale

**发布日期：** 15 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-identity-securing-agentic-ai-at-scale/

# Amazon Bedrock AgentCore Identity: 大规模保障AI智能代理安全

随着企业将AI代理部署到生产环境中，如何在大规模环境下安全管理身份和访问权限成为关键挑战。应用程序需要对用户进行身份验证以调用AI代理，而这些代理需要访问多种工具和服务、维护审计跟踪并与企业现有身份系统集成，同时避免数据泄露并确保合规。

亚马逊推出的Amazon Bedrock AgentCore Identity是一项专为AI代理设计的全面身份和访问管理服务。通过AgentCore Identity，代理开发者和管理员可以安全访问AWS资源和第三方工具，如GitHub、Salesforce或Slack。该服务提供了强大的身份和访问管理能力，使代理能够代表用户或在获得用户预授权的情况下访问资源或工具，从而减少了开发自定义访问控制和身份基础设施的需求。

AgentCore Identity的主要功能包括：代理身份目录、代理授权器、资源凭证提供程序和资源令牌保险库。它实现了双重认证模型（入站认证和出站认证），并提供了安全的令牌保险库和与SDK的无缝集成。该服务解决了企业AI代理部署中面临的关键安全挑战，包括入站身份验证（谁可以访问代理）、出站身份验证（代理可以访问什么）、企业集成需求以及合规性和可审计性要求。

通过AgentCore Identity，开发者可以避免花费数月时间构建自定义认证系统、实现令牌保险库、管理OAuth流程和创建审计机制，同时尝试维护安全最佳实践。

---

## 23. Scalable intelligent document processing using Amazon Bedrock Data Automation

**发布日期：** 14 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/scalable-intelligent-document-processing-using-amazon-bedrock-data-automation/

# 智能文档处理的新突破：Amazon Bedrock Data Automation

传统文档处理方法通常依赖手动操作，导致效率低下、易出错且成本高昂。特别是在处理各类非结构化文档时，如保险单、医疗记录和政府表格等，企业面临巨大挑战。

本文介绍了Amazon Bedrock Data Automation，这是一项增强智能文档处理(IDP)能力的新服务。与以往使用基础模型的方法相比，此服务带来了显著的改进：首先，它提供置信度分数和边界框数据，增强了数据可解释性；其次，预建蓝图简化了开发过程，加快部署速度；此外，它还支持自动文档分类，无需人工分类文档；最后，它提供了全面的数据规范化、转换和验证功能，确保输出数据的一致性和准确性。

通过一个处理儿童抚养服务表格的实例，文章展示了如何构建无服务器架构，结合AWS Step Functions和Amazon A2I实现高效文档处理。这一解决方案能自动识别文档类型、标准化数据格式(如日期和社保号)、将单行地址转换为结构化字段，并执行自动验证。当处理结果的置信度不足时，系统会启动人工审核流程，确保数据质量。Amazon Bedrock Data Automation的这些特性大大减少了开发时间，提高了数据质量，为各行业创建了更稳健、可扩展的文档处理解决方案。

---

## 24. Whiteboard to cloud in minutes using Amazon Q, Amazon Bedrock Data Automation, and Model Context Protocol

**发布日期：** 14 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/whiteboard-to-cloud-in-minutes-using-amazon-q-amazon-bedrock-data-automation-and-model-context-protocol/

# AWS机器学习新能力：从白板到云端的高效转化

在当今竞争激烈的市场环境中，企业亟需升级陈旧系统以保持竞争力，但传统的现代化转型往往面临耗时的架构评审、复杂的迁移过程和分散的系统整合等挑战。这些延迟不仅影响工程团队效率，还会导致市场机会损失、竞争力下降和运营成本增加。

针对这一痛点，AWS发布了结合Amazon Q Developer、Amazon Bedrock数据自动化(Bedrock Data Automation)和Anthropic的模型上下文协议(MCP)的综合解决方案。这一创新方案实现了从白板草图和团队讨论到完全部署、安全且可扩展的云架构的快速转化，将原本需要数月的工作缩短至几分钟内完成。

该方案的核心是Amazon Bedrock数据自动化MCP服务器，它能实现Amazon Q与企业数据的无缝集成。通过这一技术，系统可以从多模态内容(如会议记录和架构图)中提取信息，自动生成AWS CloudFormation模板并直接部署到AWS云端。MCP作为开放标准促进了AI模型与数据源之间的安全双向连接，而Bedrock数据自动化则提供了强大的ETL工具套件，能自动处理非结构化数据并将其转化为AI工作流可用的形式。这种深度集成确保AI模型能基于干净、经过验证的、富有上下文的信息提供更准确、相关和可靠的输出，从而使企业能够快速将创意转化为现实，大幅提升开发效率和业务敏捷性。

---

## 25. Bringing agentic Retrieval Augmented Generation to Amazon Q Business

**发布日期：** 14 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/bringing-agentic-retrieval-augmented-generation-to-amazon-q-business/

# Amazon Q Business引入智能代理型检索增强生成技术

企业环境下，员工经常需要处理复杂查询，如比较不同福利计划或跨季度项目成果分析，这些问题需要从多个数据源合成信息。传统的检索增强生成(RAG)系统采用单一检索方式，往往难以应对这类复杂查询，导致回答不完整或无法适时调整检索策略。

Amazon Q Business现已引入代理型检索增强生成(Agentic RAG)功能，这是一种能智能规划和执行复杂检索策略的新范式。该功能带来四项核心能力：查询分解与透明响应事件、智能检索工具使用、增强对话能力以及响应优化。系统能够将复杂问题分解为可管理的组件，实时展示处理步骤，同时能够智能部署多种数据探索工具，如表格搜索和长上下文检索。

Agentic RAG还能在多轮对话中保持上下文连贯，处理模糊查询时主动提出澄清问题，并能动态评估和优化响应。用户只需在Amazon Q Business网页界面开启"高级搜索"开关，即可体验这些功能，特别适合解决跨部门政策分析、历史趋势分析等复杂业务场景，让组织能够在保持数据安全与合规的前提下，更充分地利用企业数据资产。

---

## 26. Empowering students with disabilities: University Startups’ generative AI solution for personalized student pathways

**发布日期：** 14 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/empowering-students-with-disabilities-university-startups-generative-ai-solution-for-personalized-student-pathways/

# 为特殊教育学生创造个性化未来规划的生成式AI解决方案

美国有超过750万特殊教育需求学生，他们在高中毕业后往往不清楚自己的教育和职业方向。联邦法律要求每位特殊需求学生在16岁前必须拥有个性化过渡计划(IEP)，详细说明其未来教育和职业目标。然而，资源不足的学区常常缺乏足够的教师和顾问为每位学生创建有效的过渡计划，这不仅影响学生发展，还可能导致学校面临法律和财务后果。

针对这一挑战，University Startups开发了"Trinity"，一个基于Amazon Bedrock的AI助手，帮助特殊教育学生发现兴趣并创建个性化过渡计划。该解决方案利用Amazon Bedrock Agents协调工作流程，通过Lambda函数安全调用外部API获取最新的就业和大学信息，同时使用Amazon Bedrock Flows自动生成个性化文档。系统还集成了Amazon Bedrock Knowledge Bases提供背景知识，并通过Amazon Bedrock Guardrails确保学生信息安全和内容适当性。

试点测试表明，该工具将教育者准备过渡计划的时间缩短至约10分钟，同时让学生能够探索更多个性化发展路径。这一解决方案不仅提高了特殊教育的服务质量和效率，还赋予了资源不足地区的学生同等获得个性化教育规划的机会，展示了生成式AI在教育领域的积极应用潜力。

---

## 27. Deploy LLMs on Amazon EKS using vLLM Deep Learning Containers

**发布日期：** 14 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/deploy-llms-on-amazon-eks-using-vllm-deep-learning-containers/

# AWS基于vLLM深度学习容器在EKS上部署大型语言模型的解决方案

在大规模高效部署大型语言模型(LLMs)时，组织面临着GPU资源优化、网络基础设施管理和模型权重访问效率等重大挑战。尤其在运行分布式推理工作负载时，跨节点协调模型操作的复杂性更为突出。

AWS推出的vLLM深度学习容器(DLCs)是针对这些挑战的解决方案。这些预配置、预测试的容器环境为客户在Amazon EC2、ECS和EKS上部署vLLM提供了优化支持，且无需额外费用。这些容器包含运行vLLM所需的所有依赖项，如驱动程序和库，并内置对Elastic Fabric Adapter(EFA)的支持，以实现高性能多节点推理工作负载。

文章详细介绍了如何利用AWS DLCs在Amazon EKS上部署DeepSeek-R1-Distill-Qwen-32B模型的完整流程，包括创建EKS集群、配置支持EFA的节点组、设置FSx for Lustre文件系统存储模型权重等步骤。这一架构结合了EKS集群、GPU支持的EC2实例、EFA网络和高性能存储，提供了可扩展、高性能的LLM推理解决方案，同时保持了性能和成本效益的平衡，使组织能够专注于从数据中获取AI驱动的洞察，而非基础设施管理的复杂性。

---

## 28. Citations with Amazon Nova understanding models

**发布日期：** 14 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/citations-with-amazon-nova-understanding-models/

# 从信任到可验证：Amazon Nova理解模型的引用功能

大型语言模型(LLM)的广泛应用带来了一个显著的信任问题：这些模型常常"幻觉"，以令人信服的口吻提供错误信息。这使得用户难以验证AI生成内容的准确性，特别是在研究、医疗和教育等领域。

针对这一痛点，AWS推出了Amazon Nova理解模型的引用功能。这一功能允许模型在回答问题时引用可靠的信息来源，提供内容的出处证明。通过简单但精心设计的提示，Nova模型（如Nova Pro）能够在回答用户问题的同时，明确标注信息来源于哪些具体材料和文本片段。

这项功能旨在解决LLM可信度的关键问题，通过引用机制显著增强了AI生成内容的可验证性、透明度和可靠性。它使用户能够追踪信息来源，减少错误信息的传播风险，同时确保了知识产权的正确归属。AWS还提供了基于Amazon Bedrock的评估工具，可以大规模验证引用的准确性，进一步提升模型输出的质量。这种结合了引用功能与评估机制的方案，为企业级AI应用提供了更可靠的信息处理解决方案。

---

## 29. Securely launch and scale your agents and tools on Amazon Bedrock AgentCore Runtime

**发布日期：** 13 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/

# Amazon Bedrock AgentCore Runtime：安全部署和扩展AI代理的解决方案

企业对AI代理充满期待，但许多组织陷入"概念验证困境"，难以将原型转化为生产环境。开发团队面临多种挑战：需要使用不同框架和模型、AI代理的随机特性增加安全复杂性、身份和访问控制困难、需处理多种输入类型和大型负载、难以预测计算资源需求以及基础设施管理分散注意力。

Amazon Bedrock AgentCore Runtime专为AI代理和工具设计，提供安全的无服务器托管环境。这项服务具有多项优势：允许使用不同代理框架和模型(如LangGraph、CrewAI或Strands)；仅需四行代码即可部署、扩展和流式传输代理响应；通过会话隔离和嵌入式身份保障安全执行；支持使用AgentCore Memory的状态持久性；处理不同模态的大型负载；运行异步长时间代理；并且只为使用的资源付费。

AgentCore Runtime使用微型虚拟机完全隔离确保安全性，每个会话获得专用的虚拟机，保证代理状态、工具操作和凭证访问完全隔离。其嵌入式身份系统无缝集成认证和授权，支持IAM SigV4和基于OAuth的JWT Bearer令牌认证，解决了多租户环境中的身份和访问管理挑战。这一解决方案有效消除了将AI代理从实验阶段推向企业级部署的基础设施复杂性障碍。

---

## 30. PwC and AWS Build Responsible AI with Automated Reasoning on Amazon Bedrock

**发布日期：** 13 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/pwc-and-aws-build-responsible-ai-with-automated-reasoning-on-amazon-bedrock/

# PwC与AWS构建基于Amazon Bedrock的负责任AI解决方案

在当今组织部署生成式AI解决方案的过程中，准确性、安全性和合规性的平衡成为关键挑战。特别是在受监管行业中，AI输出结果的数学验证能力可以将创新速度从潜在风险转变为竞争优势。

文章介绍了AWS与PwC合作开发的新型推理检查功能，该功能将PwC深厚的行业专业知识与Amazon Bedrock Guardrails中的自动推理检查相结合。自动推理检查是2025年8月6日发布的Amazon Bedrock Guardrails新功能，它通过形式逻辑验证大语言模型输出的可能性，能够在定义的参数范围内维持准确性，这与传统的概率推理方法不同。

该解决方案主要应用于三个领域：金融服务风险管理中的欧盟AI法案合规、制药内容审查和公用事业停电管理的实时决策支持。在金融领域，它能自动将AI用例分类为风险类别；在制药领域，它作为营销内容生成过程中的次级验证层，加强了合规标准；在公用事业领域，它根据监管指南生成标准化协议，提高响应时间和运营效率。

这种整合为组织提供了在不妥协准确性、安全性和合规性的前提下进行创新的途径，通过数学确定性和可验证的信任来增强AI应用程序的可信度。

---

## 31. How Amazon scaled Rufus by building multi-node inference using AWS Trainium chips and vLLM

**发布日期：** 13 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/how-amazon-scaled-rufus-by-building-multi-node-inference-using-aws-trainium-chips-and-vllm/

# 如何亚马逊使用AWS Trainium芯片和vLLM构建多节点推理来扩展Rufus

亚马逊的Rufus是一个服务于数百万客户的AI购物助手，基于自定义大语言模型(LLM)构建。随着模型复杂度增加，单一芯片或实例无法提供足够内存支持，团队面临着如何在保持高质量交互的同时实现低延迟和成本效益的挑战。

文章详细介绍了亚马逊如何利用Amazon Trainium和开源库vLLM开发多节点推理解决方案。该方案采用领导/跟随节点架构，其中领导节点负责请求调度、批处理和编排，而跟随节点执行分布式模型计算。团队通过AWS Neuron SDK支持的混合并行策略(张量并行和数据并行)在多个实例和加速器之间拆分模型，并利用网络拓扑感知节点放置技术结合弹性结构适配器(EFA)实现低延迟、高带宽的跨节点通信。

此外，团队在Amazon ECS上构建了多节点推理单元抽象层，支持将多个节点部署和扩展为单一单元，提供强大可靠的大规模生产部署。通过这一解决方案，亚马逊成功在数万个AWS Trainium芯片上部署了更大的模型，支持了Prime Day的高流量，显著提升了用户体验和参与度，实现了高可用、高吞吐量的多节点LLM推理系统。

---

## 32. Build an intelligent financial analysis agent with LangGraph and Strands Agents

**发布日期：** 13 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/build-an-intelligent-financial-analysis-agent-with-langgraph-and-strands-agents/

# 《构建智能金融分析代理》摘要

金融分析工作流程对生成式AI提出了独特的技术挑战，传统大语言模型实现难以应对金融领域的复杂性，如动态适应性分析流程和多源数据集成需求。同时，金融机构在采用AI技术时还需平衡创新与监管合规。

本文介绍了一种结合三项核心技术的智能金融分析代理架构：LangGraph负责工作流程编排，支持灵活执行路径同时维持分析连贯性；Strands Agents作为中间层，协调基础模型与专业工具执行复杂分析任务；Model Context Protocol (MCP)标准化各种数据源和工具的集成，简化多系统连接复杂性。

这一组合架构充分发挥各技术优势：LangGraph处理宏观层面的结构化工作流，Strands Agents管理工具交互的细粒度决策，MCP则提供模块化系统框架减少集成复杂度。通过将复杂问题分解为离散步骤，系统能灵活处理从公司财务比较到投资文档生成等多样化任务，同时保持金融分析所需的精确性和上下文连贯性，为金融分析师提供强大支持。

---

## 33. Amazon Bedrock AgentCore Memory: Building context-aware agents

**发布日期：** 13 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/

# Amazon Bedrock AgentCore Memory: 构建具有上下文感知能力的AI代理

在AI助手交互过程中，一个关键痛点是AI无法记住之前的对话内容，导致用户体验割裂。传统的大语言模型本质上是无状态的，无法在不同交互间保留信息，这迫使开发者为每个应用程序重复构建自定义记忆系统，以追踪对话历史、记住用户偏好并维持跨会话的上下文。

AWS在纽约峰会上推出的Amazon Bedrock AgentCore Memory服务正是针对这一挑战设计的。该服务让开发者无需管理复杂的记忆基础设施，就能轻松构建具有上下文感知能力的AI代理。AgentCore Memory提供了强大的短期工作记忆(捕捉会话内即时对话上下文)和长期智能记忆(跨会话存储持久洞察和偏好)功能，使AI代理能够保持上下文连贯性，从交互中学习，并提供真正个性化的体验。

与传统的自建记忆解决方案相比，AgentCore Memory作为完全托管服务，集成了存储、智能提取和高效检索功能，消除了开发者手动编排多个组件(原始对话存储、向量数据库、会话缓存系统和自定义检索逻辑)的复杂性。它通过分层命名空间提供结构化记忆组织和细粒度访问控制，同时保证数据安全性和性能。这使得AI代理能够将一次性对话转变为用户与AI之间持续演进的关系，避免重复询问相同信息或忘记关键偏好的情况发生。

---

## 34. Build a conversational natural language interface for Amazon Athena queries using Amazon Nova

**发布日期：** 13 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/build-a-conversational-natural-language-interface-for-amazon-athena-queries-using-amazon-nova/

# 自然语言交互助力 Amazon Athena 数据查询

本文探讨了如何利用 Amazon Nova 为 Amazon Athena 构建对话式自然语言界面的解决方案。对于不熟悉 SQL 的业务用户来说，数据分析一直是一项重大挑战。传统方法需要技术专业知识来查询数据库，导致见解延迟和对数据团队的依赖。

Amazon Bedrock Agents 结合 Amazon Nova Lite 基础模型的解决方案，能够将用户的自然语言问题转换为精确的 Athena SQL 查询。这一创新架构允许用户通过日常语言与数据交互，自动生成并执行适当的 SQL 查询，从而使数据访问民主化，同时保留了 Athena 强大的分析能力。

该解决方案的核心组件包括：通过 Amazon Cognito 进行安全用户认证、AWS Amplify 托管的前端应用程序、实时查询处理和结果可视化、自然语言到 SQL 查询的转换，以及上下文感知的对话管理。技术架构整合了多个 AWS 服务，包括两个关键的 Lambda 函数行动组：提供时间上下文的时钟和日历行动组，以及处理查询执行的 Athena 查询构建和运行行动组。

该解决方案特别适用于 AWS 成本和使用情况报告(AWS CUR)查询，但也可适应其他通过 Athena 查询的数据库，帮助组织在保持数据分析能力的同时，简化了非技术用户获取数据洞察的过程。

---

## 35. Train and deploy AI models at trillion-parameter scale with Amazon SageMaker HyperPod support for P6e-GB200 UltraServers

**发布日期：** 12 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/train-and-deploy-ai-models-at-trillion-parameter-scale-with-amazon-sagemaker-hyperpod-support-for-p6e-gb200-ultraservers/

# Amazon SageMaker HyperPod支持P6e-GB200 UltraServers，实现万亿参数AI模型的训练与部署

随着人工智能模型规模日益扩大，训练和部署万亿参数级AI模型面临着巨大的计算资源需求和基础设施挑战。针对这一痛点，Amazon SageMaker HyperPod现已推出支持P6e-GB200 UltraServers的功能，为AI创新提供前所未有的计算能力。

这些由NVIDIA GB200 NVL72加速的UltraServers每个系统集成了多达72个NVIDIA Blackwell GPU，提供360 petaflops的FP8计算能力和1.4 exaflops的FP4稀疏计算能力。UltraServers有两种规格：ml.u-p6e-gb200x36（包含36个Blackwell GPU）和ml.u-p6e-gb200x72（包含72个Blackwell GPU），所有GPU通过NVLink互联构成单一网络域，实现高达130 TBps的低延迟带宽。

SageMaker HyperPod与P6e-GB200 UltraServers的结合解决了三个关键问题：首先，它支持训练规模前所未有的万亿参数模型；其次，它将大型LLM推理速度提高了30倍，实现实时性能；最后，通过拓扑感知调度和弹性训练计划，不同团队可以在共享基础设施上同时运行多样化工作负载，提高资源利用率并降低成本。这一强大组合为企业提供了自动化、弹性和高度可扩展的机器学习基础设施，使AI模型开发和部署变得更快、更稳定、更经济高效。

---

## 36. How Indegene’s AI-powered social intelligence for life sciences turns social media conversations into insights

**发布日期：** 12 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/how-indegenes-ai-powered-social-intelligence-for-life-sciences-turns-social-media-conversations-into-insights/

Indegene的AI驱动社交智能为生命科学行业转化社交媒体对话为洞察

在当今数字化世界，医疗对话越来越多地发生在线上。Indegene的研究显示，52%的医疗专业人士(HCP)现在更倾向于通过社交媒体接收医疗和推广内容，比2020年的41%有显著增长。然而，制药公司在分析和解读复杂的医疗讨论方面面临巨大挑战，难以跟上这一转变。

为解决这一痛点，Indegene开发了基于AWS技术的社交智能解决方案，利用Amazon Bedrock、Amazon SageMaker等服务，帮助制药公司从数字医疗对话中提取有价值的情报。该解决方案结合了机器学习、自然语言处理和生成式AI能力，具有广泛的社交媒体整合、医疗专业分析、精准HCP识别和全面洞察能力等特点。

这一解决方案可以帮助生命科学公司监控品牌声誉、评估产品发布反应、识别关键决策者以及获取竞争情报。它采用模块化、可扩展的架构，包括数据获取、数据管理、核心AI/ML服务和面向客户的分析层，将非结构化社交数据转化为可操作的医疗洞察，同时确保监管合规。这一专为医疗设计的系统能够准确解析医疗术语和专业背景，帮助制药公司有效弥合数字化参与差距。

---

## 37. Unlocking enhanced legal document review with Lexbe and Amazon Bedrock

**发布日期：** 12 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/unlocking-enhanced-legal-document-review-with-lexbe-and-amazon-bedrock/

# Lexbe与Amazon Bedrock合作改革法律文档审查流程

法律专业人士经常需要筛选大量文档以寻找关键证据，这一过程不仅耗时，而且容易出错，特别是在面临紧迫截止日期时成本高昂。法律文档审查软件领导者Lexbe通过整合Amazon Bedrock的先进人工智能服务，成功应对了这些挑战。

文章介绍了Lexbe如何将Amazon Bedrock知识库集成到其eDiscovery平台中，推出名为"Lexbe Pilot"的AI驱动问答助手。该解决方案允许法律团队即时查询和提取整个案例文档中的见解，无需耗时的手动研究和分析。使用Amazon Bedrock知识库，用户可以查询整个数据集并获取有依据、与上下文相关的结果，远超传统关键词搜索的功能，帮助法律团队识别可能被忽视的关键文档。

这一解决方案解决了法律专业人士在面对10万至100多万份案例文档时的困境。通过Amazon Bedrock、Amazon OpenSearch和AWS Fargate等服务的整合，Lexbe实现了文档检索的高精确度和处理速度的显著提升。系统经过多次迭代改进，检索率从最初的5%提升至90%，现在能够生成全面的人性化报告，进行深度自动推理，甚至处理多语言数据。这使法律团队能够快速生成可操作的报告，简化电子证据开示流程，并迅速获取战略洞察，从而提高工作效率并降低成本。

---

## 38. Automate AIOps with SageMaker Unified Studio Projects, Part 2: Technical implementation

**发布日期：** 12 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/automate-aiops-with-sagemaker-unified-studio-projects-part-2-technical-implementation/

# AWS SageMaker Unified Studio项目实现AIOps自动化的技术实践

本文是关于使用Amazon SageMaker Unified Studio项目实现企业级AIOps的技术实施指南。企业在实施AI/ML解决方案时面临基础设施管理与数据科学研发之间的协调难题，特别是在确保安全性、可重复性和合规性的同时，还需提高模型开发和部署效率。

文章详细介绍了一个完整的技术实现方案，该方案围绕三个核心角色展开：管理员、数据科学家和ML工程师。管理员负责建立基础设施和治理框架，数据科学家专注于模型开发而无需关注底层基础设施，ML工程师则负责执行和监控部署流程。方案通过三个阶段实现端到端自动化：项目初始化阶段建立基础设施和仓库；开发阶段使用SageMaker工具构建和训练模型；部署阶段通过事件驱动自动将模型投入生产。

这套解决方案有效解决了企业AI/ML开发中的几个关键问题：通过自动化工作流减少了手动干预；通过标准化模板确保了模型开发的一致性和治理；通过CI/CD管道实现了从开发到部署的无缝过渡；同时内置了安全和合规机制，满足企业级治理需求。最终，该方案在保持强大治理控制的同时，实现了开发效率的提升和协作的增强。

---

## 39. Automate AIOps with Amazon SageMaker Unified Studio projects, Part 1: Solution architecture

**发布日期：** 12 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/automate-aiops-with-amazon-sagemaker-unified-studio-projects-part-1-solution-architecture/

# Amazon SageMaker Unified Studio实现AIOps自动化解决方案

随着组织采用Amazon SageMaker Unified Studio来统一数据、分析和AI工作流程，他们面临着扩展、自动化、隔离、多租户和持续集成与交付(CI/CD)方面的新挑战。在团队和账户之间扩展AI计划会带来运营开销，而在统一环境中实现工作流程自动化和嵌入CI/CD实践也很困难，尤其是在需要平衡协作与严格资源边界的情况下。

本文介绍了一个可扩展的框架和架构策略，帮助组织使用SageMaker Unified Studio有效管理多租户环境、实现一致自动化并嵌入治理控制。该解决方案基于多账户AWS架构，包括AI共享服务账户、企业业务线账户和治理账户，涵盖了从项目创建到开发、测试和生产部署的端到端ML操作流程。

文章详细描述了如何通过项目模板化、集成的CI/CD、数据治理、ML管道自动化、模型提升和审批工作流等共享服务来简化AI/ML运营。该框架支持数据科学家、AI/ML工程师、管理员和治理官员等不同角色的协作，确保在扩展AI计划的同时保持安全性、资源隔离和可扩展性。通过这种方法，组织可以实现SageMaker Unified Studio项目从开发到生产的顺畅过渡，同时遵循架构良好的最佳实践。

---

## 40. Demystifying Amazon Bedrock Pricing for a Chatbot Assistant

**发布日期：** 11 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/demystifying-amazon-bedrock-pricing-for-a-chatbot-assistant/

# Amazon Bedrock聊天机器人定价解析

对于探索AI解决方案的企业来说，"在Amazon Bedrock上运行聊天机器人将花费多少?"是一个常见问题。本文通过一个客户服务聊天机器人的实例，详细解析了Amazon Bedrock的定价结构。

文章指出，AI应用成本计算往往复杂，涉及tokens、嵌入向量和各种定价模型，这给项目规划和预算带来挑战。作为解决方案，Amazon Bedrock提供了全面托管服务，集成了多家领先AI公司的基础模型，并通过单一API提供安全、隐私保护的生成式AI应用能力。

文章详细分析了聊天机器人成本的关键组成部分，包括:
- 数据源和知识库处理
- 检索增强生成(RAG)技术
- Tokens消耗计算
- 嵌入向量处理
- 大型语言模型(LLM)调用

通过一个中型呼叫中心实施案例，文章展示了如何估算容量需求并计算总拥有成本，对比了不同基础模型(如Claude、Amazon Nova、Meta Llama)的价格差异，帮助读者了解影响成本的关键因素，从而为自己的项目选择最具成本效益的配置方案。

---

## 41. Fine-tune OpenAI GPT-OSS models on Amazon SageMaker AI using Hugging Face libraries

**发布日期：** 11 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/fine-tune-openai-gpt-oss-models-on-amazon-sagemaker-ai-using-hugging-face-libraries/

# OpenAI GPT-OSS模型在Amazon SageMaker AI上的微调应用

随着全球企业对多语言推理能力的需求增加，开发专业领域内高性能AI解决方案面临挑战。OpenAI于2025年8月5日发布的GPT-OSS模型（gpt-oss-20b和gpt-oss-120b）现已通过Amazon SageMaker AI和Amazon Bedrock在AWS上提供，为解决这一问题提供了强大工具。

这些基于混合专家(MoE)架构的预训练模型每次只激活一部分参数，在保持高推理性能的同时降低了计算成本。它们专长于编码、科学分析和数学推理，支持128,000个token的上下文长度，并具备可调整的推理级别、链式思考(CoT)推理和结构化输出功能，非常适合构建智能代理工作流。

文章详细介绍了如何利用Hugging Face TRL库在SageMaker AI上微调这些模型。该方案结合了Hugging Face Accelerate库实现跨多GPU和多节点的分布式训练，并采用DeepSpeed ZeRO-3优化技术降低内存使用。通过MXFP4量化和LoRA等参数高效微调方法，即使在有限硬件资源下也能有效微调大型模型。

这个解决方案允许企业将通用GPT-OSS模型转变为特定领域的专家，而无需从头训练，大幅提升了多语言推理场景下的准确性和可靠性，减少了幻觉生成，同时保留了开放权重模型在安全企业级部署中的灵活性和可扩展性优势。

---

## 42. The DIVA logistics agent, powered by Amazon Bedrock

**发布日期：** 07 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/the-diva-logistics-agent-powered-by-amazon-bedrock/

# DIVA 2.0：Amazon Bedrock 驱动的智能物流助手

DTDC 作为印度领先的快递物流提供商，每月处理超过 40 万个客户查询，包括包裹追踪、服务可用性检查和运费查询。其原有的物流助手 DIVA 采用刚性引导式工作流，迫使用户按照结构化路径操作而非自然对话，导致客户支持团队负担增加、解决时间延长和客户体验下降。

为解决这些问题，DTDC 与 AWS 合作伙伴 ShellKode 利用 Amazon Bedrock 开发了 DIVA 2.0，这是一个基于生成式 AI 的智能物流代理。该解决方案集成了 Amazon Bedrock Agents、Knowledge Bases 和 API 集成层，通过自然语言处理和多步推理能力提供流畅的会话体验。系统直接连接到 DTDC 的多个后端 API，可实时提供追踪信息、价格计算和服务可用性等数据。

部署 DIVA 2.0 后，DTDC 取得了显著成果：助手能以 93% 的准确率理解并响应自然语言查询；客户支持团队处理的查询数量减少了 51.4%，使团队能够专注于更复杂的问题；系统还提供实时分析和仪表板，帮助持续优化服务能力。通过这一转型，DTDC 成功将传统聊天机器人升级为智能物流助手，大幅提升了客户体验和运营效率。

---

## 43. Automate enterprise workflows by integrating Salesforce Agentforce with Amazon Bedrock Agents

**发布日期：** 07 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/automate-enterprise-workflows-by-integrating-salesforce-agentforce-with-amazon-bedrock-agents/

# 跨系统AI代理协作：Salesforce Agentforce与Amazon Bedrock Agents的集成

随着企业运营环境日益复杂化，业务流程往往跨越多个系统，单一AI代理难以有效处理涉及多系统的数据获取、分析和决策执行等复杂任务。这种环境下，企业亟需一个能够协调多系统协作的智能解决方案。

本文介绍了Salesforce Agentforce与Amazon Bedrock Agents及Amazon Redshift的集成方案，实现企业工作流程自动化。该方案允许Salesforce作为主要协调器，在处理客户导向工作流程时，能够通过自定义操作将专业任务委派给Amazon Bedrock Agents，并协调跨系统访问外部数据和服务。

在实例中，Coral Cloud公司利用此集成处理智能空调和温度传感器数据。Agentforce代理通过Agent Wrapper API调用Amazon Bedrock代理，后者查询配置的知识库以获取Redshift数据库中的传感器数据。系统能够检测异常读数，并触发创建案例的操作。整个流程实现了从数据获取、分析到行动执行的自动化处理，无需人工干预。

这种集成充分发挥了Salesforce在企业数据管理和AWS在AI服务方面的各自优势，使组织能够构建更智能、更全面的AI工作流程，实现更好的业务成果，同时保持数据安全和治理能力。

---

## 44. How Amazon Bedrock powers next-generation account planning at AWS

**发布日期：** 07 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/how-amazon-bedrock-powers-next-generation-account-planning-at-aws/

# AWS 账户规划的下一代解决方案：Amazon Bedrock 驱动的 Account Plan Pulse

随着 AWS 业务规模扩大，销售团队的账户规划流程变得越来越复杂，面临三大挑战：计划质量和格式不一致、审核过程耗时耗力、知识孤岛阻碍团队协作。这些问题导致了大量运营开销，影响了客户服务质量。

为解决这些挑战，AWS 于2025年1月推出了 Account Plan Pulse——一款基于 Amazon Bedrock 构建的生成式 AI 工具。该解决方案通过自动化分析账户计划文档，提供标准化评估和可操作性见解，简化了整个账户规划流程。其核心功能包括对账户计划进行10个业务关键类别的评估，以及从文档中提取和综合客户战略重点与市场趋势。

实施 Pulse 后，AWS 在账户计划质量上取得了37%的同比提升，同时将计划完成、审核和批准的总时间减少了52%。该系统采用批处理流水线从 CRM 系统提取数据，使用 Amazon Bedrock 进行分析，并通过统计框架确保评估可靠性。通过减少审核时间并提供可操作的摘要，Pulse 帮助销售团队将更多时间用于战略性客户互动，从而更好地服务 AWS 客户。

---

## 45. Pioneering AI workflows at scale: A deep dive into Asana AI Studio and Amazon Q index collaboration

**发布日期：** 06 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/pioneering-ai-workflows-at-scale-a-deep-dive-into-asana-ai-studio-and-amazon-q-index-collaboration/

# Asana AI Studio与Amazon Q index集成：智能工作流程的革新

当代组织面临的核心挑战是需要管理分散在多个系统中不断增长的任务和信息量。传统任务管理工具虽然可以组织工作，但往往缺乏真正高效运营所需的智能化能力。

亚马逊云科技与Asana合作推出了Asana AI Studio与Amazon Q index的集成方案，将生成式AI直接引入日常工作流程。这一集成使团队能够利用来自多种应用程序的数据，实现AI工作流程的大规模应用。通过Amazon Q Business数据访问器功能，Asana可以安全地访问和分析来自各种业务应用程序的信息，将原本孤立的数据转化为有意义的商业智能。

这一解决方案的核心优势包括：快速连接应用程序、构建集成工作流程，以及安全地扩展AI应用。具体应用场景涵盖项目接收、营销活动管理和产品发布等关键业务流程。当用户通过智能聊天提问或触发AI Studio工作流程时，Asana的AI协调器会处理查询，同时检查Asana原生数据和Amazon Q index中的相关信息，然后使用生成式AI提供上下文相关的可操作见解。

这一集成有效地打破了传统的信息孤岛，增强了协作效率，同时严格维护数据安全和访问控制，为组织提供了一个更智能、更高效的工作管理未来。

---

## 46. Responsible AI for the payments industry – Part 1

**发布日期：** 06 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/responsible-ai-for-the-payments-industry-part-1/

# 负责任的AI在支付行业的应用

支付行业正经历数字化转型，人工智能技术已成为其核心驱动力。随着全球数字支付交易预计到2027年将超过15万亿美元，AI在欺诈检测、客户服务等领域的应用日益广泛。然而，当消费者将敏感金融数据托付给支付系统时，他们不仅期望便捷和安全，还要求公平、透明和隐私保护。

文章探讨了支付行业在采用AI时面临的独特挑战和监管考量，同时介绍了AWS提供的负责任AI框架，帮助企业将负责任AI转化为竞争优势。支付行业面临多重挑战：数据分类与隐私保护、实时处理需求、全球化运营环境、普惠金融要求以及严格的监管法规。

针对这些挑战，AWS提出了负责任AI的核心原则：可控性、隐私与安全、安全性、公平性、准确性与健壮性、可解释性、透明度和治理。这些原则在实践中表现为：建立人工审核工作流程、实施多层次数据保护策略、开发先进的风险评估框架、评估模型和数据中的偏见、持续验证AI模型的准确性，以及提供清晰易懂的决策解释。

通过采用这些负责任AI原则，支付行业可以在提高效率和安全性的同时，确保AI系统公平透明，保护消费者隐私，并遵守全球监管要求，最终建立更具包容性、值得信赖的金融服务生态系统。

---

## 47. Responsible AI for the payments industry – Part 2

**发布日期：** 06 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/responsible-ai-for-the-payments-industry-part-2/

# 负责任AI在支付行业的实践应用

本文是关于支付行业负责任AI实践的系列文章第二部分，主要探讨了负责任AI框架的实际实施方案。随着AI在金融决策中扮演越来越重要的角色，金融机构面临着如何确保AI系统透明、公平且值得信赖的挑战。

文章提出了一套全面的负责任AI实施框架，将其视为产品开发全生命周期的核心原则而非额外附加层。该框架建议金融机构建立跨职能的AI责任委员会，打破传统组织边界，并制定详细的政策文档将原则转化为可操作的指南。

文章详细阐述了AI生命周期四个关键阶段的实施细节：设计阶段(评估风险、定义用例)、开发阶段(数据收集与训练)、部署阶段(环境测试与信心指标)以及运营阶段(用户反馈与系统管理)。在支付应用中，这意味着训练数据必须具有代表性，涵盖各类交易类型、商户类别和地理区域；同时需建立明确的人工干预阈值，尤其是对高价值交易或异常活动模式。

AWS提供全面的工具、框架和最佳实践，帮助支付行业利益相关者实现负责任AI实施，在加速AI采用的同时满足监管要求和客户期望。在这个以信任为基础的行业中，负责任的AI不仅是正确选择，也是业务成功的重要保障。

---

## 48. Process multi-page documents with human review using Amazon Bedrock Data Automation and Amazon SageMaker AI

**发布日期：** 06 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/process-multi-page-documents-with-human-review-using-amazon-bedrock-data-automation-and-amazon-sagemaker-ai/

# Amazon Bedrock Data Automation与SageMaker AI结合实现多页文档智能处理

各行业组织在处理大量多页文档时面临挑战，尽管自动化技术不断发展，但在特定场景下仍需人工专业知识来验证数据的准确性和质量。

2025年3月，AWS推出了Amazon Bedrock Data Automation服务，该服务能够从非结构化的多模态内容(包括文档、图像、视频和音频)中自动生成有价值的洞察。它简化了文档处理流程，通过统一的多模态推理API自动执行数据提取、转换和洞察生成，减少了数据准备、模型管理等繁琐任务，以更低的成本提供行业领先的准确性。

然而，即使拥有先进的自动化能力，某些场景仍需要人工判断。此时，Amazon Bedrock Data Automation与SageMaker AI的集成创建了强大的端到端解决方案。本文展示的架构允许系统根据置信度评分自动确定何时需要人工审核，从而实现自动化与人工审核的最佳平衡。这种集成使组织能够：验证低置信度的AI预测、有效处理边缘案例、保持监管合规性、在最大化自动化的同时保持高准确性，并通过反馈循环不断改进模型性能。这一无服务器解决方案为需要处理复杂文档的组织提供了兼具效率与准确性的智能文档处理方案。

---

## 49. Build an AI assistant using Amazon Q Business with Amazon S3 clickable URLs

**发布日期：** 05 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/build-an-ai-assistant-using-amazon-q-business-with-amazon-s3-clickable-urls/

# Amazon Q Business结合S3可点击URL构建AI助手的全新解决方案

企业组织普遍面临着构建AI助手的挑战，尤其是需要在保证文档安全的前提下让AI助手能够引用企业文档。本文介绍了一个使用Amazon Q Business创建AI助手的解决方案，该助手可以提供指向Amazon S3存储文档的可点击URL链接，支持安全的文档访问和内容验证。

Amazon Q Business是一个基于生成式AI的对话助手，能够基于企业系统中的信息回答问题并完成任务。该解决方案的核心功能在于：系统将企业文档存储在S3存储桶中并配置为数据源，当用户通过Amazon Q Business网页体验或API与AI助手交互时，助手会提供带有源文档可点击URL的回答。这使用户能够直接访问参考文档以验证AI回答的准确性，而无需拥有S3存储桶的访问凭证。

解决方案通过身份感知凭证和授权验证确保只有获得授权的用户才能查看或下载文档内容。当用户点击参考URL时，系统会调用GetDocumentContent API，Amazon Q Business会验证用户身份和访问权限，然后生成一个预签名URL供用户安全访问文档。这种机制既保证了文档的安全性，又使企业能够实践负责任的AI应用，让员工能够验证AI回答的来源和准确性。

该功能特别适用于需要基于内部文档构建安全AI助手的企业，让员工能够以用户友好的方式利用生成式AI提升工作效率，同时保持对信息来源的透明度和可验证性。

---

## 50. GPT OSS models from OpenAI are now available on SageMaker JumpStart

**发布日期：** 05 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/gpt-oss-models-from-openai-are-now-available-on-sagemaker-jumpstart/

# OpenAI GPT OSS模型现已在SageMaker JumpStart上可用

随着人工智能技术的快速发展，企业和开发者对强大且可定制的大语言模型的需求不断增长。然而，许多组织在部署和管理这些模型时面临技术门槛高、安全控制不足以及缺乏企业级支持等挑战。

亚马逊AWS宣布OpenAI的开源权重模型gpt-oss-120b和gpt-oss-20b现已在SageMaker JumpStart平台上正式提供。这两款模型在编码、科学分析和数学推理任务方面表现卓越，拥有128K的上下文窗口，并支持可调节的推理水平(低/中/高)以满足不同需求。用户可以通过SageMaker JumpStart界面或Python SDK轻松部署和使用这些模型，同时享受AWS企业级安全保障。

这一功能解决了企业在采用先进语言模型时的关键痛点：模型可在安全的AWS环境中部署，受VPC控制保护，支持数据安全；用户可以完全自定义模型以满足特定业务需求；模型支持外部工具集成，包括EXA提供的网络搜索功能；同时还具备完整的思维链输出能力，提供模型推理过程的详细可见性。通过SageMaker JumpStart提供的这些模型，企业可以在AWS基础设施上安全、可控地开发和扩展生成式AI应用，而不必担心基础设施管理和安全合规问题。

---

## 51. Discover insights from Microsoft Exchange with the Microsoft Exchange connector for Amazon Q Business

**发布日期：** 05 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/discover-insights-from-microsoft-exchange-with-the-microsoft-exchange-connector-for-amazon-q-business/

# Amazon Q Business Microsoft Exchange连接器：释放企业邮件数据价值

Amazon Q Business作为一款由生成式AI驱动的企业助手，通过整合企业各类数据源提供统一的信息获取和处理能力。然而，许多企业面临的痛点在于，存储在Microsoft Exchange中的大量邮件、附件、日历和联系人等宝贵信息难以高效利用，员工经常需要在繁杂的邮件系统中耗费大量时间寻找关键信息。

文章重点介绍了Amazon Q Business全新推出的Microsoft Exchange连接器，它能够将Microsoft Exchange中的数据无缝集成到Amazon Q Business的统一索引中。该连接器支持以下核心功能：集中访问Exchange数据、基于自然语言的智能搜索和检索、增强员工协作效率、确保数据访问安全合规，以及简化工作流程和决策过程。

通过这一连接器，企业能够让员工使用自然语言直接查询邮件中的信息，例如询问"明天与账单团队会议的议程是什么"或"关于最近CloudTrail变更的主要功能和行动项是什么"，并获得准确回答。这解决了企业邮件系统中信息碎片化、难以检索的问题，显著提升了员工生产力，使他们能够更快速地获取关键信息进行决策，从而释放了存储在Microsoft Exchange中数据的全部价值。

---

## 52. Cost tracking multi-tenant model inference on Amazon Bedrock

**发布日期：** 04 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/cost-tracking-multi-tenant-model-inference-on-amazon-bedrock/

# 多租户模型推理的成本追踪解决方案

在利用AI应用服务多个租户的组织中，一个常见挑战是如何跟踪、分析和优化不同客户群体的模型使用情况。虽然Amazon Bedrock通过其Converse API提供强大的基础模型能力，但真正的商业价值在于能够将模型交互与特定租户、用户和用例联系起来。

文章介绍了一种使用Converse API的requestMetadata参数的解决方案，通过在每个请求中传递租户特定的标识符和上下文信息，可以将标准调用日志转化为丰富的分析数据集。这种方法能够精确到租户级别来衡量模型性能、跟踪使用模式和分配成本，而无需修改核心应用程序逻辑。

该解决方案包含一个全面的日志处理和分析架构，通过ETL管道处理Amazon Bedrock调用日志，将包含租户元数据的日志转换为可操作的商业智能。系统使用AWS Glue进行数据处理和转换，并通过Amazon QuickSight Enterprise版本提供强大的可视化和报告功能。最终，这套架构帮助组织解决了几个关键问题：1) 准确追踪不同租户的模型使用情况；2) 基于实际使用模式制定更精确的定价模型；3) 根据租户特定需求识别模型优化机会；4) 为产品团队提供数据支持以优先开发更有价值的功能。这一解决方案为组织构建了AI策略的分析基础，实现了更加个性化的AI体验。

---

## 53. AI judging AI: Scaling unstructured text analysis with Amazon Nova

**发布日期：** 04 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/ai-judging-ai-scaling-unstructured-text-analysis-with-amazon-nova/

# AI 评估 AI：通过 Amazon Nova 实现非结构化文本分析的规模化

这篇博客文章讨论了组织在处理大量非结构化文本数据(如客户反馈)时面临的挑战。传统的手动分析方法既费时又耗资源——例如，手动审核2,000条评论可能需要超过80小时。虽然大型语言模型(LLM)可以高效地生成文本摘要，但单一模型的输出可能存在偏见、幻觉或确认偏差等问题。

文章介绍了一种基于Amazon Bedrock的"LLM评审团"解决方案，该方案利用多个生成式AI模型(如Amazon Nova Pro、Claude 3 Sonnet和Llama 3)来相互评估彼此的输出。这种方法不仅可以生成文本主题摘要，还能通过多模型交叉验证来评估这些摘要的准确性和相关性。

整个工作流程包括四个主要步骤：数据预处理和上传、主题生成、多模型评估以及与人工评分的统计比较。文章提供了详细的实现方法，并介绍了评估指标如百分比一致性、Cohen's kappa等。研究表明，LLM之间的一致性可达91%，而与人类评估的一致性可达79%，这意味着虽然LLM可以提供可靠的主题评估，但人类监督仍然重要，尤其是在识别LLM可能忽略的细微上下文差异方面。

这一解决方案通过Amazon Bedrock的模型托管能力，使组织能够高效地利用多个AI模型实现大规模文本分析，同时保持高质量的输出。

---

## 54. Building an AI-driven course content generation system using Amazon Bedrock

**发布日期：** 04 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/building-an-ai-driven-course-content-generation-system-using-amazon-bedrock/

# AI驱动的课程内容生成系统：使用Amazon Bedrock提升教育效率

教育领域面临的主要挑战是课程材料开发既费时又需高质量，且必须跟上快速变化的知识领域。教师通常需要花费数天时间来创建教学内容和测验，这不仅导致创新教学时间不足，还造成课程材料质量不一致，影响教师和学生的体验。

本文介绍了一个基于Amazon Bedrock和Anthropic的Claude 3.5大语模型的AI驱动课程内容生成系统。该系统主要包含两个核心功能模块：课程大纲生成和课程内容生成。课程大纲模块能自动创建结构化的课程框架，包含每周模块和子模块；内容生成模块则根据大纲为每个模块生成详细文本内容、视频脚本以及相应的多选题。

该解决方案采用WebSocket API实现实时交互，整合了AWS多种服务，如Lambda、SQS、S3、DynamoDB、Cognito和WAF等，构建了安全、可扩展的架构。系统大大缩短了课程开发周期，将原本需要数天的工作减少到几小时，同时确保教材保持最新且内容全面，让教育工作者有更多时间专注于互动教学和创新教学策略，有效应对现代教育需求。

---

## 55. How Handmade.com modernizes product image and description handling with Amazon Bedrock and Amazon OpenSearch Service

**发布日期：** 04 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/how-handmade-com-modernizes-product-image-and-description-handling-with-amazon-bedrock-and-amazon-opensearch-service/

# Handmade.com如何借助Amazon Bedrock和OpenSearch Service现代化产品图像和描述处理

Handmade.com作为全球领先的手工艺品在线市场，面临着产品数量快速增长的挑战。随着目录中超过60,000件产品，其中许多产品描述过于简单，难以实现良好的搜索效果和搜索引擎优化。传统的人工处理方式每周需要约10小时，且需要多名团队成员维持基本质量。随着市场规模扩大，自动化和提升产品描述质量的需求日益迫切。

针对这一痛点，Handmade.com实施了一套基于Amazon Bedrock和Amazon OpenSearch Service的AI驱动解决方案。该方案融合了大语言模型和向量搜索技术，构建了端到端的自动化流程：首先使用Anthropic的Claude 3.7 Sonnet模型分析产品图像并生成初步描述；然后通过Amazon Titan Text Embeddings V2模型将这些描述转换为向量并存储在OpenSearch Service中；最后利用检索增强生成(RAG)技术，结合语义搜索结果生成针对每个产品优化的SEO描述。

这套解决方案有效解决了多个关键问题：自动生成符合不同手工艺品独特特性的精准描述；大幅减少从卖家提交到产品上线的时间，满足卖家期望的一小时内上线要求；支持多语言内容生成，促进全球市场扩展；提升产品可发现性和SEO表现。系统还整合了客户互动数据和评论信息，持续优化描述生成和产品展示效果，为Handmade.com打造了一个可扩展、高效的产品内容管理流程。

---

## 56. Introducing Amazon Bedrock AgentCore Browser Tool

**发布日期：** 01 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-browser-tool/

# Amazon Bedrock AgentCore 浏览器工具：实现大规模AI网络自动化

AWS在纽约峰会上宣布预览版发布Amazon Bedrock AgentCore浏览器工具，这是一款完全托管的云端浏览器解决方案。该工具解决了两大根本性挑战：首先，基础模型(FMs)基于静态数据集训练，当API不可用时缺乏获取实时信息的能力；其次，企业在尝试使用AI进行大规模网络自动化时面临诸多困难。

AgentCore浏览器工具使AI代理能够像人类一样与网站和网页应用交互，无需复杂的基础设施管理。它提供了完整的导航控制、表单操作、视觉理解和JavaScript应用支持能力，同时确保企业级安全性和可扩展性。用户可以通过Playwright等浏览器操作库，或者Amazon Nova Act等AI代理框架来使用该工具。

这一创新解决方案特别适用于重复性网络任务自动化、AI驱动的研究与信息收集、跨系统工作流自动化、大规模测试与质量保证，以及无API的遗留系统集成。企业可从AWS全托管的基础设施中获益，无需维护浏览器实例集群，显著降低成本和管理复杂度，同时实现从单个会话到数千个并发会话的无缝扩展，支持各种企业级AI自动化应用场景。

---

## 57. Introducing the Amazon Bedrock AgentCore Code Interpreter

**发布日期：** 01 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-agentcore-code-interpreter/

# Amazon Bedrock AgentCore代码解释器：安全执行AI生成代码的完整解决方案

当前AI代理已经能够生成复杂代码，但在生产环境中安全执行这些代码成为严峻挑战。企业面临的主要痛点包括：AI生成代码的安全漏洞风险、搭建执行环境的基础设施成本高、扩展性瓶颈、集成复杂度大，以及合规难题。这些障碍限制了组织充分利用AI代理的计算能力。

Amazon Bedrock AgentCore代码解释器是专为解决这些挑战而推出的全托管服务，允许AI代理在隔离的沙箱环境中安全执行代码。该服务的核心优势在于：增强的安全态势，支持从完全隔离到可控网络连接的多种配置；零基础设施管理，减少了专业DevOps资源需求；动态扩展性，自动资源分配以处理变化的工作负载；框架无关的集成，原生支持Strands、LangChain等主流AI框架；以及内置的企业级合规功能。

AgentCore代码解释器为AI代理提供了执行Python、JavaScript和TypeScript代码的安全环境，支持复杂数据分析、可视化和数学计算。它通过安全沙箱架构、高级会话管理、完整的Python运行环境和强大的文件操作能力，使企业能够构建更智能、更安全的AI应用，从自动化财务分析到交互式数据科学助手等广泛场景。

---

## 58. Observing and evaluating AI agentic workflows with Strands Agents SDK and Arize AX

**发布日期：** 01 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/observing-and-evaluating-ai-agentic-workflows-with-strands-agents-sdk-and-arize-ax/

# Strands Agents SDK和Arize AX：为AI代理工作流提供可观察性与评估能力

在AI代理应用中，由于基于大语言模型(LLM)的非确定性特性，同样的输入可能产生不同的输出，这给应用设计者带来了巨大挑战。组织在部署代理工作流时需要可靠的可观察性系统来确保结果的正确性和可信度。

本文介绍了Arize AX服务与Strands Agents SDK的强大组合，这一集成解决方案旨在解决生成式AI应用面临的关键问题，包括规模化后的不可预测行为、隐藏的失败模式、非确定性路径、工具集成复杂性以及成本和性能变异等。

Arize AX提供了全面的可观察性、评估和实验框架，具有追踪、评估、数据集管理、实验、交互式环境、提示管理、监控告警以及代理可视化等功能。结合Strands Agents低代码框架，用户可以构建代理、进行可观察性监控、测试并生成跟踪数据、在Arize AI中分析跟踪数据、评估代理行为并优化代理性能。

这一集成解决方案使团队能够深入了解AI代理的行为和决策过程，通过LLM作为评判器自动识别失败案例，建立回归数据集推动改进工作流程，并在提示实验环境中测试不同选项。该方案为组织提供了从开发到生产全生命周期管理AI代理系统的强大工具，确保AI系统产出可靠且值得信赖的结果。

---

## 59. Building AIOps with Amazon Q Developer CLI and MCP Server

**发布日期：** 01 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/building-aiops-with-amazon-q-developer-cli-and-mcp-server/

# 构建AIOps：整合Amazon Q Developer CLI与MCP服务器的创新方案

IT团队在管理日益复杂的基础设施和应用程序时面临诸多挑战，他们往往需要花费大量时间手动识别运营问题、排除故障并执行重复性维护工作。这种运营负担分散了宝贵的技术资源，使其无法专注于创新和战略性工作。

文章介绍了如何利用Amazon Q Developer CLI和模型上下文协议(MCP)服务器构建强大的AIOps(人工智能运维)解决方案。这一低代码/无代码解决方案能够通过自然语言交互大幅减少手动工作。MCP服务器作为AI模型的通用连接器，使Amazon Q能够与外部系统交互，获取实时数据并无缝集成各种工具。

该解决方案专门解决三类关键运维问题：识别并修复EC2实例中的高CPU使用率、检测并移除S3存储桶的公共访问权限、识别并阻止EC2实例的特定不需要开放的入站连接端口。通过单一配置文件(mcp.json)，IT团队可以配置Amazon Q Developer CLI的MCP服务器连接到外部系统，使用自然语言处理运营查询，并自动化执行所需任务。这一集成方案帮助组织在保持安全态势的同时，高效地监控、识别和排除运营事件问题，从而大幅提升运营效率。

---

## 60. Containerize legacy Spring Boot application using Amazon Q Developer CLI and MCP server

**发布日期：** 01 AUG 2025
**原文链接：** https://aws.amazon.com/blogs/machine-learning/containerize-legacy-spring-boot-application-using-amazon-q-developer-cli-and-mcp-server/

# 容器化传统Spring Boot应用：Amazon Q Developer CLI与MCP服务器的应用实践

在应用迁移和现代化过程中，企业常面临将传统应用容器化的挑战，包括兼容性问题、依赖关系处理和配置调整等，这些都会导致开发团队大量时间花费在手动编码、测试和调试上。

本文介绍了如何利用Amazon Q Developer命令行界面(CLI)与模型上下文协议(MCP)服务器集成，来实现传统Java Spring Boot应用的现代化和向AWS迁移。这一解决方案使开发人员能够通过自然语言提示，无需编写代码即可自动化完成应用迁移的核心步骤：从Java 8升级到Java 21、从Spring Boot 2.3.x升级到Spring Boot 3.5.0、应用容器化，以及部署到Amazon EKS(Elastic Kubernetes Service)。

这种方法通过自动处理代码转换、依赖更新和部署配置，显著降低了应用现代化的复杂性。Amazon Q Developer CLI能理解上下文信息并连接外部工具和服务，在整个迁移过程中提供智能辅助，让开发团队可以更专注于创新而非处理繁琐的任务。该解决方案还包括故障引入和问题排查功能，帮助开发人员应对生产环境中可能出现的复杂情况，展示了AI驱动工具在简化应用现代化和云迁移方面的强大潜力。

---

