import streamlit as st

# sidebar
st.sidebar.markdown("Clicked Page 1")
st.sidebar.markdown("Side Menu")
st.sidebar.button("Click")
st.sidebar.radio("성별", ["여자","남자"])
# page
st.title("Page 1")
st.markdown("Mark Down")
st.header("Header")
st.subheader("Subheader")
st.caption("Caption")
st.code("""
        def func():
            print("OK")
        def func2():
            print("OK2")   
""",language="python")