# Project

## Prerequisites

docker-compose at least in 2.0.0

## Installation/Run via Docker

```bash
docker-compose up  # Lance le projet
docker-compose build  # Mettre a jour le projet
```

Or

```bash
docker-compose  up --build
```

## Env var
If you want to set the project in prod mode you can switch the environment variable on True in docker-compose.yml.
Env path : `services.api.environment.PRODENV`

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

## Tests
To run tests, execute the following command :
```sh
docker exec -it api-container  /bin/bash -c "cd app/tests && pytest"
```
