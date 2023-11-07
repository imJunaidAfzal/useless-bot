import gradio as gr
from bot import openai_bot

with gr.Blocks() as demo:
    with gr.Blocks():
        with gr.Row():
            gr.Markdown("# Useless Bot")
    
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        msg.submit(openai_bot, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(debug=True, share=True)
