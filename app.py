
import os
import requests
import streamlit as st
from dotenv import load_dotenv
from deep_translator import GoogleTranslator

# =========================================================
# CONFIGURATION
# =========================================================

load_dotenv()
API_KEY = os.getenv("GNANI_API_KEY")

STT_URL = "https://api.vachana.ai/stt/v3"
TTS_URL = "https://api.vachana.ai/api/v1/tts/inference"

st.set_page_config(
    page_title="VoiceBridge | AI Speech Studio",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# CUSTOM UI
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    .stApp {
        background:
          radial-gradient(ellipse at 8% 0%, rgba(42,105,177,.24), transparent 42%),
          radial-gradient(ellipse at 95% 12%, rgba(119,72,200,.20), transparent 35%),
          #080d1b;
        color: #eaf2ff;
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] { background: transparent; }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #f3f7ff !important;
    }

    p, label, .stMarkdown { color: #d8e3f5; }

    .hero {
        padding: 1.8rem 2rem;
        border-radius: 24px;
        border: 1px solid rgba(146,178,226,.22);
        background: linear-gradient(125deg, rgba(22,37,67,.96), rgba(18,24,48,.90));
        box-shadow: 0 18px 60px rgba(0,0,0,.24);
        margin-bottom: 1.4rem;
    }

    .eyebrow {
        color: #42e8c4;
        text-transform: uppercase;
        letter-spacing: .15em;
        font-size: .75rem;
        font-weight: 700;
        margin-bottom: .65rem;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2rem, 5vw, 3.4rem);
        line-height: 1.1;
        font-weight: 700;
        color: #f7faff;
    }

    .hero-sub {
        color: #b6c7e2;
        font-size: 1.05rem;
        margin-top: .8rem;
    }

    .pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: .5rem;
        margin-top: 1rem;
    }

    .pill {
        border: 1px solid rgba(117,230,211,.28);
        background: rgba(66,232,196,.08);
        color: #b8fff0;
        border-radius: 99px;
        padding: .4rem .75rem;
        font-size: .82rem;
    }

    .section-card {
        border: 1px solid rgba(146,178,226,.18);
        background: rgba(17,27,49,.78);
        border-radius: 20px;
        padding: 1.15rem 1.25rem;
        margin-bottom: .8rem;
    }

    .step-label {
        color: #42e8c4;
        font-size: .75rem;
        text-transform: uppercase;
        letter-spacing: .12em;
        font-weight: 700;
    }

    .step-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.25rem;
        color: #f3f7ff;
        font-weight: 600;
        margin: .3rem 0;
    }

    .small-muted {
        color: #a8b8d4;
        font-size: .9rem;
    }

    div[data-testid="stFileUploader"] section,
    div[data-testid="stTextArea"] textarea,
    div[data-testid="stSelectbox"] > div > div {
        background: #0b1222 !important;
        border-color: rgba(146,178,226,.28) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }

    div.stButton > button,
    div[data-testid="stDownloadButton"] button {
        border-radius: 12px !important;
        border: 1px solid #55e6cf !important;
        background: linear-gradient(100deg, #126e70, #167f78) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        min-height: 2.8rem;
        box-shadow: 0 4px 14px rgba(0,0,0,.18);
    }

    div.stButton > button p,
    div.stButton > button span,
    div[data-testid="stDownloadButton"] button p,
    div[data-testid="stDownloadButton"] button span {
        color: #ffffff !important;
    }

    div.stButton > button:hover,
    div[data-testid="stDownloadButton"] button:hover {
        background: linear-gradient(100deg, #0d5b60, #116b65) !important;
        border-color: #8ff7e5 !important;
    }

    div[data-testid="stRadio"] label { color: #eaf2ff !important; }

    .footer {
        text-align: center;
        color: #a8b8d4;
        font-size: .82rem;
        padding-top: 1.5rem;
    }

    hr { border-color: rgba(146,178,226,.15) !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">✦ AI SPEECH STUDIO · POWERED BY GNANI AI</div>
      <div class="hero-title">VoiceBridge<span style="color:#42e8c4">.</span></div>
      <div class="hero-sub">
        Turn your voice into editable text, translate your message,
        and transform it into speech using AI.
      </div>
      <div class="pill-row">
        <span class="pill">◉ Prisma · Speech to Text</span>
        <span class="pill">🌐 Multilingual Translation</span>
        <span class="pill">♫ Timbre · Text to Speech</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if not API_KEY:
    st.error(
        "GNANI_API_KEY is missing. Configure it in your local .env "
        "file or your Streamlit Cloud app secrets."
    )
    st.stop()

# =========================================================
# SESSION STATE
# =========================================================

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "generated_audio" not in st.session_state:
    st.session_state.generated_audio = None

# =========================================================
# LANGUAGES
# =========================================================

language_options = {
    "ಕನ್ನಡ · Kannada": "kn-IN",
    "తెలుగు · Telugu": "te-IN",
    "English": "en-IN",
    "हिन्दी · Hindi": "hi-IN",
    "Hinglish (Hindi in English letters)": "hi-IN",
}

translation_targets = {
    "ಕನ್ನಡ · Kannada": "kn",
    "తెలుగు · Telugu": "te",
    "English": "en",
    "हिन्दी · Hindi": "hi",
    "Hinglish (Hindi in English letters)": "hi",
}

language_label = st.selectbox(
    "Translation and speech output language",
    list(language_options.keys()),
    index=2,
    help="Your audio is transcribed first and then translated into this language.",
)

language_code = language_options[language_label]
translation_target = translation_targets[language_label]

if language_label == "Hinglish (Hindi in English letters)":
    st.info(
        "This option currently translates to Hindi in Devanagari. "
        "Romanized Hinglish is not implemented yet."
    )

st.divider()

# =========================================================
# TRANSLATION
# =========================================================


def translate_text(text, target_language):
    """Translate text using MyMemory first, then Google as a fallback."""
    if not text or not text.strip():
        raise ValueError("No text was received for translation.")

    text = text.strip()

    # Detect common Indian languages from their writing systems.
    if any("\u0900" <= char <= "\u097f" for char in text):
        source_language = "hi"
    elif any("\u0c00" <= char <= "\u0c7f" for char in text):
        source_language = "te"
    elif any("\u0c80" <= char <= "\u0cff" for char in text):
        source_language = "kn"
    else:
        source_language = "en"

    # Try MyMemory first to avoid relying only on Google Translate.
    try:
        response = requests.get(
            "https://api.mymemory.translated.net/get",
            params={
                "q": text[:4500],
                "langpair": f"{source_language}|{target_language}",
            },
            timeout=15,
        )
        response.raise_for_status()
        result = response.json()

        translated = (
            result.get("responseData", {}).get("translatedText", "").strip()
        )

        if result.get("responseStatus") == 200 and translated:
            return translated

    except (requests.RequestException, ValueError, AttributeError):
        pass

    # Fallback to Google if MyMemory is unavailable.
    try:
        return GoogleTranslator(
            source=source_language,
            target=target_language,
        ).translate(text)

    except Exception as exc:
        raise RuntimeError(
            "Both translation services failed or are temporarily unavailable. "
            "Please wait and try again."
        ) from exc


# =========================================================
# WORKSPACE
# =========================================================

left, right = st.columns([1, 1], gap="large")

audio_file = None
audio_name = None
audio_mime = None

# =========================================================
# LEFT: AUDIO INPUT AND TRANSCRIPTION
# =========================================================

with left:

    st.markdown(
        """
        <div class="section-card">
          <div class="step-label">STEP 01 · INPUT</div>
          <div class="step-title">Capture your voice</div>
          <div class="small-muted">
            Record with your microphone or upload an audio file.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    input_mode = st.radio(
        "Choose your audio input",
        ["🎙️ Record with microphone", "📁 Upload an audio file"],
        horizontal=True,
    )

    if input_mode == "🎙️ Record with microphone":
        recording = st.audio_input("Record your voice")

        if recording is not None:
            audio_file = recording
            audio_name = "microphone_recording.wav"
            audio_mime = "audio/wav"

            st.success("Your recording is ready!")
            st.audio(recording, format="audio/wav")

    else:
        uploaded_audio = st.file_uploader(
            "Upload your audio recording",
            type=["wav", "mp3", "m4a", "ogg", "flac"],
            help="Gnani's documented STT formats include WAV, MP3, FLAC, OGG, and M4A.",
        )

        if uploaded_audio is not None:
            audio_file = uploaded_audio
            audio_name = uploaded_audio.name
            audio_mime = uploaded_audio.type or "application/octet-stream"

            st.success("Audio file selected!")
            st.audio(uploaded_audio)

    st.caption("Tip: Speak clearly and minimize background noise.")

    if st.button(
        "✨ Transcribe and translate",
        type="primary",
        use_container_width=True,
    ):

        if audio_file is None:
            st.warning("Please record or upload an audio file first.")

        else:
            try:
                with st.spinner("Gnani Prisma is transcribing your audio..."):

                    response = requests.post(
                        STT_URL,
                        headers={"X-API-Key-ID": API_KEY},
                        files={
                            "audio_file": (
                                audio_name,
                                audio_file.getvalue(),
                                audio_mime,
                            )
                        },
                        data={
                            "model": "prisma-v3.0",
                            "language_code": "indic-auto",
                            "format": "transcribe",
                        },
                        timeout=90,
                    )

                if not response.ok:
                    st.error(
                        f"Prisma API request failed: HTTP {response.status_code}"
                    )
                    st.code(response.text[:3000])
                    st.stop()

                try:
                    result = response.json()
                except ValueError:
                    st.error("Prisma returned a response that was not valid JSON.")
                    st.code(response.text[:3000])
                    st.stop()

                original_transcript = result.get("transcript")

                if not original_transcript:
                    st.error("Prisma did not return a transcript.")
                    st.json(result)
                    st.stop()

                st.session_state.generated_audio = None

                st.success("Transcription completed!")

                with st.expander("View original transcription"):
                    st.write(original_transcript)

                with st.spinner(f"Translating into {language_label}..."):
                    translated_text = translate_text(
                        original_transcript,
                        translation_target,
                    )

                if not translated_text:
                    st.error("Translation returned empty text.")
                else:
                    st.session_state.transcript = translated_text
                    st.success(
                        f"Translation into {language_label} completed!"
                    )

            except requests.Timeout:
                st.error("Prisma timed out. Try a shorter audio recording.")

            except requests.RequestException as exc:
                st.error(f"Could not connect to Prisma: {exc}")

            except Exception as exc:
                st.error(
                    "Translation failed. Check your internet connection "
                    "and the translation service."
                )
                st.caption(f"Details: {exc}")

# =========================================================
# RIGHT: EDIT TRANSCRIPT AND GENERATE SPEECH
# =========================================================

with right:

    st.markdown(
        """
        <div class="section-card">
          <div class="step-label">STEP 02 · REVIEW</div>
          <div class="step-title">Make it yours</div>
          <div class="small-muted">
            Review and edit your translated text before generating speech.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    edited_text = st.text_area(
        "Translated transcript · editable",
        key="transcript",
        height=250,
        placeholder="Your translated text will appear here...",
    )

    st.caption(
        f"{len(edited_text.strip())} characters · Edit before generating speech."
    )

    if st.button(
        "♫ Generate speech with Timbre",
        use_container_width=True,
    ):

        if not edited_text.strip():
            st.warning("Please transcribe audio or enter text first.")

        else:
            payload = {
                "text": edited_text.strip(),
                "model": "timbre-v2.5",
                "voice": "Kaveri",
                "language": language_code,
                "audio_config": {
                    "encoding": "linear_pcm",
                    "container": "wav",
                    "num_channels": 1,
                    "sample_rate": 48000,
                    "sample_width": 2,
                },
            }

            try:
                with st.spinner("Gnani Timbre is generating your speech..."):
                    response = requests.post(
                        TTS_URL,
                        headers={
                            "X-API-Key-ID": API_KEY,
                            "Content-Type": "application/json",
                        },
                        json=payload,
                        timeout=90,
                    )

                if not response.ok:
                    st.error(
                        f"Timbre API request failed: HTTP {response.status_code}"
                    )
                    st.code(response.text[:3000])

                elif not response.content:
                    st.error("Timbre returned an empty audio response.")

                else:
                    st.session_state.generated_audio = response.content
                    st.success("Speech generated successfully!")

            except requests.Timeout:
                st.error("Timbre timed out. Please try again.")

            except requests.RequestException as exc:
                st.error(f"Could not connect to Timbre: {exc}")

# =========================================================
# AUDIO OUTPUT
# =========================================================

if st.session_state.generated_audio:

    st.divider()

    st.markdown(
        """
        <div class="section-card">
          <div class="step-label">STEP 03 · OUTPUT</div>
          <div class="step-title">Your speech is ready!</div>
          <div class="small-muted">
            Listen to your generated audio or download it.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.audio(st.session_state.generated_audio, format="audio/wav")

    st.download_button(
        "⬇️ Download spoken audio (.wav)",
        data=st.session_state.generated_audio,
        file_name="voicebridge_output.wav",
        mime="audio/wav",
        use_container_width=True,
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
      VoiceBridge · Streamlit + Gnani AI Prisma
      + Google Translate + Gnani AI Timbre
      <br>
      Review your transcript before relying on generated speech.
    </div>
    """,
    unsafe_allow_html=True,
)
