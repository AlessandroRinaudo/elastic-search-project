from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_upload_pdf():
    file = open('./data/nicolas-lejeune-2021.pdf', 'rb')
    response = client.post('/upload_cv', files={"files": file})
    assert response.status_code == 200

def test_upload_docx():
    file = open('./data/CV_Alessandro_Rinaudo.docx', 'rb')
    response = client.post('/upload_cv', files={"files": file})
    assert response.status_code == 200

def test_upload_other():
    file = open('./data/error.txt', 'rb')
    response = client.post('/upload_cv', files={"files": file})
    assert response.status_code == 415
    
## Doesn't work
# def test_upload_multiple_pdf():
#     f1 = open('./data/nicolas-lejeune-2021.pdf', 'rb')
#     f2 = open('./data/CV_Alessandro_Rinaudo.pdf', 'rb')
#     response = client.post('/upload_cv', files={"files": [f1, f2]]})
#     assert response.status_code == 200

