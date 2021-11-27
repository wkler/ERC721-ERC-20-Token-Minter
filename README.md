# ERC-721 + ERC-20 Token Minter
This project aims to give users an all in one NFT creation and minting experience. It contains a GUI that can edit and mint an image directly from local storage. All .PNG or .JPG images can be uploaded, styled utilizing the OpenCv library, and minted onto an Ethereum network. So far, this has only been tested on the Rinkeby network, but direct support for other networks will be added. Each time an NFT is minted, the creator also receives from 1 - 15 ERC-20 tokens. This was done to incentivize creators to mint their NFT's on this platform. As this idea is still in it's early stages, anyone who clones this project will have to deploy the smart contracts themselves, nullifying the ERC-20 token incentive, but as this repo matures, there will already be one contract for minting ERC-721 tokens (NFT's), and one contract for minting ERC-20 tokens. In it's final form, users would download a gui, connect their wallet, edit their images and mint NFT's all from one package. They would also be gaining from 1 - 15 ERC-20 tokens as incentive for every NFT they minted. The smart contracts the gui would mint from would already be on chain. 
See below for detailed steps on how to use.

*This project is in it's early stages, and was made for the Chainlink, 2021 Fall Hackathon.
https://chain.link/hackathon*


# How to use
There are a handful of required setup steps for this project.
1) You will need to install and create an account on MetaMask. You will also need your account's private key and be connected to the Rinkeby network. MetaMask documentation can be found at: https://metamask.io/faqs.html.
Once you have MetaMask installed and connected to the Rinkeby network, it will need some test ETH and test LINK. You can get some of each here: https://faucets.chain.link/rinkeby.
Make sure you select "Ethereum Rinkeby" under the "Network" tab.

*In order to insure security for your real crypto, only use this wallet for testing purposes*

2) Create free Infura account https://infura.io/. Obtain it's Rinkeby API project ID. Documentation can be found at:
https://infura.io/docs/ethereum

3)  Create free account on Pinata and obtain API key, and API secret. Documentation can be found at: https://docs.pinata.cloud/

4) Create free account on Etherscan and obtain API token. Documentation can be found at: https://docs.etherscan.io/

5)  Clone repository
~~~
git clone https://github.com/McManOfTheLand/ERC721-ERC-20-Token-Minter
~~~
 6)  Create Python virtual environment and activate it. While in the root of your directory, type the fallowing into your terminal:
~~~
python3 -m venv venv
./venv/scripts/activate
~~~
7)  Install needed packages. These can be found in the "requirements.txt" file in root directory. It should be noted that eth-brownie is NOT installed globally to prevent future version conflicts.
~~~
pip install -r requirements.txt
~~~
8) Install IPFS Command-Line. Instructions can be found: https://docs.ipfs.io/install/command-line/#official-distributions

9) Inside the root directory of your project, create a .env file. Add API keys as well as your MetaMask accounts private key to the .env file. 
 ADD SCREEN SHOT ON WHAT IT SHOULD LOOK LIKE
 
10) Name and deploy contracts by editing the deployment script found at <path/to/scripts/deploy_contracts.py>. You can also set the total supply of the ERC20 token and it will be sent to your wallet on deployment. To import your new token into MetaMask, follow this guide: https://metamask.zendesk.com/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask
To deploy contracts to the blockchain, run the command:
~~~
brownie run PATH/TO/deploy_contracty.py --network rinkeby
~~~
*NOTE: This project must to be run on the Rinkeby network*
A succesful deployment to the Rinkeby test network should look something like this:
ADD PHOTO OF TERMINAL AFTER SUCCESSFUL DEPLOYMENT

11) It is imperative that you fund your ERC20Token.sol contract with LINK tokens. If you do not do this, you will not be able to get ERC-20 tokens. In order to mint a random amount of tokens from 1 - 15, a Chainlink random number oracle was utilized. More info on Chainlink's VRF (random number generator) can be found: https://docs.chain.link/docs/chainlink-vrf/
Copy the contract address of your ERC20Token.sol contract and send it 1 LINK. Each oracle call will cost 0.1 LINK so you will be able to mint tokens 10 times before needing to refill the contract with LINK again.

12) Start IPFS server in a new terminal with the command: 
~~~
ipfs daemon
~~~

13) Once all of this set up is complete you can finally start the gui. Run the command:
~~~
brownie run PATH/TO/start_gui.py --network rinkeby
~~~

14) Click on "browse" to select image with extension .PNG or .JPG. Once image has loaded in, select a style.
15) Click on "stage" to add image to the minting area.
16) Click "MINT" to start the minting process. Blockchains will take a couple minutes to confirm the transactions, so in the mean time, it is recommended to not just keep clicking things on the gui (LOL). Once a couple minutes have gone by check https://testnets.opensea.io/, connect your wallet ---> view profile, and assuming all of the above steps were followed, your NFT will be visible. In your MetaMask, your token balance will have updated once the Chainlink VRF has returned a random number. Since the oracle will have to go off chain to fetch a random number, your tokens will take a minute or two longer to show up in your account than your NFT.

## Congragulations. You've done it!


