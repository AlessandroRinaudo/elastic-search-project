
from elasticsearch.exceptions import NotFoundError, ConnectionError
from fastapi import FastAPI, File, UploadFile, HTTPException
from app.objects.CVObject import CVObject
from elasticsearch import Elasticsearch
from docx2txt import process
from typing import Optional
from typing import List

import textract
import logstash
import logging
import time
import os

# Logstash initialization
host = 'logs-container'
test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version = 1))
tmp_path = os.getcwd()+"/app/tmp/"

app = FastAPI()
es = Elasticsearch([{'host': 'es-container', 'port': 9200}])


@app.post("/upload_cv")
async def upload_pdf_file(files: List[UploadFile] = File(...)):
    cv_list = []
    
    for file in files:
        type_file = file.filename.split('.')[1]
        path = tmp_path + str(int(time.time())) + "." + type_file
        currentCV = CVObject()  

        with open(path, "wb") as cv:
            cv.write(file.file.read())
            if type_file == 'pdf':
                currentCV.initCvWithInfo(textract.process(path).decode("utf-8"))
            if type_file == 'docx':
                currentCV.initCvWithInfo(process(path))
        os.remove(path)

        try:
            response = es.index(
                index=currentCV.index,
                doc_type=currentCV.doc_type,
                id=currentCV.id,
                body=currentCV.getBody()
            )
            cv_list.append(response)
            test_logger.info('CV uploaded successfully', extra = {"file_name": file.filename})
            
        except ConnectionError:
            test_logger.error('Tried to reach "/upload", status : 500 - Internal Server Error')
            raise HTTPException(status_code = 500, detail = "Internal Server Error")

    return cv_list

@app.get("/search_cv")
def read_item(q: Optional[str] = None, contactInfoOnly: bool = False):
    srouceExcluseList = "info" if contactInfoOnly else ""

    try:
        test_logger.info('Search executed : ' + str(q))
        if q:
            logs = es.search(index = "cv_search", query = { "match": { "info": q}}, _source_excludes = srouceExcluseList)
        else:
            logs = es.search(index = "cv_search", query = { "match_all": {}}, _source_excludes = srouceExcluseList)
        return logs['hits']['hits']

    except NotFoundError:
        return []
    except ConnectionError:
        test_logger.error('Tried to reach "/search_cv", status : 500 - Internal Server Error')
        raise HTTPException(status_code=500, detail="Internal Server Error")
