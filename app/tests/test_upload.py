from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from ..routers.upload import es
from ..routers.upload import test_logger
from fastapi import APIRouter, File, UploadFile, HTTPException

from ..main import app

client = TestClient(app)


def test_upload_pdf():
    es.index = MagicMock(return_value=[
        {"_index": "cv_search",
         "_type": "cv",
         "_id": "d0c2767a-1752-5a78-8ae5-401ce3a0ba4a",
         "_version": 5,
         "result": "updated",
         "_shards": {
             "total": 2,
             "successful": 1,
             "failed": 0
         },
         "_seq_no": 81,
         "_primary_term": 3}
    ]
    )
    file = open('data/nicolas-lejeune-2021.pdf', 'rb')
    response = client.post('/upload_cv', files={"files": file})
    assert response.status_code == 200
    assert response.json() == [[
        {
            "_index": "cv_search",
            "_type": "cv",
            "_id": "d0c2767a-1752-5a78-8ae5-401ce3a0ba4a",
            "_version": 5,
            "result": "updated",
            "_shards": {
                "total": 2,
                "successful": 1,
                "failed": 0
            },
            "_seq_no": 81,
            "_primary_term": 3
        }
    ]
    ]


def test_upload_docx():
    es.index = MagicMock(return_value=[
        {"_index": "cv_search",
         "_type": "cv",
         "_id": "d0c2767a-1752-5a78-8ae5-401ce3a0ba4a",
         "_version": 5,
         "result": "updated",
         "_shards": {
             "total": 2,
             "successful": 1,
             "failed": 0
         },
            "_seq_no": 81,
            "_primary_term": 3}
    ]
    )
    file = open('data/CV_Alessandro_Rinaudo.docx', 'rb')
    response = client.post('/upload_cv', files={"files": file})
    assert response.status_code == 200
    assert response.json() == [[
        {
            "_index": "cv_search",
            "_type": "cv",
            "_id": "d0c2767a-1752-5a78-8ae5-401ce3a0ba4a",
            "_version": 5,
            "result": "updated",
            "_shards": {
                "total": 2,
                "successful": 1,
                "failed": 0
            },
            "_seq_no": 81,
            "_primary_term": 3
        }
    ]
    ]

def test_upload_multiple_pdf():
    es.index = MagicMock(return_value=[
        {
            "_index": "cv_search",
            "_type": "cv",
            "_id": "363720ac-2744-56e8-9725-d29e55e95f7c",
            "_version": 16,
            "result": "updated",
            "_shards": {
                "total": 2,
                "successful": 1,
                "failed": 0
            },
            "_seq_no": 87,
            "_primary_term": 3
        },
        {
            "_index": "cv_search",
            "_type": "cv",
            "_id": "70df3d01-444e-5f44-a676-f35ff788f4a2",
            "_version": 31,
            "result": "updated",
            "_shards": {
                "total": 2,
                "successful": 1,
                "failed": 0
            },
            "_seq_no": 88,
            "_primary_term": 3
        }
    ]
    )
    f1 = open('./data/nicolas-lejeune-2021.pdf', 'rb')
    f2 = open('./data/CV_Alessandro_Rinaudo.pdf', 'rb')
    response = client.post('/upload_cv', files={"files": f1, "files": f2})
    assert response.status_code == 200
    assert response.json() == [[
    {
        "_index": "cv_search",
            "_type": "cv",
            "_id": "363720ac-2744-56e8-9725-d29e55e95f7c",
            "_version": 16,
            "result": "updated",
            "_shards": {
                "total": 2,
                "successful": 1,
                "failed": 0
            },
            "_seq_no": 87,
            "_primary_term": 3
        },
        {
            "_index": "cv_search",
            "_type": "cv",
            "_id": "70df3d01-444e-5f44-a676-f35ff788f4a2",
            "_version": 31,
            "result": "updated",
            "_shards": {
                "total": 2,
                "successful": 1,
                "failed": 0
            },
            "_seq_no": 88,
            "_primary_term": 3
    }
]
]

#  to mock
def test_upload_other():
    file = open('data/error.txt', 'rb')
    response = client.post('/upload_cv', files={"files": file})
    assert response.status_code == 415
    assert response.json() == {"detail": "Unsupported Media Type : You're file extension (txt) is not supported"}

