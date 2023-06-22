import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/my-photo.png")

with col2:
    st.title("Akram Ali")
    content = """
    As a DevOps learner, my passion lies in understanding the principles and practices that enable organizations to deliver high-quality software at scale. Through my studies, I have developed a deep understanding of key DevOps concepts such as continuous integration and deployment, infrastructure as code, containerising applications.
I have experience working with various tools and technologies such as Git, Jenkins, Docker and Kubernetes.
As I continue to learn and grow in the DevOps space, I am committed to staying up-to-date with emerging trends and best practices. I am excited about the prospect of contributing to a team that is passionate about creating a culture of continuous improvement and delivering value to customers.
    """
    st.info(content)

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
