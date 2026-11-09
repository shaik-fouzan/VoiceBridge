# VoiceBridge 🎙️🌉
### Bridging Languages Through AI-Powered Speech Technology

**VoiceBridge** is an AI-powered speech application built with Python and Streamlit. It helps users transform spoken language into text, translate the transcript into English, and generate natural-sounding speech using AI-powered speech technologies.

🌐 **Live Application:** https://voicebridgegit-3pd58xjb2by3zndtw6psut.streamlit.app/

---

## 🚀 Features

- 🎤 **Audio Input:** Provide speech through the application's audio input workflow.
- 📝 **Speech-to-Text:** Convert spoken audio into written text using Gnani AI Prisma STT.
- 🌍 **Language Translation:** Translate recognized text into English using Google Translator.
- 🗣️ **AI Text-to-Speech:** Generate speech from text using Gnani AI Timbre TTS.
- ✏️ **Editable Transcript:** Review and edit recognized text before generating speech.
- 🔊 **Audio Playback:** Listen to the generated speech directly in the application.
- 📥 **WAV Download:** Download generated audio for offline use.
- 🌐 **Web-Based Interface:** Access the application online without installing it locally.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Gnani AI Prisma STT | Speech recognition |
| Gnani AI Timbre TTS | Speech generation |
| Google Translator (`deep-translator`) | Text translation |
| Requests | API communication |
| Python-dotenv | Environment variable management |

## ⚙️ How It Works

1. **Input Speech:** Provide an audio recording through the application.
2. **Transcription:** The speech recognition service converts the audio into text.
3. **Translation:** Translate the recognized text into English.
4. **Text Editing:** Review and modify the transcript if necessary.
5. **Speech Generation:** Generate spoken audio from the text using Timbre TTS.
6. **Playback and Download:** Listen to the generated audio and download the WAV file.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd voicebridge
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root directory:

```env
GNANI_API_KEY=your_gnani_api_key_here
```

Replace the placeholder with your actual Gnani AI API key.

**Security note:** Never commit your `.env` file or expose your API key in your source code, screenshots, or public repository.

Ensure your `.gitignore` includes:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
```

### 5. Launch the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL that you can open in your browser.

## 🔑 API Configuration

VoiceBridge uses Gnani AI services for speech recognition and speech generation. A valid API key and access to the required services are needed to run the application locally.

Keep your API credentials private and configure them using environment variables. For deployment, add secrets through your hosting platform's secure configuration settings.

## 🧪 Testing

The deployed application has been tested successfully for the following core workflows:

- Application startup and accessibility
- Audio input
- Hindi speech transcription
- English translation
- Timbre speech generation
- WAV audio download

## 🎯 Project Objective

VoiceBridge aims to make speech-based communication more accessible by combining speech recognition, language translation, and speech synthesis in a single, easy-to-use interface.

The project demonstrates how AI APIs and Python web technologies can be integrated into a practical application that converts spoken input into translated text and generated speech.

## 🔮 Future Improvements

- Expand support for additional Indian and international languages.
- Improve transcription accuracy for different accents and recording conditions.
- Add more voice and speech-generation options.
- Enhance error handling and audio-processing performance.
- Introduce additional accessibility features.

## 🔒 Privacy and Security

- API keys should be stored securely in environment variables or deployment secrets.
- Never publish credentials or sensitive configuration files.
- Avoid uploading confidential audio recordings or personal information.

## 👨‍💻 Author

**VoiceBridge — AI-Powered Speech and Translation Application**

Built with Python, Streamlit, and Gnani AI speech technologies.

## 🌐 Try VoiceBridge

**Experience the live application here:**

👉 https://voicebridgegit-3pd58xjb2by3zndtw6psut.streamlit.app/

If you find this project interesting, consider giving the repository a ⭐ on GitHub.
