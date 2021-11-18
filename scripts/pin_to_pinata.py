import os
import requests
from pathlib import Path

PINATA_BASE_URL = "https://app.pinata.cloud"
filepath = "./nft_creator_gui/TextFiles/edited_image_result_path.txt"
filename = filepath.split("/")[-1]
endpoint = "pinning/pinFileToIPFS"

pinata_keys = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_api_secret": os.getenv("PINATA_API_SECRET")
}
print(filename)

def upload_to_pinata():
    with open(filepath, "r") as f:
        file = f.read()
        print(file)
        response = requests.post(PINATA_BASE_URL + endpoint, )
