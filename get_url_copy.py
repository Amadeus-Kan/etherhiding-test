# get_url.py
from web3 import Web3

'''
    https://rpc.sepolia.org
    https://eth-sepolia.api.onfinality.io/public

    infura api key:
    cd03cfcd5b9841bda10062b23096cfbc 
    https://sepolia.infura.io/v3/<MY API KEY>
'''
w3 = Web3(Web3.HTTPProvider('https://rpc.sepolia.org'))
if not w3.is_connected():
    print("连接以太坊节点失败!")
    exit()

'''
    0x167f8c47bd109e18cb4129688cfadd03517ef937 bilibili
    0x882bc29940a840c471777cf1e30fe62eff79c8bb hit

'''

CONTRACT_ADDRESS = Web3.to_checksum_address("0x167f8c47bd109e18cb4129688cfadd03517ef937")
CONTRACT_ABI = [
    {
        "inputs": [],
        "name": "storedUrl",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

try:
    stored_url = contract.functions.storedUrl().call()
    print(f"从区块链上读取到的 URL 是: {stored_url}")
except Exception as e:
    print(f"合约调用失败: {e}")