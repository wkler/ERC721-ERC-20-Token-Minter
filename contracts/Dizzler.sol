pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Dizzler is ERC20 {
    address public owner;
    constructor(uint256 _totalSupply) public ERC20("Dizzler", "DIZ") {
        owner = msg.sender;
        _mint(owner, _totalSupply);
    }

    function mint(uint256 _to, uint256 _amount) internal returns(uint256) {
        //Function can only be called if msg.sender succesfully mints nft.
        //Possible use of Chainlink keepers here
        return _amount;
    }
    
}