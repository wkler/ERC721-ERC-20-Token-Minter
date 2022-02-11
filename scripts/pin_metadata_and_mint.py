# Pins NFT metadata, as well as the NFT image to Pinata.
# Once pinned, the mint function within the NFT factory contract
# is called, and the Pinata link to the NFT metadata is
# passed as parameter in order to mint.
import os
import requests
from pathlib import Path
from brownie import NftFactory
from scripts.utils import get_account

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
nft_metadata_filepath = "./metadata_info/metadata.json"
nft_metadata_filename = nft_metadata_filepath.split("/")[-1:]
nft_img_to_pin = "./stylized.png"
# Authorization information for Pinata
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}

# Pins both the NFT metadata and the NFT image to Pinata
def upload_to_pinata():
    # Opens and reads the NFT image
    with Path(nft_img_to_pin).open("rb") as nft_image:
        image = nft_image.read()
        # Pins the NFT image to Pinata
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": ("nft_image", image)},
            headers=headers,
        )
    # Opens and reads NFT metatdata
    with Path(nft_metadata_filepath).open("r") as fp:
        nft_meta_data = fp.read()
        # Pins the NFT metadata to Pinata
        print(nft_meta_data)
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": ("nft_metadata", nft_meta_data)},
            headers=headers,
        )
        meatadata_ipfs_hash = response.json()["IpfsHash"]
        # Inserts the IPFS hash provided in our POST response to the Pinata link
        pinned_metadata_url = f"https://gateway.pinata.cloud/ipfs/{meatadata_ipfs_hash}"
        print(f"Minting: {pinned_metadata_url}")
        # Invokes the NFT minting function within smart contract and passes it the pinned metadata URL
        mint_nft_metadata(pinned_metadata_url)


# Mints pinned metadata URL
def mint_nft_metadata(nft_metadata):
    account = get_account()
    # Gets the most recent nft factory contract instance
    nft_factory_contract = NftFactory[-1]
    # Mints pinned metadata URL
    nft_factory_contract.createNFT(nft_metadata, {"from": account})
    print(f"You now have {nft_factory_contract.tokenCounter()} collectable")
