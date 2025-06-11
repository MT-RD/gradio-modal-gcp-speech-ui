"""
Gradio interface components for the Speech-to-Text application.
"""

import gradio as gr
from typing import Optional

def process_speech_placeholder(audio_input) -> str:
    """
    Placeholder function for speech processing.
    This will be replaced with actual GCP Speech-to-Text integration.
    """
    if audio_input is None:
        return "🎤 Please upload an audio file or record some audio to transcribe."
    
    # Mock response for testing
    return f"✅ Mock Transcription: This is a placeholder response for testing the UI.\n\nAudio file received: {audio_input}\n\nThis demonstrates that the interface is working correctly and ready for integration with Google Cloud Speech-to-Text API."

def create_speech_interface() -> gr.Interface:
    """
    Create and configure the main Gradio interface for speech-to-text processing.
    
    Returns:
        gr.Interface: Configured Gradio interface
    """
    
    # Create the interface using simple string specification for compatibility
    interface = gr.Interface(
        fn=process_speech_placeholder,
        inputs="audio",  # Simple string specification
        outputs="text",  # Simple string specification
        title="🎙️ Speech-to-Text UI",
        description="Upload an audio file or record directly to get started with speech transcription."
    )
    
    return interface
