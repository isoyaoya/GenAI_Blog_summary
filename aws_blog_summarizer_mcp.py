#!/usr/bin/env python3
"""
AWS 生成式AI博客摘要生成器 - 优化版本
基于客户信息智能筛选感兴趣的博客文章并生成摘要
使用AWS Knowledge MCP Server搜索和获取博客内容

使用方法:
python aws_blog_summarizer_optimized.py --month 2025-08
python aws_blog_summarizer_optimized.py --month 2025-09
"""

import asyncio
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
import os
import sys
import argparse
import boto3
from botocore.exceptions import ClientError
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from customer_info import customer_description, AI_application_description, AI_workload_Description

class AWSBlogSummarizerOptimized:
    def __init__(self, target_month="2025-08"):
        self.base_url = "https://aws.amazon.com/blogs/machine-learning/"
        self.target_month = target_month
        self.max_pages = 2
        # 初始化Bedrock客户端
        self.bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
        
        # 客户信息
        self.customer_description = customer_description
        self.ai_application_description = AI_application_description
        self.ai_workload_description = AI_workload_Description
    
    def get_blog_list(self, page=1):
        """获取博客列表页面"""
        try:
            if page == 1:
                url = self.base_url
            else:
                url = f"{self.base_url}page/{page}/"
            
            print(f"正在获取第 {page} 页: {url}")
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"获取博客列表第 {page} 页失败: {e}")
            return None
    
    def get_all_blog_posts(self):
        """获取所有页面的博客文章"""
        all_posts = []
        
        for page in range(1, self.max_pages + 1):
            html_content = self.get_blog_list(page)
            if html_content:
                posts = self.parse_blog_links(html_content)
                if posts:
                    all_posts.extend(posts)
                    print(f"第 {page} 页找到 {len(posts)} 篇文章")
                else:
                    print(f"第 {page} 页没有找到文章，可能已到最后一页")
                    break
            else:
                print(f"无法获取第 {page} 页内容")
                break
        
        return all_posts
    
    def parse_blog_links(self, html_content):
        """解析博客链接和发布日期"""
        soup = BeautifulSoup(html_content, 'html.parser')
        blog_posts = []
        
        # 查找博客文章链接
        articles = soup.find_all('article') or soup.find_all('div', class_=re.compile(r'post|article|blog'))
        
        for article in articles:
            # 查找标题链接
            title_link = article.find('a', href=True)
            if not title_link:
                continue
                
            # 查找日期
            date_elem = article.find('time') or article.find('span', class_=re.compile(r'date|time'))
            if not date_elem:
                continue
                
            date_text = date_elem.get_text().strip()
            
            # 检查是否为目标月份的文章
            if self.is_target_month(date_text):
                blog_posts.append({
                    'title': title_link.get_text().strip(),
                    'url': self.normalize_url(title_link['href']),
                    'date': date_text
                })
        
        return blog_posts
    
    def is_target_month(self, date_text):
        """检查日期是否为目标月份"""
        # 解析目标月份 (格式: YYYY-MM)
        try:
            year, month = self.target_month.split('-')
            month_num = month.zfill(2)  # 确保月份是两位数
            
            # 月份名称映射
            month_names = {
                '01': ['January', 'Jan'], '02': ['February', 'Feb'], '03': ['March', 'Mar'],
                '04': ['April', 'Apr'], '05': ['May', 'May'], '06': ['June', 'Jun'],
                '07': ['July', 'Jul'], '08': ['August', 'Aug'], '09': ['September', 'Sep'],
                '10': ['October', 'Oct'], '11': ['November', 'Nov'], '12': ['December', 'Dec']
            }
            
            # 构建匹配模式
            patterns = [
                rf'{year}.*{month_num}',  # 2025-08 或 2025/08
                rf'{month_num}.*{year}',  # 08-2025 或 08/2025
            ]
            
            # 添加月份名称模式
            if month_num in month_names:
                for month_name in month_names[month_num]:
                    patterns.append(rf'{month_name}.*{year}')  # August 2025
            
            # 检查所有模式
            for pattern in patterns:
                if re.search(pattern, date_text, re.IGNORECASE):
                    return True
            return False
            
        except ValueError:
            print(f"无效的月份格式: {self.target_month}，应该使用 YYYY-MM 格式")
            return False
    
    def normalize_url(self, url):
        """标准化URL"""
        if url.startswith('/'):
            return f"https://aws.amazon.com{url}"
        elif not url.startswith('http'):
            return f"https://aws.amazon.com/blogs/machine-learning/{url}"
        return url
    
    async def get_article_content_via_mcp_async(self, url):
        """使用AWS Knowledge MCP获取文章内容 (异步版本)"""
        try:
            print(f"使用MCP获取文章内容: {url}")
            
            server_params = StdioServerParameters(
                command="npx",
                args=["mcp-remote", "https://knowledge-mcp.global.api.aws"]
            )
            
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    
                    # 调用read_documentation工具
                    result = await session.call_tool("aws___read_documentation", {
                        "url": url
                    })
                    
                    if result.content and len(result.content) > 0:
                        # 获取返回的内容
                        content_data = result.content[0]
                        
                        # 解析MCP返回的内容
                        if hasattr(content_data, 'text'):
                            raw_content = content_data.text
                        else:
                            raw_content = str(content_data)
                        
                        # 尝试解析JSON格式的响应
                        try:
                            parsed_data = json.loads(raw_content)
                            if 'response' in parsed_data and 'payload' in parsed_data['response']:
                                markdown_content = parsed_data['response']['payload']['content']['result']
                            else:
                                markdown_content = raw_content
                        except (json.JSONDecodeError, KeyError):
                            markdown_content = raw_content
                        
                        # 从markdown内容中提取标题
                        lines = markdown_content.split('\n')
                        title = ""
                        for line in lines:
                            if line.startswith('# '):
                                title = line[2:].strip()
                                break
                        
                        print(f"MCP成功获取内容，长度: {len(markdown_content)} 字符")
                        return {"title": title, "content": markdown_content}
                    else:
                        print("MCP返回空内容")
                        return None
                        
        except Exception as e:
            print(f"MCP调用失败: {e}")
            return None
    
    def get_article_content_via_mcp(self, url):
        """使用AWS Knowledge MCP获取文章内容 (同步包装器)"""
        try:
            # 运行异步函数
            result = asyncio.run(self.get_article_content_via_mcp_async(url))
            if result:
                return result
            else:
                print("MCP调用失败，回退到HTML解析")
                return self.get_article_content_fallback(url)
        except Exception as e:
            print(f"MCP调用异常: {e}，回退到HTML解析")
            return self.get_article_content_fallback(url)
    
    def get_article_content_fallback(self, url):
        """备用的HTML解析方法"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 获取文章标题
            title = ""
            title_selectors = ['h1', '.entry-title', '.post-title', 'title']
            for selector in title_selectors:
                title_elem = soup.select_one(selector)
                if title_elem:
                    title = title_elem.get_text().strip()
                    break
            
            # 查找文章主体内容
            content_selectors = [
                'article .entry-content',
                '.post-content',
                '.blog-post-content',
                'main article',
                '.content'
            ]
            
            content = None
            for selector in content_selectors:
                content = soup.select_one(selector)
                if content:
                    break
            
            if not content:
                content = soup.find('body')
            
            # 提取文本内容
            if content:
                # 移除脚本和样式标签
                for script in content(["script", "style"]):
                    script.decompose()
                text_content = content.get_text().strip()
                return {"title": title, "content": text_content}
            
            return {"title": title, "content": ""}
        except Exception as e:
            print(f"获取文章内容失败 {url}: {e}")
            return {"title": "", "content": ""}
    
    def get_article_content(self, url):
        """获取文章内容（优先使用MCP，失败时回退到HTML解析）"""
        return self.get_article_content_via_mcp(url)
    
    def assess_customer_interest(self, title, content):
        """
        使用Claude 3.7模型评估客户对文章的兴趣度
        返回: 0 (不感兴趣) 或 1 (感兴趣)
        """
        # 限制内容长度以避免token限制
        max_content_length = 8000
        if len(content) > max_content_length:
            content = content[:max_content_length] + "..."
        
        try:
            interest_score = self.call_bedrock_claude_for_interest(title, content)
            return interest_score
        except Exception as e:
            print(f"评估客户兴趣度失败: {e}")
            # 如果调用失败，默认返回感兴趣以避免遗漏
            return 1
    
    def call_bedrock_claude_for_interest(self, title, content):
        """调用AWS Bedrock Claude模型评估客户兴趣度"""
        prompt = f"""
你需要根据客户信息严格判断客户是否会对这篇AWS博客文章感兴趣。

客户信息：
公司描述：{self.customer_description}

AI应用场景：{self.ai_application_description}

基础设施情况：{self.ai_workload_description}

博客文章信息：
标题：{title}
内容：{content}

判断标准（必须同时满足多个条件才能判定为感兴趣）：

核心匹配度评估：
1. **业务场景匹配**：文章的应用场景是否与客户的核心业务场景高度相关？
   - 即使使用相同的AWS服务，但应用领域完全不同也应判定为不感兴趣

2. **技术方案相关性**：文章介绍的技术方案是否能直接应用到客户的业务中？
   - 解决的技术问题是否是客户会遇到的问题

3. **实际业务价值**：文章内容是否能为客户带来直接的业务价值？

注意事项：
- 仅仅使用相同的AWS服务，但应用场景完全不同的文章应判定为不感兴趣
- 文章必须在业务场景、技术方案、实际价值三个维度都有较高相关性才能判定为感兴趣


请只回答数字：
0 - 客户不会感兴趣（业务场景不匹配或相关性较低）
1 - 客户会感兴趣（业务场景高度匹配且有直接应用价值）

不要解释原因，只输出数字0或1。
"""

        try:
            # 构建请求体
            request_body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 10,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
            
            # 调用Bedrock
            response = self.bedrock_client.invoke_model(
                modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
                body=json.dumps(request_body),
                contentType="application/json"
            )
            
            # 解析响应
            response_body = json.loads(response['body'].read())
            result = response_body['content'][0]['text'].strip()
            
            # 提取数字结果
            if '1' in result:
                return 1
            elif '0' in result:
                return 0
            else:
                # 如果无法解析，默认返回感兴趣
                print(f"无法解析兴趣度结果: {result}，默认返回感兴趣")
                return 1
            
        except ClientError as e:
            print(f"Bedrock调用失败: {e}")
            raise e
        except Exception as e:
            print(f"处理Bedrock响应失败: {e}")
            raise e
    
    def generate_summary(self, title, content):
        """使用AWS Bedrock Claude生成文章摘要"""
        # 限制内容长度以避免token限制
        max_content_length = 15000
        if len(content) > max_content_length:
            content = content[:max_content_length] + "..."
        
        try:
            summary = self.call_bedrock_claude_for_summary(title, content)
            return summary
        except Exception as e:
            print(f"生成摘要失败: {e}")
            # 如果Bedrock调用失败，使用简单的备用方法
            return self.create_fallback_summary(title, content)
    
    def call_bedrock_claude_for_summary(self, title, content):
        """调用AWS Bedrock Claude模型生成摘要"""
        prompt = f"""
请为以下AWS机器学习博客文章生成一个300字左右的中文摘要。

摘要应该包含：
1. 背景和痛点是什么
2. 文章主要讲了什么方案或发布了什么功能
3. 这个方案/功能是解决什么问题的

文章标题：{title}

文章内容：
{content}

请用自然流畅的中文写作，不要使用模板化的语言。直接给出摘要内容，不需要其他格式。
"""

        try:
            # 构建请求体
            request_body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
            
            # 调用Bedrock
            response = self.bedrock_client.invoke_model(
                modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
                body=json.dumps(request_body),
                contentType="application/json"
            )
            
            # 解析响应
            response_body = json.loads(response['body'].read())
            summary = response_body['content'][0]['text'].strip()
            
            return summary
            
        except ClientError as e:
            print(f"Bedrock调用失败: {e}")
            raise e
        except Exception as e:
            print(f"处理Bedrock响应失败: {e}")
            raise e
    
    def create_fallback_summary(self, title, content):
        """备用摘要生成方法（当Bedrock不可用时）"""
        # 简单提取文章开头和关键信息
        sentences = [s.strip() for s in content.split('.') if len(s.strip()) > 30]
        
        # 取前几句作为基础
        intro_sentences = sentences[:5] if len(sentences) >= 5 else sentences
        intro_text = '. '.join(intro_sentences)
        
        if len(intro_text) > 300:
            intro_text = intro_text[:297] + "..."
        
        return f"本文介绍了{title}的相关内容。{intro_text}"

def main():
    """主函数，处理命令行参数并运行博客摘要生成器"""
    parser = argparse.ArgumentParser(
        description="AWS机器学习博客摘要生成器 - 基于客户信息智能筛选",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python aws_blog_summarizer_optimized.py --month 2025-08
  python aws_blog_summarizer_optimized.py --month 2025-09
  python aws_blog_summarizer_optimized.py --month 2024-12
        """
    )
    
    parser.add_argument(
        '--month', 
        type=str, 
        default='2025-08',
        help='目标月份，格式为 YYYY-MM (默认: 2025-08)'
    )
    
    parser.add_argument(
        '--pages',
        type=int,
        default=2,
        help='扫描的博客页面数量 (默认: 2)'
    )
    
    args = parser.parse_args()
    
    # 验证月份格式
    if not re.match(r'^\d{4}-\d{2}$', args.month):
        print("错误：月份格式应为 YYYY-MM，例如 2025-08")
        sys.exit(1)
    
    print(f"开始处理 {args.month} 的AWS机器学习博客...")
    
    # 创建摘要生成器实例
    summarizer = AWSBlogSummarizerOptimized(target_month=args.month)
    summarizer.max_pages = args.pages
    
    print("正在获取AWS机器学习博客列表...")
    
    # 获取所有页面的博客文章
    all_blog_posts = summarizer.get_all_blog_posts()
    
    # 筛选目标月份的文章
    target_month_posts = [post for post in all_blog_posts if summarizer.is_target_month(post['date'])]
    
    print(f"\n总共扫描了 {len(all_blog_posts)} 篇文章")
    print(f"找到 {len(target_month_posts)} 篇{summarizer.target_month}的文章\n")
    
    if target_month_posts:
        # 创建摘要文件
        output_filename = f"aws_blog_summaries_{summarizer.target_month.replace('-', '_')}_optimized.md"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(f"# AWS机器学习博客摘要 - {summarizer.target_month} (智能筛选版本)\n\n")
            f.write(f"本文档包含了AWS机器学习博客中{summarizer.target_month}发布的文章摘要。\n")
            f.write("基于客户信息智能筛选感兴趣的文章，使用AWS Knowledge MCP Server获取内容。\n\n")
            
            interested_count = 0
            total_processed = 0
            
            for i, post in enumerate(target_month_posts, 1):
                print(f"正在处理第 {i}/{len(target_month_posts)} 篇文章...")
                print(f"标题: {post['title']}")
                
                # 获取文章内容
                article_data = summarizer.get_article_content(post['url'])
                if article_data and article_data['content']:
                    print(f"内容长度: {len(article_data['content'])} 字符")
                    
                    # 评估客户兴趣度
                    print("正在评估客户兴趣度...")
                    interest_score = summarizer.assess_customer_interest(article_data['title'], article_data['content'])
                    
                    if interest_score == 1:
                        print("✓ 客户感兴趣，生成摘要...")
                        interested_count += 1
                        
                        # 生成摘要
                        summary = summarizer.generate_summary(article_data['title'], article_data['content'])
                        
                        # 写入文件
                        f.write(f"## {interested_count}. {article_data['title']}\n\n")
                        f.write(f"**发布日期：** {post['date']}\n")
                        f.write(f"**原文链接：** {post['url']}\n")
                        f.write(f"**兴趣度评分：** ✓ 感兴趣\n\n")
                        f.write(f"{summary}\n\n")
                        f.write("---\n\n")
                        
                        print("摘要生成完成\n")
                    else:
                        print("✗ 客户不感兴趣，跳过摘要生成\n")
                    
                    total_processed += 1
                else:
                    print("无法获取文章内容\n")
            
            # 添加统计信息
            f.write(f"\n## 统计信息\n\n")
            f.write(f"- 总共处理文章数：{total_processed}\n")
            f.write(f"- 客户感兴趣文章数：{interested_count}\n")
            if total_processed > 0:
                f.write(f"- 筛选效率：{interested_count/total_processed*100:.1f}%\n")
            else:
                f.write(f"- 筛选效率：0%\n")
        
        print(f"处理完成！")
        print(f"总共处理了 {total_processed} 篇文章")
        print(f"其中 {interested_count} 篇被判断为客户感兴趣")
        if total_processed > 0:
            print(f"筛选效率：{interested_count/total_processed*100:.1f}%")
        print(f"请查看 {output_filename} 文件")
    else:
        print(f"没有找到{summarizer.target_month}的博客文章")

if __name__ == "__main__":
    main()