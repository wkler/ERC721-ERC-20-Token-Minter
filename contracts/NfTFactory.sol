pragma solidity ^0.7.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
// import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NftFactory is ERC721 {
    uint256 public tokenCounter;
    constructor(
        string memory _name, 
        string memory _symbol
    ) public 
    ERC721(_name, _symbol) 
    {
        tokenCounter = 0;
    }

    function createNFT(string memory tokenURI) public returns(uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter += 1;
        return newItemId;
    }
}