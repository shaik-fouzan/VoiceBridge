# 🎙️ VoiceBridge — Telugu Speech to Text & Text to Speech

VoiceBridge is a Python-based speech application built with Streamlit that helps users convert Telugu speech into text and transform written text back into speech. Powered by Gnani AI's Prisma Speech-to-Text (STT) and Timbre Text-to-Speech (TTS), it provides a simple and accessible way to work with spoken language.

## ✨ Features

- 🎧 **Speech-to-Text:** Transcribe uploaded Telugu audio into text.
- ✍️ **Editable Transcription:** Review and edit the generated transcript.
- 🔊 **Text-to-Speech:** Generate speech audio from written or edited text.
- ▶️ **Audio Playback:** Listen to generated speech directly in the app.
- 📥 **Audio Download:** Download generated speech for later use.
- 🌐 **Web Interface:** Simple, interactive interface powered by Streamlit.
- 🔐 **API Key Protection:** Keep API credentials in environment variables rather than hardcoding them in the source code.

## 🛠️ Tech Stack

- **Python** — Application logic
- **Streamlit** — Web interface
- **Gnani AI Prisma** — Speech-to-Text
- **Gnani AI Timbre** — Text-to-Speech
- **Git & GitHub** — Version control and project hosting

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by your dependencies
- A Gnani AI API key with access to the required speech services
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/shaik-fouzan/VoiceBridge.git
cd VoiceBridge
```


### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root and add your Gnani AI API key using the environment variable name expected by `app.py`.

Example:

```env
GNANI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key. Never commit your `.env` file or publish your API key on GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL that you can open in your browser.

## 📖 How to Use

1. Open VoiceBridge in your browser.
2. Upload a short Telugu audio sample.
3. Generate a speech transcription.
4. Review and edit the transcript if needed.
5. Convert the text into speech.
6. Play and download the generated audio.

## 🎯 Project Goal

VoiceBridge aims to make speech and text conversion easier through a straightforward interface, helping users interact with Telugu audio and written content more conveniently.

## 🔒 Security

- Keep API keys private.
- Store secrets in environment variables or the hosting platform's secret manager.
- Never commit `.env`, credentials, or private configuration files.
- If an API key is accidentally exposed, revoke it and generate a replacement.

## 🌍 Deployment

VoiceBridge can be deployed to a compatible hosting platform that supports Streamlit and the required Python dependencies. Configure the necessary API key through the platform's secrets or environment-variable settings before launching the application.

## 👨‍💻 Author

**Shaik Fouzan**

## 📄 License

Add a license if you intend to distribute or allow others to reuse this project. Until a license is added, standard copyright restrictions apply.
