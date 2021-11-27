//For basic usage, this file does not need to be edited. 
//To name your NFT collection, edit the "deploy_contracts.py" file which can be found in the scripts folder

//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NftFactory is ERC721URIStorage, Ownable {
    uint256 public tokenCounter;
    //Name your NFT colection and give it a symbol through the "deploy_contracts.py" script found in the scripts folder
    constructor(
        string memory _name, 
        string memory _symbol
    ) 
    ERC721(_name, _symbol) 
    {
        tokenCounter = 0;
    }

    function createNFT(string memory tokenURI) public onlyOwner() returns(uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter += 1;
        return newItemId;
    }
}