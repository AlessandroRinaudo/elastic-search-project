from pathlib import Path
import requests as r
import os

files = []

for child in Path(os.getcwd()+'/data').iterdir():
    if child.is_file():
        headers = {
            'accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }

        fn = './data/'+child.name

        fi = open(fn, 'rb')

        files.append(('files', (fn, fi)))

    if len(files) > 100:
        response = r.post(
                    'http://localhost/upload_pdf', files=files)
        print(response.text)
        del(files)
        files = []
    print(files)

response = r.post(
            'http://localhost/upload_pdf', files=files)
print(response.text)
