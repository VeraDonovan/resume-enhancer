# ai_utils.py
import os
import traceback
from openai import OpenAI

# 使用环境变量 OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_resume(text, max_tokens=800):
    prompt = f"""你是一位资深简历优化专家。请阅读以下简历内容，并提供以下输出：
1. 简要总结（50字以内）
2. 关键词提取（5个）
3. 优化建议（3条）

简历内容如下：
{text}
"""
    try:
        # openai v2+ 的推荐调用路径：client.chat.completions.create
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=max_tokens
        )
        # 解析返回，做健壮性判断
        choices = getattr(response, "choices", None)
        if not choices:
            raise ValueError(f"OpenAI 返回没有 choices，完整返回: {response}")
        first = choices[0]
        # 在新版 SDK 中 message 可能以对象或 dict 形式存在
        message = getattr(first, "message", None)
        if message:
            # 支持 message.content 或 message["content"]
            content = message.content if hasattr(message, "content") else message.get("content")
        else:
            # 备用字段（有些版本可能用 text）
            content = getattr(first, "text", None)
        if not content:
            raise ValueError(f"无法从 response 解析 content，完整返回: {response}")
        return content
    except Exception as e:
        # 打印完整堆栈到控制台，便于调试
        print("OpenAI 调用异常：", e)
        print(traceback.format_exc())
        # 向上抛出异常，Gradio 层会显示简短错误；你也可以返回字符串
        raise
