from brownie import NftFactory, config, network
from scripts.helpful_scripts import get_account


def deploy_nft():
    account = get_account()
    nft_factory = NftFactory.deploy("Test", "TST", {"from": account}, publish_source=True)
    print(f"  NftFactory deployed to: {account}")

def main():
    deploy_nft()