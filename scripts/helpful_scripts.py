import sys
sys.path.append("nft_creator_gui/metadata_info")
from metadata import metadata_dictionary
from brownie import accounts, network, config, NftFactory

LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "mainnet-fork"]
TEST_BLOCKCHAIN_ENVIRONMENTS = ["rinkeby"]

#gets account based on what network contract is deployed to
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        return accounts[0]
    if network.show_active() in TEST_BLOCKCHAIN_ENVIRONMENTS:
        return accounts.add(config["wallets"]["from_key"])

#Reads the file path of image to be minted
def assign():
    with open("nft_creator_gui/TextFiles/nft_name.txt", "r") as name_metadata:
        name = name_metadata.read()
    with open("nft_creator_gui/TextFiles/nft_description.txt", "r") as description_metadata:
        description = description_metadata.read()

    metadata_dictionary["name"] = name
    metadata_dictionary["description"] = description
    print(metadata_dictionary)

def main():
    assign()