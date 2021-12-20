from fastapi import APIRouter, File, UploadFile, HTTPException
from app.objects.CVObject import CVObject
from docx2txt import process
from typing import List

import textract
import time
import os
import pathlib
from app.connections import es
import app.routers.envLog as envLog

router = APIRouter(
    tags=["upload"]
)


@router.post("/upload_cv")
async def upload_pdf_file(files: List[UploadFile] = File(...)):
    cv_list = []
    supportedExtension = ["docx", "pdf"]
    tmp_path = "/code/app/tmp/"

    for file in files:
        type_file = pathlib.Path(file.filename).suffix.replace('.', '')
        if type_file in supportedExtension:
            path = tmp_path + str(int(time.time())) + "." + type_file
            currentCV = CVObject()

            with open(path, "wb") as cv:
                cv.write(file.file.read())
                if type_file == 'pdf':
                    currentCV.initCvWithInfo(
                        textract.process(path).decode("utf-8"))
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
                envLog.logFunction("info", 'CV uploaded successfully', {"file_name": file.filename})

            except ConnectionError:
                envLog.logFunction("error", 'Tried to reach "/upload", status : 500 - Internal Server Error (Cant reach ES instance)')
                raise HTTPException(
                    status_code=500, detail="Internal Server Error")

        else:
            envLog.logFunction("error", 'Tried to reach "/upload", status : 415 - Unsupported Media Type')
            raise HTTPException(
                                status_code=415, detail="Unsupported Media Type : You're file extension ({}) is not supported".format(type_file))
    return cv_list
