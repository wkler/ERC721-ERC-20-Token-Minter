import os
import json
from web3 import Web3
from dotenv import load_dotenv
load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("RINKEBY_RPC_URL")))
chain_id = 4
my_address = "0x42A7b811d096Cba5b3bbf346361106bDe275C8d7"
private_key = os.getenv("PRIVATE_KEY")
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)
token_address = "0x9e306f6c4acBe2D5856D0876A9d7AC8e9444AB34"

with open("build/contracts/ERC20Token.json", "r") as abi_file:
    abi_info_json = json.load(abi_file)
token_abi = abi_info_json["abi"]

contract_instance = w3.eth.contract(address=token_address, abi=token_abi)
rand_res = contract_instance.functions.randomResult().call()
print(rand_res)
get_rand = contract_instance.functions.getRandomNumber().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce + 1}
)
signed_get_rand_txn = w3.eth.account.sign_transaction(
    get_rand, private_key=private_key
)

signed_tx_hash = w3.eth.send_raw_transaction(signed_get_rand_txn.rawTransaction)
print("Getting random number")
tx_receipt = w3.eth.wait_for_transaction_receipt(signed_tx_hash)
print(f"{contract_instance.functions.getLinkBalance().call()}")