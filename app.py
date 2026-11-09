
import os
import requests
import streamlit as st
from dotenv import load_dotenv

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
# CUSTOM UI DESIGN
# =========================================================

st.markdown(
    """
    <style>
    @import url(
      'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
    );

    .stApp {
        background:
          radial-gradient(ellipse at 8% 0%,
            rgba(42,105,177,.24), transparent 42%),
          radial-gradient(ellipse at 95% 12%,
            rgba(119,72,200,.20), transparent 35%),
          #080d1b;
        color: #eaf2ff;
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #f3f7ff !important;
    }

    p, label, .stMarkdown {
        color: #d8e3f5;
    }

    .hero {
        padding: 1.8rem 2rem;
        border-radius: 24px;
        border: 1px solid rgba(146,178,226,.22);
        background: linear-gradient(
            125deg, rgba(22,37,67,.96),
            rgba(18,24,48,.90)
        );
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

    /* High-contrast action buttons */
    div.stButton > button,
    div[data-testid="stDownloadButton"] button {
        border-radius: 12px !important;
        border: 1px solid #55e6cf !important;
        background: linear-gradient(
            100deg, #126e70, #167f78
        ) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        min-height: 2.8rem;
        box-shadow: 0 4px 14px rgba(0,0,0,.18);
        transition: .15s ease;
    }

    div.stButton > button p,
    div.stButton > button span,
    div[data-testid="stDownloadButton"] button p,
    div[data-testid="stDownloadButton"] button span {
        color: #ffffff !important;
    }

    div.stButton > button:hover,
    div[data-testid="stDownloadButton"] button:hover {
        background: linear-gradient(
            100deg, #0d5b60, #116b65
        ) !important;
        border-color: #8ff7e5 !important;
        color: #ffffff !important;
        transform: translateY(-1px);
    }

    div.stButton > button:focus,
    div[data-testid="stDownloadButton"] button:focus {
        outline: 2px solid #a5fff0 !important;
        outline-offset: 3px;
    }

    div[data-testid="stRadio"] label {
        color: #eaf2ff !important;
    }

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    hr {
        border-color: rgba(146,178,226,.15) !important;
    }

    .footer {
        text-align: center;
        color: #a8b8d4;
        font-size: .82rem;
        padding-top: 1.5rem;
    }
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
      <div class="eyebrow">
        ✦ AI SPEECH STUDIO · POWERED BY GNANI AI
      </div>
      <div class="hero-title">
        VoiceBridge<span style="color:#42e8c4">.</span>
      </div>
      <div class="hero-sub">
        Turn your voice into editable text, review your message,
        and transform it into speech using AI.
      </div>
      <div class="pill-row">
        <span class="pill">◉ Prisma · Speech to Text</span>
        <span class="pill">♫ Timbre · Text to Speech</span>
        <span class="pill">Indian languages · Multilingual speech</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if not API_KEY:
    st.error(
        "GNANI_API_KEY is missing. Add it to your private .env file."
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
# LANGUAGE SELECTION
# =========================================================

language_options = {
    "ಕನ್ನಡ · Kannada": "kn-IN",
    "తెలుగు · Telugu": "te-IN",
    "English": "en-IN",
    "हिन्दी · Hindi": "hi-IN",
    "Hinglish (Hindi in English letters)": "hi-IN",
}

language_label = st.selectbox(
    "Speech output language",
    list(language_options.keys()),
    index=1,
    help=(
        "Select the language for Timbre speech output. "
        "Prisma uses automatic language detection for transcription."
    ),
)

language_code = language_options[language_label]

st.divider()

# =========================================================
# TWO-COLUMN WORKSPACE
# =========================================================

left, right = st.columns([1, 1], gap="large")

# These variables identify the audio selected during this run.
audio_file = None
audio_name = None
audio_mime = None

# =========================================================
# LEFT COLUMN: RECORD OR UPLOAD
# =========================================================

with left:

    st.markdown(
        """
        <div class="section-card">
          <div class="step-label">STEP 01 · INPUT</div>
          <div class="step-title">Capture your voice</div>
          <div class="small-muted">
            Record directly with your microphone or upload
            an existing audio file.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    input_mode = st.radio(
        "Choose your audio input",
        [
            "🎙️ Record with microphone",
            "📁 Upload an audio file",
        ],
        horizontal=True,
    )

    if input_mode == "🎙️ Record with microphone":

        recording = st.audio_input(
            "Record your voice",
            help=(
                "Allow microphone access in your browser. "
                "Record your voice and stop when finished."
            ),
        )

        if recording is not None:
            audio_file = recording
            audio_name = "microphone_recording.wav"
            audio_mime = "audio/wav"

            st.success("Your recording is ready!")
            st.audio(recording, format="audio/wav")

    else:

        uploaded_audio = st.file_uploader(
            "Upload your audio recording",
            type=[
                "wav",
                "mp3",
                "m4a",
                "ogg",
                "flac",
                "aac",
            ],
            help=(
                "Supported file types: WAV, MP3, M4A, "
                "OGG, FLAC, and AAC."
            ),
        )

        if uploaded_audio is not None:
            audio_file = uploaded_audio
            audio_name = uploaded_audio.name
            audio_mime = (
                uploaded_audio.type or "application/octet-stream"
            )

            st.success("Audio file selected!")
            st.audio(uploaded_audio)

    st.caption(
        "Tip: Speak clearly and minimize background noise."
    )

    # =====================================================
    # PRISMA STT
    # =====================================================

    if st.button(
        "✨  Transcribe with Prisma",
        type="primary",
        use_container_width=True,
    ):

        if audio_file is None:
            st.warning(
                "Please record your voice or upload an audio file first."
            )

        else:
            try:
                with st.spinner(
                    "Gnani Prisma is transcribing your voice..."
                ):

                    response = requests.post(
                        STT_URL,
                        headers={
                            "X-API-Key-ID": API_KEY,
                        },
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
                        },
                        timeout=90,
                    )

                    response.raise_for_status()
                    result = response.json()

                    transcript = result.get("transcript")

                    if transcript:
                        st.session_state.transcript = transcript
                        st.session_state.generated_audio = None

                        st.success(
                            "Transcription completed successfully!"
                        )

                    else:
                        st.error(
                            "No transcript returned. "
                            "Try a clearer or shorter recording."
                        )

            except requests.Timeout:
                st.error(
                    "Prisma took too long to respond. "
                    "Please try again."
                )

            except requests.HTTPError as exc:
                status = (
                    exc.response.status_code
                    if exc.response is not None
                    else "unknown"
                )

                st.error(
                    f"Prisma API request failed: HTTP {status}. "
                    "Check your API access and audio format."
                )

            except requests.RequestException:
                st.error(
                    "Could not connect to Gnani AI. "
                    "Check your internet connection."
                )

            except ValueError:
                st.error(
                    "Prisma returned an unexpected response."
                )

# =========================================================
# RIGHT COLUMN: REVIEW TRANSCRIPT
# =========================================================

with right:

    st.markdown(
        """
        <div class="section-card">
          <div class="step-label">STEP 02 · REVIEW</div>
          <div class="step-title">Make it yours</div>
          <div class="small-muted">
            Review your transcription and correct any mistakes
            before generating speech.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    edited_text = st.text_area(
        "Transcript · editable",
        key="transcript",
        height=250,
        placeholder="Your transcript will appear here...",
    )

    st.caption(
        f"{len(edited_text.strip())} characters · "
        "Edit the text before generating speech."
    )

    # =====================================================
    # TIMBRE TTS
    # =====================================================

    if st.button(
        "♫  Speak reviewed message with Timbre",
        use_container_width=True,
    ):

        if not edited_text.strip():
            st.warning(
                "Please transcribe or enter some text first."
            )

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
                with st.spinner(
                    "Gnani Timbre is generating your speech..."
                ):

                    response = requests.post(
                        TTS_URL,
                        headers={
                            "X-API-Key-ID": API_KEY,
                            "Content-Type": "application/json",
                        },
                        json=payload,
                        timeout=90,
                    )

                    response.raise_for_status()

                    st.session_state.generated_audio = (
                        response.content
                    )

                    st.success("Speech generated successfully!")

            except requests.Timeout:
                st.error(
                    "Timbre took too long to respond. "
                    "Please try again."
                )

            except requests.HTTPError as exc:
                status = (
                    exc.response.status_code
                    if exc.response is not None
                    else "unknown"
                )

                st.error(
                    f"Timbre API request failed: HTTP {status}. "
                    "Check the selected language and API access."
                )

            except requests.RequestException:
                st.error(
                    "Could not connect to Gnani AI. "
                    "Check your internet connection."
                )

# =========================================================
# GENERATED AUDIO OUTPUT
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

    st.audio(
        st.session_state.generated_audio,
        format="audio/wav",
    )

    st.download_button(
        "⬇️  Download spoken audio (.wav)",
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
      VoiceBridge · Streamlit + Gnani AI Prisma + Gnani AI Timbre
      <br>
      Review your transcript before relying on the generated speech.
    </div>
    """,
    unsafe_allow_html=True,
)
