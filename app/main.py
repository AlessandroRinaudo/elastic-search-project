from fastapi import FastAPI, File, UploadFile, HTTPException
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConnectionError
from typing import Optional
from typing import List

import uuid
import textract
import time
import os

from app.objects.CVObject import CVObject as cvo

app = FastAPI()
es = Elasticsearch([{'host': 'es-container', 'port': 9200}])


@app.post("/upload_pdf")
async def upload_file(files: List[UploadFile] = File(...)):
    idFile = 0
    responseDict = dict()

    for file in files:
        path = os.getcwd()+"/app/tmp/"+str(int(time.time()))+str(idFile)+".pdf"
        currentCV = cvo(info="", id=uuid.uuid4())
        with open(path, "wb") as cv:
            cv.write(file.file.read())
            currentCV.info = textract.process(path).decode("utf-8")

        os.remove(path)

        try:
            response = es.index(
                index=currentCV.index,
                doc_type=currentCV.doc_type,
                id=currentCV.id,
                body=currentCV.getBody()
            )
            responseDict[currentCV.id] = response

        except ConnectionError:
            raise HTTPException(
                status_code=500, detail="Internal Server Error")
            continue
        idFile += 1

    if responseDict:
        return responseDict
    else:
        return []


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
