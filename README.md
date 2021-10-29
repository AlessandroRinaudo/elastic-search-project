# Project

## Prerequisites

docker-compose at leat in 2.0.0

## Installation/Run via Docker

```bash
docker-compose up  # Lance le projet
docker-compose build  # Mettre a jour le projet
```

Or

```bash
docker-compose  up --build
```

## Usage
To use this program, once the installation is done via Docker you have two solutions :

### Via Swagger (Strongly recommended !)

Connect to `localhost:80/docs` with your favorite browser and... You're good ! You can use the API with swagger !
If you do a search immediately after first installtion you can see few resumes aldready in Elastic Search, but you can add yours !

### Curl test


```bash
# Upload
curl -X 'POST' \
  'http://localhost/upload_cv' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@<FILENAME>;type=application/<>'

# Show all resumes, you can choose if you want to see only contact info or not
curl -X 'GET' \
  'http://localhost/search_cv?contactInfoOnly=<BOOL>' \
  -H 'accept: application/json'

# Search something in resumes
curl -X 'GET' \
  'http://localhost/search_cv?q=<QUERY>&contactInfoOnly=<BOOL>' \
  -H 'accept: application/json'
```
