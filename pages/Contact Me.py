import streamlit as st

st.title('Contact Me')

with st.form(key='email_form'):
    email = st.text_input("Enter Your Email")
    message = st.text_area("Enter Your Message")
    button = st.form_submit_button("SUBMIT")
