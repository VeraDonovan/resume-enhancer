import gradio as gr
import traceback
from ai_utils import analyze_resume



def process_resume(text):
    try:
        print("==== process_resume input length:", len(text) if text else 0)
        # 可限制输出前后片段，避免泄露 key
        print("input sample:", (text[:200] + "...") if text and len(text) > 200 else text)
        result = analyze_resume(text)
        print("==== analyze_resume returned type:", type(result))
        return result
    except Exception as e:
        tb = traceback.format_exc()
        print(tb)                  # 控制台可见完整堆栈
        return f"处理失败：{str(e)}\n详细堆栈已打印到控制台。"
demo = gr.Interface(
    fn=process_resume,
    inputs=gr.Textbox(lines=20, placeholder="粘贴你的简历文本..."),
    outputs="text",
    title="AI简历优化器",
    description="上传简历文本，获取AI生成的优化建议、关键词和总结"
)

demo.launch()
