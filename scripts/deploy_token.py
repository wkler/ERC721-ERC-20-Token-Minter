from brownie import Dizzler, network, config
from scripts.helpful_scripts import get_account, TEST_BLOCKCHAIN_ENVIRONMENTS

link_fee = 0.1 * 1**18
#Auto verifys contract when uploaded to a network listed on etherscan
publish_source = (
    True if network.show_active() in TEST_BLOCKCHAIN_ENVIRONMENTS else False
)
#Deploys the contract
def main():
    account = get_account()
    dizzler_token = Dizzler.deploy(
        config["networks"][network.show_active()]["vrf_coordinator_addr"],
        config["networks"][network.show_active()]["link_token_addr"],
        config["networks"][network.show_active()]["key_hash"],
        link_fee,
        {"from": account}, 
        publish_source=publish_source
    )
    print("  Dizzler deployed")
    print(f"  Owner is: {account}\n")