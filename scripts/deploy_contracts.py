#This file handles contract deployment.
#See contract constructors for input field types
#See config file for more info on arguments passed to contract constructors
#To run this file, type: brownie run PATH/deploy_contract.py 
#Make sure to have your virtual environment activated
from brownie import ERC20Token, NftFactory, config, network
from scripts.utils import(
    get_account, LOCAL_BLOCKCHAIN_ENVIROMENTS
)
#Verifiys contracts on etherscan automatically when given as constructor argument
publish_source = (
    True if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS else False
)
#Deploys NFT factory contract with specified arguments
def deploy_nft():
    account = get_account()
    nft_factory = NftFactory.deploy(
        "Test", 
        "TST", 
        {"from": account}, 
        publish_source=publish_source
    )

#Deploys ERC20Token contract with specified arguments
def deploy_token():
    account = get_account() 
    token_contract = ERC20Token.deploy(
        "NameHere",
        "SymbolHere",
        config["networks"][network.show_active()]["vrf_coordinator_address"],
        config["networks"][network.show_active()]["link_token_address"],
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["link_fee"],
        10000000000000000000000,
        {"from": account},
        publish_source=publish_source
    )

def main():
    deploy_nft()
    deploy_token()