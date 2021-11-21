//SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.7/VRFConsumerBase.sol";

contract Dizzler is ERC20("Dizzler", "DIZ"), VRFConsumerBase, Ownable {
    address public guiCreatorAddr;
    address vrfCoordinator;
    bytes32 keyhash;
    address linkToken;
    uint256 fee;
    uint256 randomResult;
    // address[] public guiMinters;  
    mapping(address => bool) public isMinter;
    event RandomNumberFulfillment(bytes32 requestId);
    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 _fee
    ) 
    VRFConsumerBase(
        vrfCoordinator,
        linkToken
    ) 
    {
        vrfCoordinator = _vrfCoordinator;
        linkToken = _linkToken;
        keyhash = _keyhash;
        fee = _fee;
    }

    function getRandomNumber() private onlyMinter() returns(bytes32 requestId) {
        require(LINK.balanceOf(address(this)) >= fee, "Please fund contract with Link");
        return requestRandomness(keyhash, fee);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        require(randomness > 0, "Randomness not returned");
        randomResult = (randomness % 15) + 1;
        _mint(msg.sender, randomResult);
        emit RandomNumberFulfillment(requestId);
    }

    modifier onlyMinter() {
        require(isMinter[msg.sender] == true, "Has to be minter");
        _;
    }
}