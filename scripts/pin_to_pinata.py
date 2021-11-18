import os
import requests
from pathlib import Path

PINATA_BASE_URL = "https://app.pinata.cloud"
filepath = "./nft_creator_gui/TextFiles/edited_image_result_path.txt"
filename = filepath.split("/")[-1]

pinata_keys = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_api_secret": os.getenv("PINATA_API_SECRET")
}

print(filename)
with open(filepath, "r") as f:
    file = f.read()
