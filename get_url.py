# get_url.py
import webbrowser
from web3 import Web3

# 1. 连接到以太坊节点 (使用公共节点)
'''
    https://eth-sepolia.api.onfinality.io/public

    infura:
    https://sepolia.infura.io/v3/cd03cfcd5b9841bda10062b23096cfbc
    FW89daaaX9E7KG2a6vbDCs6ka7HKywS3JC9EbDegBbfpOMWOwE3cug

'''
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/cd03cfcd5b9841bda10062b23096cfbc'))

if not w3.is_connected():
    print("连接以太坊节点失败!")
    exit()

# 2. 创建合约对象
'''
    0x167f8c47bd109e18cb4129688cfadd03517ef937 bilibili
    0x882bc29940a840c471777cf1e30fe62eff79c8bb hit
    0x2566a117e112a3262763722100706de36e5b4904 bilibili
'''
CONTRACT_ADDRESS = Web3.to_checksum_address("0x167f8c47bd109e18cb4129688cfadd03517ef937")
CONTRACT_ABI = [
    {
        "inputs": [],
        "name": "storedUrl",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# 5. 调用合约的 storedUrl() 
try:
    stored_url = contract.functions.storedUrl().call()
    print(f"从区块链上读取到的 URL 是: {stored_url}")
    print("正在打开浏览器...")
    webbrowser.open(stored_url)

except Exception as e:
    print(f"合约调用失败: {e}")