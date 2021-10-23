from fastapi import FastAPI, File, UploadFile, HTTPException
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConnectionError
from app.objects.CVObject import CVObject as cvo
from typing import Optional
from typing import List
import os
from docx2txt import process
import uuid
import textract
import time
import os

import logging
import logstash
import sys

# Logstash initialization
host = 'logs-container'
test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
tmp_path=os.getcwd()+"/app/tmp/"

app = FastAPI()
es = Elasticsearch([{'host': 'es-container', 'port': 9200}])


@app.post("/upload_cv")
async def upload_pdf_file(files: List[UploadFile] = File(...)):
    idFile = 0
    responseDict = dict()

    for file in files:
        try:
          path = tmp_path+str(int(time.time()))+str(idFile)+".pdf"
        except:
          path = tmp_path+str(int(time.time()))+str(idFile)+".docx"
        currentCV = cvo(info="", id=uuid.uuid4())
        with open(path, "wb") as cv:
            cv.write(file.file.read())
            try :
              currentCV.info = textract.process(path).decode("utf-8")
            except:
              currentCV.info = process(path)

        os.remove(path)

        try:
            response = es.index(
                index=currentCV.index,
                doc_type=currentCV.doc_type,
                id=currentCV.id,
                body=currentCV.getBody()
            )
            responseDict[currentCV.id] = response

            # Send log to Logstash
            test_logger.info('CV uploaded successfully', extra={"file_name": file.filename})

        except ConnectionError:
           # Send log to Logstash
            test_logger.error('Tried to reach "/upload", status : 500 - Internal Server Error')
            raise HTTPException(
                status_code=500, detail="Internal Server Error")
        idFile += 1

    if responseDict:
        return responseDict
    else:
        return []

@app.get("/search_cv")
def read_item(q: Optional[str] = None, contactInfoOnly: bool = False):
    # _source_excludes
    srouceExcluseList = ""
    if contactInfoOnly:
        srouceExcluseList = "info"
    try:
        test_logger.info('Search executed : ' + str(q))
        if q:
            logs = es.search(index="cv_search", query={"match": {"info": q}}, _source_excludes = srouceExcluseList)
        else:
            logs = es.search(index="cv_search", query={"match_all": {}}, _source_excludes = srouceExcluseList)
        return logs['hits']['hits']

    except NotFoundError:
        return []
    except ConnectionError:
        # Senf log to Logstash
        test_logger.error('Tried to reach "/search_cv", status : 500 - Internal Server Error')
        
        raise HTTPException(status_code=500, detail="Internal Server Error")


