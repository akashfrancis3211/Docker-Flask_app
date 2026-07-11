# Docker Flask Application

A simple Python Flask web application containerized using Docker and deployed on an AWS EC2 instance.

---

## Features

- Python Flask application
- Dockerized using Dockerfile
- Runs inside a Docker container
- Health endpoint (/health)
- Built on AWS EC2
- Exposed using Port 5000

---

## Technologies Used

- Docker
- Python 3.12
- Flask
- AWS EC2
- Linux
- Git

---

## Project Structure

```text
docker-flask-app
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── screenshots
```

---

## Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python","app.py"]
```

---

## Build Docker Image

```bash
docker build -t akash-flask-app:v1 .
```

---

## Run Container

```bash
docker run -d \
--name flask-app \
-p 5000:5000 \
akash-flask-app:v1
```

---

## Verify Running Container

```bash
docker ps
```

---

## Application Endpoints

Home Page

```text
http://<EC2-PUBLIC-IP>:5000/
```

Health Check

```text
http://<EC2-PUBLIC-IP>:5000/health
```

---

## Screenshot

Place your browser screenshot inside:

```text
screenshots/flask-running.png
```

Then add:

```markdown
![Flask App](screenshots/flask-running.png)
```

---

## What I Learned

- Docker Images
- Docker Containers
- Dockerfile
- Python Flask
- Port Mapping
- Docker Logs
- Docker Exec
- Container Lifecycle
- Health Check
- AWS EC2 Deployment

---

Created by **Akash Francis**
