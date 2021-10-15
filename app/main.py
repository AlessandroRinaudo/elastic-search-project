from fastapi import FastAPI, File, UploadFile, HTTPException
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConnectionError
from typing import Optional

import uuid
import textract
import time
import os

app = FastAPI()
es = Elasticsearch([{'host': 'es-container', 'port': 9200}])

@app.post("/upload_pdf")
async def upload_file(file: UploadFile = File(...)):
    path = os.getcwd()+"/app/tmp/" + str(int(time.time())) + ".pdf"

    with open(path, "wb") as cv:
        cv.write(file.file.read())
        text = textract.process(path).decode("utf-8")
    os.remove(path)

    try:
        response = es.index(
            index = 'cv_search',
            doc_type = 'cv',
            id = uuid.uuid4(),
            body = {
                "info" : text
            }
        )
        return response

    except ConnectionError:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/search_cv")
def read_item(q: Optional[str] = None):
    try: 
        if q:
            logs = es.search(index="cv_search", query={"match": {"info": q}})   
        else:
            logs = es.search(index="cv_search", query={"match_all": {}})
        return logs['hits']['hits']
    except NotFoundError:
        return []
    except ConnectionError:
        raise HTTPException(status_code=500, detail="Internal Server Error")