from fastapi import FastAPI, File, UploadFile, HTTPException
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConnectionError
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

# Bah je fait des choses qui va faire le viens en faite
host = 'logs-container'
test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959, version=1))
tmp_path=os.getcwd()+"/app/tmp/"

# Et puis la je fait genre qu'il y a des choses a dire
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
from app.objects.CVObject import CVObject as cvo

app = FastAPI()
es = Elasticsearch([{'host': 'es-container', 'port': 9200}])


@app.get("/")
async def test():
    # et la je genere des logs en fait non ?
    test_logger.error('python-logstash: test logstash error message.')
    test_logger.info('python-logstash: test logstash info message.')
    test_logger.warning('python-logstash: test logstash warning message.')
    test_logger.info('python-logstash: test extra fields', extra=extra)
    return {"test": 1}


@app.post("/upload_pdf")
async def upload_pdf_file(files: List[UploadFile] = File(...)):
    idFile = 0
    responseDict = dict()

    for file in files:
        path = tmp_path+str(int(time.time()))+str(idFile)+".pdf"
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
        if q:
            logs = es.search(index="cv_search", query={"match": {"info": q}}, _source_excludes = srouceExcluseList)
        else:
            logs = es.search(index="cv_search", query={"match_all": {}}, _source_excludes = srouceExcluseList)
        return logs['hits']['hits']

    except NotFoundError:
        return []
    except ConnectionError:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/upload_word")
async def upload_word_file(files: List[UploadFile] = File(...)):
    idFile = 0
    responseDict = dict()

    for file in files:
        path = tmp_path+str(int(time.time()))+str(idFile)+".docx"

        with open(path, "wb") as cv:
            cv.write(file.file.read())
            text = process(path)
        os.remove(path)

        try:
            response = es.index(
                index='cv_search',
                doc_type='cv',
                id=uuid.uuid4(),
                body={
                    "info": text
                }
            )
            responseDict[idFile] = response

        except ConnectionError:
            raise HTTPException(
                status_code=500, detail="Internal Server Error")
        idFile += 1

    if responseDict:
        return responseDict
    else:
        return []
