import gradio as gr
from ai_utils import analyze_resume

def process_resume(text):
    return analyze_resume(text)

demo = gr.Interface(
    fn=process_resume,
    inputs=gr.Textbox(lines=20, placeholder="粘贴你的简历文本..."),
    outputs="text",
    title="AI简历优化器",
    description="上传简历文本，获取AI生成的优化建议、关键词和总结"
)

demo.launch()
