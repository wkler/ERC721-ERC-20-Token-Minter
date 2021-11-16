pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract NftFactory is ERC721 {
    uint256 tokenCounter;
    constructor(
        string memory _name, 
        string memory _symbol
    ) 
        public 
    ERC721(_name, _symbol) 
    {
        tokenCounter = 0;
    }

    function createCollectable(string memory tokenURI) public returns(uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter += 1;
        return newItemId;
    }
}