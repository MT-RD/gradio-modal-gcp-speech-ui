"""
Gradio interface components for the Speech-to-Text application.
"""

import gradio as gr
from typing import Optional

def process_speech_placeholder(audio_input: Optional[str] = None) -> str:
    """
    Placeholder function for speech processing.
    This will be replaced with actual GCP Speech-to-Text integration.
    """
    if audio_input is None:
        return "🎤 Please provide an audio file or record some audio to transcribe."
    
    # Mock response for testing
    return f"✅ Mock Transcription: This is a placeholder response for testing the UI. Audio file: {audio_input}"

def create_speech_interface() -> gr.Interface:
    """
    Create and configure the main Gradio interface for speech-to-text processing.
    
    Returns:
        gr.Interface: Configured Gradio interface
    """
    
    # Create the interface
    interface = gr.Interface(
        fn=process_speech_placeholder,
        inputs=[
            gr.Audio(
                label="🎵 Audio Input", 
                type="filepath"
            )
        ],
        outputs=[
            gr.Textbox(
                label="📝 Transcription Result",
                placeholder="Your transcribed text will appear here...",
                lines=5,
                show_copy_button=True
            )
        ],
        title="🎙️ Speech-to-Text UI",
        description="""
        ### Welcome to the Speech-to-Text Application!
        
        Upload an audio file or record directly to get started with speech transcription.
        
        **Supported formats:** WAV, MP3, M4A, OGG, FLAC
        """,
        theme=gr.themes.Soft(),
        examples=[
            # We'll add example audio files later
        ],
        cache_examples=False,
        flagging_mode="never"
    )
    
    return interface
