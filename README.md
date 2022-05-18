# edu_dApp
Задание по курсу "Экосистема распределенных реестров"

* Virtual Wallet: MetaMask
* Network: TestNet (Rinkeby)
* Ethereum infrastructure provider: Alchemy
* Smart Contracts Lang: Solidity
* Framework for smart contracts: Brownie
* Minting NFT Standart: ERC-1155

IPFS - https://nft.storage/

Steps:
* brownie networks set_provider alchemy
* brownie accounts new deployment_account
* brownie run deploy.py --network rinkeby
