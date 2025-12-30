# Medical-MultimodelBOT

## Overview

Medical-MultimodelBOT is an AI-powered medical assistant that combines voice input, image analysis, and text-to-speech capabilities to simulate a doctor's consultation. The system allows patients to describe their symptoms verbally and optionally upload medical images (e.g., X-rays, skin conditions) for analysis. The AI provides diagnostic insights and suggestions in a natural, doctor-like manner.

## Features

- **Voice Input**: Record audio from microphone and transcribe it using Groq's Whisper model
- **Image Analysis**: Analyze medical images using Groq's Llama vision model for diagnostic insights
- **AI Doctor Response**: Generate professional medical responses based on patient input and image analysis
- **Text-to-Speech**: Convert doctor's responses to audio using Google Text-to-Speech (gTTS) or ElevenLabs
- **Web Interface**: User-friendly Gradio interface for easy interaction

## Architecture

The project consists of several key components:

- `gradio_app.py`: Main application interface using Gradio
- `brain.py`: Handles image encoding and analysis with Groq's vision API
- `voice_patient.py`: Audio recording and transcription functionality
- `voice_docter.py`: Text-to-speech conversion for doctor's responses

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Medical-MultimodelBOT.git
   cd Medical-MultimodelBOT
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file with your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here  # Optional, for ElevenLabs TTS
   ```

4. Install FFmpeg (required for audio processing):
   - On Ubuntu/Debian: `sudo apt install ffmpeg`
   - On macOS: `brew install ffmpeg`
   - On Windows: Download from https://ffmpeg.org/download.html

## Usage

Run the application:
```bash
python gradio_app.py
```

This will launch a Gradio interface where you can:
1. Record audio describing your symptoms
2. Optionally upload a medical image
3. Receive a doctor's analysis and recommendations
4. Listen to the response via text-to-speech

## Dependencies

- gradio: Web interface
- groq: AI model API for transcription and vision analysis
- speechrecognition: Audio recording
- pydub: Audio processing
- gtts: Text-to-speech (Google)
- elevenlabs: Alternative text-to-speech (optional)
- python-dotenv: Environment variable management

## Disclaimer

This is an educational project and not intended for real medical use. The AI responses are simulated and should not replace professional medical advice. Always consult qualified healthcare professionals for medical concerns.

## License

[Add your license here]