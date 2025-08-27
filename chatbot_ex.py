import streamlit as st

st.title("Chatbot Example")

with st.chat_message("user"):
    st.write("Hello ji")

with st.chat_message("assistant"):
    st.write("Namaste! Kaise ho?")  # AI response
