import os
import requests
from pathlib import Path
from brownie import NftFactory
from scripts.utils import get_account

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
filepath = "./metadata_info/metadata.json"
filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}

def upload_to_pinata():
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        print(response.json()["IpfsHash"])
        meatadata_ipfs_hash = response.json()["IpfsHash"]
        pinned_metadata_url = f"https://gateway.pinata.cloud/ipfs/{meatadata_ipfs_hash}"
    mint_nft_metadata(pinned_metadata_url)
    print(f"  Begining to mint {pinned_metadata_url}")

def mint_nft_metadata(ipfs_hash):
    print(ipfs_hash)
    account = get_account()
    nft_factory_contract = NftFactory[-1]
    nft_factory_contract.createNFT(
        ipfs_hash,
        {"from": account}
    )
    print(f"  This is your {nft_factory_contract.tokenCounter()}th collectable!")
    
# def main():
#     upload_to_pinata()

    