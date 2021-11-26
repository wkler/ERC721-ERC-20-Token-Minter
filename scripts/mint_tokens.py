# Creates random amount of tokens. The number of tokens created
# is based on the random number returned from VRFCoordinator.
# This number will always be from 1 - 15 
# More info on randomness can be found at: https://docs.chain.link/docs/get-a-random-number/

from brownie import ERC20Token
from scripts.utils import get_account

def mint_erc20_tokens():
    account = get_account()
    token_contract = ERC20Token[-1]
    print(f"  Minting tokens form {token_contract}")
    tx = token_contract.getRandomNumber({"from": account})
    print(f"  Chainlink VRF called\nVerifying random number...\n")