

#To run streamlit use command -> streamlit run stream.py

import streamlit as st
import pandas as pd
import numpy as np
import time
 
st.title("5 Minutes Engineering(Title)")
st.header("Machine Learning, Simplified(Header)")
st.subheader("AI & Data Science in Small Bites(Sub-Header)")
st.write("Quick ML tutorials with interactive visualizations.(Text)")
st.markdown("Experiment with AI models in real-time using Streamlit.(Markdown)")
st.caption("Bringing ML concepts to life with Streamlit.(Caption)")

st.image("bot2.jpg",width=350)
st.audio("sample-3s.mp3")
st.video("Tokyo_night.mp4")

st.checkbox('Checkbox')
st.button('Click button')
st.radio('Pick your city(Radio)',['Pune','Mumbai','Delhi','Surat'])
st.selectbox('Pick your city(SelectBox)',['Pune','Mumbai','Delhi','Surat'])
st.multiselect('Pick favourite sports(Multiselect)',['cricket', 'football', 'basketball'])
st.select_slider('Give a Remark(Select slider)', ['Bad', 'Good', 'Excellent','Outstanding'])
st.slider('Your Marks(Slider)', 0,100)

on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")

number = st.number_input("Insert a number")
st.write("The current number is ", number)

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)

t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)

st.number_input('Enter your marks', 0,100)
st.text_input('Enter Text')
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description')               #Imp 
st.file_uploader('Upload File')
st.color_picker('Choose a color')

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("5 Minutes Engineering")
st.sidebar.image("streamlit_logo.png",width=200)

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)

#np.random.randn(10, 5) -> creates a matrix of 10 rows and 5 columns which is then converted to a pandas dataframe by pd.DataFrame

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
st.table(df)

col1, col2, col3 = st.columns(3)               
col1.metric("Temperature", "70 °F", "1.2 °F")     #metric(label, value, delta)
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

col1, col2, col3= st.columns(3)
with col2:
    st.image("bot2.jpg",width=200)

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    
    

with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)
st.button("Rerun")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

df = pd.DataFrame({
    "lat": [40.7128],  # Valid latitude
    "lon": [-74.0060]  # Valid longitude
})
st.map(df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)

with st.chat_message("user"):
    st.write("Hello ji")





