
# Portfolio Website


## Description
A basic functionality website to showcase your projects with their description and source code link.
- Created using **Python** with **streamlit** module to make frontend of the website.
- A **Dockerfile** included to create **Docker Image** out of it.
- A Home page to add a profile picture with an introduction about yourself.
- Contact Me page to get the emails from users about their queries.
- You can customize it according to you by changing some reference variables and can change the project list by updating data.csv file.

## Run Locally

### Run with streamlit

Install dependencies

```bash
  pip3 install --no-cache-dir -r requirements.txt
```

Run the Application

```bash
  streamlit run Home.py
```
### Run with Docker

Build Docker Image

```bash
  docker build -t portfolio:1.0 .
```

Run the Docker Image

```bash
  Docker run -p 8501:8501 portfolio:1.0
```

## Screenshots
![Screenshot 1](https://github.com/AkramExp/portfolio-website/blob/main/images/Screenshot1.png?raw=true)

![Screenshot 1](https://github.com/AkramExp/portfolio-website/blob/main/images/Screenshot2.png?raw=true)

![Screenshot 1](https://github.com/AkramExp/portfolio-website/blob/main/images/Screenshot3.png?raw=true)
