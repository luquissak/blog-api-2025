# Introduction

Python project that uses Gen AI to analyze blog posts.

# Clone repo

```bash
git clone git@github.com:luquissak/blog-api-2025.git
```

# Enable GCP services

```bash
gcloud services enable aiplatform.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable bigquery.googleapis.com
gcloud services enable bigqueryconnection.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable containerregistry.googleapis.com
gcloud services enable generativelanguage.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable secretmanager.googleapis.com
```

# Login and load variables

```bash
gcloud auth login
gcloud config set project llm-studies
gcloud auth application-default login

get-content .env | foreach {
    $name, $value = $_.split('=')
    set-content env:\$name $value
    echo $name $value
}
gcloud config set project $Env:GOOGLE_CLOUD_PROJECT
```

# Create env

```bash
py -m venv .venv
.venv\scripts\activate
python.exe -m pip install --upgrade pip
cd app
pip freeze > src/requirements.txt
pip install -r requirements.txt
```

# Run locally

```bash
pip install -r src/requirements.txt
get-content .env | foreach {
    $name, $value = $_.split('=')
    set-content env:\$name $value
    echo $name $value
}
cd src
uvicorn main:app --reload
.venv\scripts\activate && fastapi dev app\main.py
.venv\scripts\activate && fastapi run

```

# Deploy

```bash
.venv\scripts\activate
cd src
docker build -t $Env:TAG .
docker run -dp $Env:PORT:$Env:PORT -e PORT=$Env:PORT $Env:TAG
curl http://127.0.0.1:$PORT

gcloud builds submit --tag $Env:TAG
gcloud run deploy $Env:APP --image $Env:TAG --platform managed --region $Env:GCP_REGION --allow-unauthenticated
gcloud run services describe $Env:APP --region $Env:GCP_REGION
```

# Helpers

```bash
.venv\scripts\activate && .venv\Scripts\python.exe helper\add_sec.py
.venv\scripts\activate && .venv\Scripts\python.exe helper\set_sec.py
.venv\scripts\activate && .venv\Scripts\python.exe helper\get_data_from_url.py
```

# Links & Sources

- [Build and deploy a LangChain app on Google Cloud Run](https://github.com/michaelprosario/langchain-cloudrun-lab/tree/main?tab=readme-ov-file)
- [Deploying a FastAPI app on Google Cloud Run](https://github.com/sekR4/FastAPI-on-Google-Cloud-Run/tree/main)

# Git Setup

```bash
git init
git add README.md
git commit -m "initial load"
git branch -M main
git remote add origin git@github.com:luquissak/blog-api-2025.git
git push -u origin main
```
