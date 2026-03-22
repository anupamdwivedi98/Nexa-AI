import streamlit as st
st.title("Welcome to the New World!")
st.subheader("Start")
st.text("come in the virtual world and gaining amazing experience")
st.write("new assign")

role = st.selectbox("your role: ",["unbelivable", "satisfying", "cluthces",])
st.write(f"you are define by {role}")

st.success("your role is defined")