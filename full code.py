import streamlit as st
import numpy as np
import pandas as pd
import librosa
import tempfile

from sklearn.ensemble import RandomForestClassifier

# =========================
#  TRAIN SIMPLE MODEL
# =========================

data = pd.DataFrame({
    "voice_stress": [8,7,2,9,1,6,8,3,7,2],
    "pause_rate":   [7,6,2,8,1,5,7,2,6,1],
    "eye_shift":    [8,7,2,9,1,6,8,2,7,1],
    "label":        [1,1,0,1,0,1,1,0,1,0]
})

X = data[["voice_stress","pause_rate","eye_shift"]]
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

# =========================
#  FEATURE EXTRACTION
# =========================

def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)

    voice_stress = np.std(y) * 100
    pause_rate = np.sum(np.abs(y) < 0.02) / len(y) * 10
    eye_shift = voice_stress * 0.7  # fake but ok for demo

    return voice_stress, pause_rate, eye_shift

# =========================
#  EXPLANATION
# =========================

def explain(vs, pr, es):
    reasons = []

    if vs > 6:
        reasons.append("High voice stress detected")
    if pr > 6:
        reasons.append("Frequent pauses detected")
    if es > 6:
        reasons.append("Irregular speech pattern detected")

    return reasons

# =========================
#  UI
# =========================

st.set_page_config(page_title="Lie Detection AI", layout="centered")

st.title("🎤 AI Lie Detection System")
st.write("Upload or record your voice (max ~2 minutes) to detect truth vs lie")

tab1, tab2 = st.tabs(["📁 Upload Audio", "🎙️ Record Audio"])

audio_bytes = None

with tab1:
    uploaded_file = st.file_uploader("Upload WAV audio", type=["wav"])
    if uploaded_file is not None:
        audio_bytes = uploaded_file.read()
        st.audio(audio_bytes)

with tab2:
    st.info("Click the microphone, speak for up to 2 minutes, then click again to stop.")
    recorded_audio = st.audio_input("Record your voice")
    if recorded_audio is not None:
        audio_bytes = recorded_audio.read()
        st.audio(audio_bytes)

if audio_bytes is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        path = tmp.name

    # extract features
    vs, pr, es = extract_features(path)

    st.subheader("📊 Features")
    st.write({
        "voice_stress": vs,
        "pause_rate": pr,
        "eye_shift": es
    })

    # prediction
    pred = model.predict([[vs, pr, es]])[0]

    decision = "🔴 LIE" if pred == 1 else "🟢 TRUTH"

    st.subheader("🧠 Decision")
    st.title(decision)

    # explanation
    st.subheader("💡 AI Explanation")

    reasons = explain(vs, pr, es)
    if reasons:
        for r in reasons:
            st.write("•", r)
    else:
        st.write("No strong stress indicators detected.")
