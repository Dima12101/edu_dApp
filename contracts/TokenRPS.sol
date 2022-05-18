// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract TokenRPS is ERC1155 {
    uint256 public constant Rock = 1;
    uint256 public constant Paper = 2;
    uint256 public constant Scissors = 3;

    constructor() ERC1155("https://ipfs.io/ipfs/bafybeiccdc7pnvqmttfiuryvba2damanm3g5eyikawo36qjkivmfhodali/{id}.json") {}

    function uri(uint256 _tokenid) override public pure returns (string memory) {
        return string(
            abi.encodePacked(
                "https://ipfs.io/ipfs/bafybeiccdc7pnvqmttfiuryvba2damanm3g5eyikawo36qjkivmfhodali/",
                Strings.toString(_tokenid),".json"
            )
        );
    }

    //If this of your first Rock and you do not have any Paper the contract will let you buy one
    function mintRock() public{
        require(balanceOf(msg.sender,Rock) == 0,"you already have a Rock ");
        require(balanceOf(msg.sender,Paper) > 0,"you have a Paper, stop!");
        _mint(msg.sender,Rock,1,"0x000");
    }
    
    //If this of your first Paper and you do not have any Scissors the contract will let you buy one
    function mintPaper() public{
        require(balanceOf(msg.sender,Paper) == 0,"you already have a Paper ");
        require(balanceOf(msg.sender,Scissors) > 0,"you have a Scissors, stop!");
        _mint(msg.sender,Paper,1,"0x000");
    }

    //If this of your first Scissors and you do not have any Rock the contract will let you buy one
    function mintScissors() public{
        require(balanceOf(msg.sender,Scissors) == 0,"you already have a Scissors ");
        require(balanceOf(msg.sender,Rock) > 0,"you have a Rock, stop!");
        _mint(msg.sender,Paper,1,"0x000");
    }
    
}
