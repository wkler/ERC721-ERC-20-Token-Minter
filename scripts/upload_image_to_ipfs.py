import json
import requests
from pathlib import Path
from metadata_template import nft_metadata

# Uploads image to IPFS and and updates NFT metadata to reflect the image URI
def ipfs_upload():
    filepath = "./stylized.png"
    # Opens path to image and reads it
    with Path(filepath).open("rb") as styled_image_path:
        image_binary = styled_image_path.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        # Posts image to IPFS. This image will become the NFT image
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        # Initializes variable with the full IPFS link to image
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"

    # Open metadata.json file and dumps the metadata dictionary into it
    with Path("./metadata_info/metadata.json").open("w") as updated_metadata_image:
        nft_metadata["image"] = image_uri
        json.dump(nft_metadata, updated_metadata_image, indent=2)
        return image_uri
