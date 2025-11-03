import openai
import os

# 设置你的 OpenAI API Key（推荐用环境变量）
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_resume(text):
    prompt = f"""你是一位资深简历优化专家。请阅读以下简历内容，并提供以下输出：
1. 简要总结（50字以内）
2. 关键词提取（5个）
3. 优化建议（3条）

简历内容如下：
{text}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
