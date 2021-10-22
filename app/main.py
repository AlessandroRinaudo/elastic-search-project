from fastapi import FastAPI, File, UploadFile, HTTPException
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError, ConnectionError
from typing import Optional
from typing import List

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

app = FastAPI()
es = Elasticsearch([{'host': 'es-container', 'port': 9200}])

""" extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, 3]
} """

""" @app.get("/")
async def test():
    et la je genere des logs en fait non ?
    test_logger.error('python-logstash: test logstash error message.')
    test_logger.info('python-logstash: test logstash info message.')
    test_logger.warning('python-logstash: test logstash warning message.')
    test_logger.info('python-logstash: test extra fields', extra=extra)
    return { "test": 1} """

@app.post("/upload_pdf")
async def upload_file(files: List[UploadFile] = File(...)):
    idFile = 0
    responseDict = dict()

    for file in files:
        path = os.getcwd()+"/app/tmp/"+str(int(time.time()))+str(idFile)+".pdf"

        with open(path, "wb") as cv:
            cv.write(file.file.read())
            text = textract.process(path).decode("utf-8")
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

            # Send log to Logstash
            test_logger.info('CV uploaded successfully', extra={"file_name": file.filename})

        except ConnectionError:

            # Send log to Logstash
            test_logger.error('Tried to reach "/upload", status : 500 - Internal Server Error')

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
        test_logger.info('Search executed : ' + q)
        if q:
            logs = es.search(index="cv_search", query={"match": {"info": q}})
        else:
            logs = es.search(index="cv_search", query={"match_all": {}})
        return logs['hits']['hits']
    except NotFoundError:
        return []
    except ConnectionError:
        # Senf log to Logstash
        test_logger.error('Tried to reach "/search_cv", status : 500 - Internal Server Error')
        
        raise HTTPException(status_code=500, detail="Internal Server Error")
