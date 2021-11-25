import os
import requests
from pathlib import Path

PINATA_BASE_URL = "https://app.pinata.cloud/"
filepath = "./stylized.png"
filename = filepath.split("/")[-1]
endpoint = "pinning/pinFileToIPFS"

pinata_keys = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_api_secret": os.getenv("PINATA_API_SECRET")
}
print(filename)

def upload_to_pinata():
    with open(filepath, "rb") as f:
        file = f.read()
        print(file)
        response = requests.post(
            PINATA_BASE_URL + endpoint,  files={"file": (filename, file)},
            headers=pinata_keys,
        )
        print(response.json())
        
if __name__ == "main":
    main()