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
def read_image_file_path():
    with open("nft_creator_gui/edited_image_result_path.txt") as image:
        print(image.read())

