# This scripts is meant to ONLY be run when the "MINT" button is clicked within the gui
# This script calls the "mintTokens" function on PATH/TO/ERC20Token.sol contract anytime the "MINT" button is clicked within the gui
# The acmount of tokens minted to contract owner will always be between 1 - 15
from brownie import ERC20Token
from scripts.utils import get_account

def mint_erc20_tokens():
    account = get_account()
    token_contract = ERC20Token[-1]
    print(f"  Minting tokens from {token_contract}")
    tx = token_contract.mintTokens({"from": account})
    print(f"  Chainlink VRF called\nVerifying random number...\n")