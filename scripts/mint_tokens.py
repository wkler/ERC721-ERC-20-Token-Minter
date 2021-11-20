from brownie import interface, config, network
from scripts.helpful_scripts import get_account

IToken = interface.IDizzler(
    config["networks"]
    [network.show_active()]
    ["IDizzler_token"]
)

def main():
    account = get_account()
    tx = IToken.getRandomNumber({"from": account})
    tx.wait(1)
    print("Hopefully this worked")