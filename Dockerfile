FROM python
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD [ "streamlit", "run", "Home.py" ]