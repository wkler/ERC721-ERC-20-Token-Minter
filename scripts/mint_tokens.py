from brownie import ERC20Token
from scripts.utils import get_account

# Mints from 1 - 15 ERC-20 tokens to the NFT minter.
def mint_erc20_tokens():
    account = get_account()
    # Gets latest instance of the ERC-20 token contract
    token_contract = ERC20Token[-1]
    print(f"  Minting tokens from {token_contract}")
    # Calls the function that mints tokens to the function invoker
    token_contract.mintTokens({"from": account})
    print(f"  Chainlink VRF called\nVerifying random number...\n")
