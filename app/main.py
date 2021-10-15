from fastapi import FastAPI, File, HTTPException
from PyPDF2 import PdfFileReader
from io import BufferedReader, BytesIO
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConnectionError
from typing import Optional

import uuid

app = FastAPI()
es = Elasticsearch([{'host': 'es-container', 'port': 9200}])

@app.post("/upload_pdf")
async def upload_file(file: bytes = File(...)):
    sample_bytes = BytesIO(file)
    fFileObj = BufferedReader(sample_bytes)
    pdfReader = PdfFileReader(fFileObj)
    pageObj = pdfReader.getPage(0)
    resume = pageObj.extractText()
    try:
        response = es.index(
            index = 'cv_search',
            doc_type = 'cv',
            id = uuid.uuid4(),
            body = {
                "info" : resume
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