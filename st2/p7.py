import streamlit as st



st.markdown("# Page 7🎉")


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)