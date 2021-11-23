#To be used when initially deploying contracts
from brownie import ERC20Token, config, network
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIROMENTS
#Verifiys contracts on etherscan automatically.  
publish_source = (
    True if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS else False
)

# def deploy_nft():
#     account = get_account()
#     nft_factory = NftFactory.deploy("Test", "TST", {"from": account}, publish_source=True)
#     print(f"  NftFactory deployed to: {account}")

def deploy_token():
    account = get_account() 
    token_contract = ERC20Token.deploy(
        "Dizzler",
        "DIZ",
        config["networks"][network.show_active()]["vrf_coordinator_address"],
        config["networks"][network.show_active()]["link_token_address"],
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["link_fee"],
        {"from": account},
        publish_source=True
    )

def main():
    # deploy_nft()
    deploy_token()