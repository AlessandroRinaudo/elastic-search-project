# Projet

## Docker

```bash
docker-compose up  # Lance le projet
docker-compose build  # Mettre a jour le projet
```

## Curl test

```bash
# Le | jq sert a formater la sortie sous le format json

# Ajouter un CV
curl -X POST localhost:80 -H 'accept: application/json' -H 'Content-Type: multipart/form-data' -F 'file=@Rouquier_CV.pdf;type=application/pdf' | jq

# Lister les CV
curl -X GET localhost:9200/cv_search/cv/_search | jq
```