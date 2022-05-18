// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract TokenRPS is ERC1155 {
    uint256 public constant Rock = 1;
    uint256 public constant Paper = 2;
    uint256 public constant Scissors = 3;

    constructor() ERC1155("https://ipfs.io/ipfs/bafybeiccdc7pnvqmttfiuryvba2damanm3g5eyikawo36qjkivmfhodali/{id}.json") {
        _mint(msg.sender, Rock, 1, "");
        _mint(msg.sender, Paper, 1, "");
        _mint(msg.sender, Scissors, 1, "");
    }

    function uri(uint256 _tokenid) override public pure returns (string memory) {
        return string(
            abi.encodePacked(
                "https://ipfs.io/ipfs/bafybeiccdc7pnvqmttfiuryvba2damanm3g5eyikawo36qjkivmfhodali/",
                Strings.toString(_tokenid),".json"
            )
        );
    }
    
}
