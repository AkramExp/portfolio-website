import streamlit as st
from send_email import sendMail

st.title('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input("Enter Your Email")
    raw_message = st.text_area("Enter Your Message")
    message = f"""\
Subject: An Email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("SUBMIT")
    if button:
        sendMail(message)
