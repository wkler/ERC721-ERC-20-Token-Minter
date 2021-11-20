from brownie import NftFactory
from scripts.helpful_scripts import get_account, network, config

def create_nft():
    account = get_account()
    nft_factory = NftFactory[-1]
    tx = nft_factory.createNFT(
        "https://gateway.ipfs.io/ipns/k51qzi5uqu5djlfyyj2hi192fwqindfrz01pkqhb7th7m77qwmrhvqx9txgt4l",
        {"from": account}
    )
    tx.wait(1)
    print(tx)
    print("  If you are reading this then this might have worked!")
    return nft_factory.tokenCounter()



def main():
    create_nft()