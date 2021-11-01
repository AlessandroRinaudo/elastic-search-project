from fastapi.testclient import TestClient

from . import main as app

client = TestClient(app)


# def cv_successfully_upload():
#     response = client.get("http://localhost/search_cv")
#     print(response)
#     assert response.status_code == 200