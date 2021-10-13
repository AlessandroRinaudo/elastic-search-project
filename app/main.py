from fastapi import FastAPI, File
from PyPDF2 import PdfFileReader

from io import BufferedReader, BytesIO
app = FastAPI()

@app.post("/")
async def upload_file(file: bytes = File(...)):
    sample_bytes = BytesIO(file)
    fFileObj = BufferedReader(sample_bytes)

    pdfReader = PdfFileReader(fFileObj)
    pageObj = pdfReader.getPage(0)
    resume = pageObj.extractText()
    return { "data" : pageObj.extractText()}
