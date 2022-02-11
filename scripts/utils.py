from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "mainnet-fork"]

# Gets account based on what network is being used
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
