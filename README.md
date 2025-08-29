# AWS 博客摘要生成器

基于客户信息筛选感兴趣的AWS机器学习博客文章并生成中文摘要的自动化工具。

## 功能特性

- 🎯 **智能筛选**：基于客户信息自动判断文章相关性
- 📝 **自动摘要**：生成300字左右的中文摘要
- 🔄 **多数据源**：优先使用MCP获取内容，失败时自动回退到HTML解析
- 📊 **统计分析**：提供筛选效率和处理统计
- 🎯 **PowerPoint演示文稿生成**：自动生成专业的PowerPoint演示文稿
- 📊 **双重输出格式**：同时支持Markdown和PowerPoint格式输出


## 环境要求

### 必需依赖
- Python 3.7+
- AWS账户和适当的IAM权限
- AWS Bedrock访问权限（us-east-1区域）
- AWS Knowledge MCP Server（推荐使用Kiro配置）

### Python包依赖
```bash
pip install boto3 requests beautifulsoup4 mcp python-pptx
```

### AWS权限要求
确保您的AWS凭证具有以下权限：
- `bedrock:InvokeModel`
- 访问Claude 3.7 Sonnet模型的权限

## 快速开始

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
# 使用AWS CLI
aws configure

# 或设置环境变量
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1
```

### 4. 配置客户信息
编辑 `customer_info.py` 文件，填入您的客户信息：

```python
customer_description = "您的公司描述..."
AI_application_description = "您的AI应用场景..."
AI_workload_Description = "您的基础设施情况..."
```

## 使用方法

### 基本用法
```bash
# 处理2025年8月的博客
python aws_blog_summarizer_mcp.py --month 2025-08

# 处理2025年9月的博客
python aws_blog_summarizer_mcp.py --month 2025-09
```

### 高级选项
```bash
# 指定扫描页面数量
python aws_blog_summarizer_mcp.py --month 2025-08 --pages 3

# 生成PowerPoint演示文稿（同时生成Markdown和PowerPoint）
python aws_blog_summarizer_mcp.py --month 2025-08 --ppt

# 仅生成PowerPoint演示文稿
python aws_blog_summarizer_mcp.py --month 2025-08 --ppt-only

# 使用自定义PowerPoint模板
python aws_blog_summarizer_mcp.py --month 2025-08 --ppt --ppt-template custom_template.json

# 查看帮助信息
python aws_blog_summarizer_mcp.py --help
```

### 参数说明
- `--month`：目标月份，格式为 YYYY-MM（默认：2025-08）
- `--pages`：扫描的博客页面数量（默认：2）
- `--ppt` 或 `--powerpoint`：生成PowerPoint演示文稿（同时生成Markdown）
- `--ppt-only`：仅生成PowerPoint演示文稿（不生成Markdown）
- `--ppt-template`：指定自定义PowerPoint模板配置文件路径

## 输出结果

### 输出文件
程序支持两种输出格式：

#### Markdown格式 (默认)
生成名为 `aws_blog_summaries_YYYY_MM_optimized.md` 的文件，包含：
- 📋 筛选后的文章摘要
- 📅 发布日期和原文链接
- ✅ 兴趣度评分标识
- 📊 处理统计信息

#### PowerPoint格式 (新功能)
生成名为 `aws_blog_summaries_YYYY_MM_optimized.pptx` 的演示文稿，包含：
- 🎯 **标题幻灯片**：包含报告标题和生成日期
- 📊 **统计概览幻灯片**：展示分析统计和客户信息
- 📝 **文章摘要幻灯片**：每篇感兴趣的文章单独一页
- 💡 **总结建议幻灯片**：分析结论和行动建议

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

## PowerPoint功能

### 演示文稿结构
1. **标题页**：报告标题、目标月份、生成日期
2. **统计页**：处理文章数、感兴趣文章数、筛选效率、客户信息概览
3. **摘要页**：每篇感兴趣文章的详细摘要（每篇一页，包含原文链接）
4. **总结页**：主要发现、技术趋势分析和行动建议

### 功能特性
- ✅ **16:9宽屏比例**：现代16:9幻灯片比例，适合各种显示设备
- ✅ **原文链接**：每张摘要幻灯片底部显示可点击的原文链接
- ✅ **优化字体**：标题16pt，内容10pt，链接9pt，紧凑布局不溢出
- ✅ **美观格式**：使用表情符号、清晰段落结构和紧凑行间距
- ✅ **智能截断**：标题和内容智能截断，保持重要信息完整
- ✅ **自动换行**：内容自动换行，充分利用16:9宽屏空间

### 自定义模板
创建JSON格式的模板配置文件：
```json
{
  "theme_name": "widescreen_16_9",
  "primary_color": "#2c5aa0",
  "secondary_color": "#5cb85c",
  "font_family": "Calibri",
  "title_font_size": 16,
  "subtitle_font_size": 12,
  "content_font_size": 10,
  "url_font_size": 9
}
```

### 技术规格
- **幻灯片比例**：16:9 (13.33" × 7.5")
- **字体优化**：紧凑布局，适应现代显示器
- **行间距**：1.0倍，最大化内容显示
- **内容长度**：最多800字符，充分利用宽屏空间

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

**Q: PowerPoint生成失败**
```
A: 确保已安装python-pptx库：pip install python-pptx
   如果仍然失败，程序会继续生成Markdown文件
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
- PowerPoint生成状态
- 错误信息和回退策略

## 项目结构

```
├── aws_blog_summarizer_mcp.py        # 主程序文件
├── powerpoint_generator.py           # PowerPoint生成模块
├── customer_info.py                  # 客户信息配置
├── requirements.txt                  # 依赖包列表
├── README.md                         # 项目说明文档
├── aws_blog_summaries_*.md           # 生成的Markdown摘要文件
└── aws_blog_summaries_*.pptx         # 生成的PowerPoint演示文稿
```

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

本项目采用MIT许可证。

## 联系方式

如有问题或建议，请通过Issue联系我们。