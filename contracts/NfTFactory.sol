//SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NftFactory is ERC721URIStorage, Ownable {
    uint256 public tokenCounter;
    // See deploy_contracts.py for what these parameters are shipping with
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