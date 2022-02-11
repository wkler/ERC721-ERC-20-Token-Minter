# This file handles contract deployment.
# See the smart contract constructors for input field types.
# See config file for more info on arguments passed to contract constructors.
from brownie import ERC20Token, NftFactory, config, network
from scripts.utils import get_account, LOCAL_BLOCKCHAIN_ENVIROMENTS

# Programmatically verifies contracts on Etherscan if deploying to Ethereum testnet.
# This veriable gets passed to the contract constructors.
publish_source = (
    True if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIROMENTS else False
)


# Deploys NFT factory contract.
def deploy_nft():
    account = get_account()
    nft_factory = NftFactory.deploy(
        "MyFactoryName",
        "FACTORYSYMBOL",
        {"from": account},
        publish_source=publish_source,
    )
    print(nft_factory)


# Deploys ERC20Token contract
def deploy_token():
    account = get_account()
    token_contract = ERC20Token.deploy(
        "MyTokenName",
        "TOKENSYMBOL",
        config["networks"][network.show_active()]["vrf_coordinator_address"],
        config["networks"][network.show_active()]["link_token_address"],
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["link_fee"],
        1000000000000000000000,
        {"from": account},
        publish_source=publish_source,
    )
    print(token_contract)


def main():
    deploy_nft()
    deploy_token()
