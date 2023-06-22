FROM python
WORKDIR /app
COPY . .
RUN pip3 install requirements.txt
EXPOSE 8501
CMD [ "streamlit", "run", "Home.py" ]