import streamlit as st
import os
from audio_recorder_streamlit import audio_recorder
from openai import OpenAI as OAI
from dotenv import load_dotenv
from langchain_helper import output_func

load_dotenv()

openaikey = os.getenv("OPENAI_API_KEY")

client = OAI(api_key=openaikey)


st.title("Speak To Site 🗣️🗣️🗣️")

if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:

    st.markdown("# Speak Your Imagination 🌟", unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    recorded_audio = audio_recorder(
        icon_size='5x', neutral_color="white", recording_color="red", text="")
    if recorded_audio is not None:
        audio_file = "a.mp3"
        with open(audio_file, "wb") as f:
            f.write(recorded_audio)
audio_file = open("a.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)
st.markdown(
    f"<h4 style='background-color: #0d0d0d; color: white; margin-top: 20vh; border-bottom: 1px solid #808080; padding: 2.5rem 2.5rem; opacity: 0.7; border-radius: 16px; margin-bottom:5vh; '>👤 - {transcription}</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='background-color: #0d0d0d; color: white; border-bottom: 1px solid #808080; padding: 2.5rem 2.5rem; opacity: 0.7; border-radius: 16px; margin-bottom:5vh; '>🤖 - Your website is cooking 🔥🔥🔥</h4>",
            unsafe_allow_html=True)

# The INCREDIENTSSSS
# output_func(transcription)

st.markdown("<h4 style='background-color: #0d0d0d; color: white; border-bottom: 1px solid #808080; padding: 2.5rem 2.5rem; opacity: 0.7; border-radius: 16px; margin-bottom:5vh; '>🤖 - yupp 😋 done: go visit it here 👉 <a href='http://127.0.0.1:5500/saturday-hack-night-template/output.html' style='color: #4CAF50;'>link</a></h4>", unsafe_allow_html=True)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

#   st.session_state.messages.append({"role": "assistant", "content": "I am a robot, I don't have feelings."})
