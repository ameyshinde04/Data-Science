import streamlit as st
import geocoder
import pandas as pd

g = geocoder.ip("me")  # Get user's location based on IP
if g.latlng:
    df = pd.DataFrame({"lat": [g.latlng[0]], "lon": [g.latlng[1]]})
    st.map(df)
else:
    st.error("Could not retrieve location")
