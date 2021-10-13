from fastapi import FastAPI, File
from PyPDF2 import PdfFileReader
from io import BufferedReader, BytesIO
from elasticsearch import Elasticsearch
import uuid

app = FastAPI()
es = Elasticsearch([{'host': 'es-container', 'port': 9200}])

@app.post("/")
async def upload_file(file: bytes = File(...)):
    sample_bytes = BytesIO(file)
    fFileObj = BufferedReader(sample_bytes)
    pdfReader = PdfFileReader(fFileObj)
    pageObj = pdfReader.getPage(0)
    resume = pageObj.extractText()

    response = es.index(
        index = 'cv_search',
        doc_type = 'cv',
        id = uuid.uuid(),
        body = {
            "info" : resume
        }
    )