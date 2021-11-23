from brownie import ERC20Token, config, network, project
from scripts.helpful_scripts import get_account
from Gui.gui_main import *

def mint_tokens():
    account = get_account()
    token_contract = ERC20Token[-1]
    print(token_contract)
    tx = token_contract.getRandomNumber({"from": account})
    tx.wait(1)
    print(f"  VRF called")


def get_total_supply():
    account = get_account()
    token_contract = ERC20Token[-1]
    get_total_supply = token_contract.totalSupply()
    print(f"  Total supply: {get_total_supply}")

def get_random_result():
    account = get_account()
    token_contract = ERC20Token[-1]
    get_random_number = token_contract.randomResult()
    get_link_balance = token_contract.getLinkBalance()
    print(f"  Contract address: {token_contract.address}")
    print(f"  Contract has {get_link_balance} LINK")
    print(f"  Random number: {get_random_number}")

def main():
    baseClass()
    # get_total_supply()
    # get_random_result()
    # mint_tokens()