import sys
sys.path.append("metadata_info")
import json
import requests
from metadata_template import nft_metadata
from brownie import NftFactory, ERC20Token
from scripts.utils import get_account, network, config
from metadata_template import nft_metadata

def ipfs_upload():
    filepath = "./stylized.png"
    with open(filepath, "rb") as styled_image_path:
        image_binary = styled_image_path.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
    with open("metadata_info/metadata.json", "w") as updated_metadata_image:
        nft_metadata["image"] = image_uri
        json.dump(nft_metadata, updated_metadata_image, indent=2)
        print(image_uri)


