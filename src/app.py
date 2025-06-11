#!/usr/bin/env python3
"""
Main entry point for the Gradio Speech-to-Text UI application.
"""

import os
import sys
from pathlib import Path

# Add the src directory to Python path for imports
src_dir = Path(__file__).parent
sys.path.insert(0, str(src_dir))

from gradio_app.interface import create_speech_interface

def main():
    """Main function to run the Gradio application."""
    print("🚀 Starting Gradio Speech-to-Text UI...")
    
    # Create the Gradio interface
    interface = create_speech_interface()
    
    # Launch the application
    interface.launch(
        server_name="0.0.0.0",  # Allow external connections
        server_port=7860,       # Default Gradio port
        share=False,            # Set to True for public sharing
        debug=True,             # Enable debug mode
        show_error=True         # Show detailed error messages
    )

if __name__ == "__main__":
    main()
