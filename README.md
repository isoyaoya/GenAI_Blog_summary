# AWS 生成式AI博客摘要生成器

基于客户信息筛选感兴趣的AWS机器学习博客文章并生成中文摘要的自动化工具。

## 项目介绍

这个项目帮助您从AWS机器学习博客中自动筛选和总结与您业务相关的文章。通过结合AWS Bedrock Claude模型和AWS Knowledge MCP Server，实现：

- 🎯 **智能筛选**：基于客户信息自动判断文章相关性
- 📝 **自动摘要**：生成300字左右的中文摘要
- 🔄 **多数据源**：优先使用MCP获取内容，失败时自动回退到HTML解析
- 📊 **统计分析**：提供筛选效率和处理统计

## 功能特性

### 核心功能
- 按月份筛选AWS机器学习博客文章
- 基于客户业务场景智能评估文章相关性
- 自动生成结构化的中文摘要
- 支持批量处理和进度跟踪


## 如何使用
### 必需依赖
- Python 3.7+
- AWS账户和适当的IAM权限
- AWS Bedrock访问权限（us-east-1区域）
- 使用AWS Q cli 或者Kiro并且已经配置好了AWS Knowledge MCP Server
https://awslabs.github.io/mcp/servers/aws-knowledge-mcp-server/

### Python包依赖
```bash
pip install boto3 requests beautifulsoup4 mcp
```

### AWS权限要求
确保您的AWS凭证具有以下权限：
- `bedrock:InvokeModel`
- 访问Claude 3.7 Sonnet模型的权限

## 安装配置

### 1. 克隆项目
```bash
git clone https://github.com/isoyaoya/GenAI_Blog_summary.git
cd GenAI_Blog_summary

```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置AWS凭证
```bash
# 方法1：使用AWS CLI
aws configure

# 方法2：设置环境变量
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

### 4. 配置客户信息
编辑 `customer_info.py` 文件，填入您的客户信息：

```python
# 客户公司描述
customer_description = "您的公司描述..."

# AI应用场景描述  
AI_application_description = "您的AI应用场景..."

# 基础设施描述
AI_workload_Description = "您的基础设施情况..."
```

## 使用方法

### 基本用法
```bash
# 处理2025年8月的博客
python aws_blog_summarizer_optimized.py --month 2025-08

# 处理2025年9月的博客
python aws_blog_summarizer_optimized.py --month 2025-09
```

### 高级选项
```bash
# 指定扫描页面数量
python aws_blog_summarizer_optimized.py --month 2025-08 --pages 3

# 查看帮助信息
python aws_blog_summarizer_optimized.py --help
```

### 参数说明
- `--month`：目标月份，格式为 YYYY-MM（默认：2025-08）
- `--pages`：扫描的博客页面数量（默认：2）

## 输出结果

### 输出文件
程序会生成名为 `aws_blog_summaries_YYYY_MM_optimized.md` 的Markdown文件，包含：

- 📋 筛选后的文章摘要
- 📅 发布日期和原文链接
- ✅ 兴趣度评分标识
- 📊 处理统计信息

### 摘要格式
每篇文章摘要包含：
1. **背景和痛点**：文章要解决的问题
2. **主要方案**：介绍的技术方案或新功能
3. **解决价值**：方案能解决的具体问题

### 统计信息
- 总处理文章数
- 客户感兴趣文章数
- 筛选效率百分比

## 工作流程

1. **获取博客列表**：从AWS机器学习博客获取指定月份的文章
2. **内容获取**：优先使用MCP Server，失败时回退到HTML解析
3. **兴趣评估**：使用Claude模型基于客户信息判断相关性
4. **摘要生成**：为感兴趣的文章生成结构化摘要
5. **结果输出**：生成Markdown格式的最终报告

## 故障排除

### 常见问题

**Q: Bedrock调用失败**
```
A: 检查AWS凭证和区域设置，确保有bedrock:InvokeModel权限
```

**Q: MCP连接失败**
```
A: 程序会自动回退到HTML解析，不影响正常使用
```

**Q: 找不到目标月份文章**
```
A: 检查月份格式是否正确（YYYY-MM），或尝试增加扫描页面数
```

### 调试模式
程序会输出详细的处理日志，包括：
- 页面获取状态
- 文章处理进度
- 兴趣评估结果
- 错误信息和回退策略

## 项目结构

```
├── aws_blog_summarizer_optimized.py  # 主程序文件
├── customer_info.py                   # 客户信息配置
├── requirements.txt                   # 依赖包列表
├── README.md                         # 项目说明文档
└── aws_blog_summaries_*.md           # 生成的摘要文件
```

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

本项目采用MIT许可证。

## 联系方式

如有问题或建议，请通过Issue联系我们。