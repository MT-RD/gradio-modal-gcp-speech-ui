"""
Simple working Gradio interface for testing.
"""

import gradio as gr

def simple_text_function(text_input):
    """Simple text processing function for testing."""
    if not text_input:
        return "Please enter some text!"
    return f"You entered: {text_input}"

# Create a simple interface that should work with any Gradio version
demo = gr.Interface(
    fn=simple_text_function,
    inputs="text",
    outputs="text",
    title="🧪 Simple Test Interface",
    description="A simple test to verify Gradio is working."
)

if __name__ == "__main__":
    print("🧪 Testing simple Gradio interface...")
    demo.launch(share=True)
