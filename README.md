# Projet

## Docker

```
docker build -t myimage .
docker run --name mycontainer -p 80:80 myimage
```

## Curl test

```bash
curl -X 'POST' 'http://0.0.0.0:80/'-H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@Rouquier_CV.pdf;type=application/pdf'
```