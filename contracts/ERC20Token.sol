//SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract ERC20Token is ERC20, VRFConsumerBase, Ownable {
    address vrfCoordinator;
    bytes32 keyhash;
    address linkToken;
    uint256 fee;
    uint256 public randomResult;
    event RandomNumberFulfillment(bytes32 requestId);
    // See deploy_contracts.py for what these parameters are shipping with
    constructor(
        string memory _name,
        string memory _symbol,
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 _fee,
        uint256 _totalSupply
    ) 
    VRFConsumerBase(
        _vrfCoordinator,
        _linkToken
    ) 
    ERC20(_name, _symbol) 
    {
        _mint(owner(), _totalSupply);
        vrfCoordinator = _vrfCoordinator;
        linkToken = _linkToken;
        keyhash = _keyhash;
        fee = _fee;
    }

    function mintTokens() public onlyOwner() returns(bytes32 requestId) {
        require(LINK.balanceOf(address(this)) >= fee, "Please fund contract with Link");
        return requestRandomness(keyhash, fee);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        require(randomness > 0, "Randomness not returned");
        randomResult = (randomness % 15) + 1;
        _mint(owner(), randomResult * 10**18);
        emit RandomNumberFulfillment(requestId);
    }

    function getLinkBalance() public view returns(uint256) {
        return LINK.balanceOf(address(this));
    }
}