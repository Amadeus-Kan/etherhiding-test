from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ethereum-sepolia-rpc.publicnode.com'))

# 把旧地址填在这里
old_contract = "0x167f8c47bd109e18cb4129688cfadd03517ef937"

# 1. 检查该地址是否有代码（0x表示没有合约）
code = w3.eth.get_code(old_contract)
if code == b'' or code == '0x':
    print("❌ 在当前节点的最新状态下，该地址没有合约代码！")
    print("   原因：要么地址错了，要么该节点把旧数据修剪掉了，要么你连错了网络。")
else:
    print(f"✅ 该地址有代码: {code.hex()[:50]}...")
    print("   既然有代码，尝试用我们之前的读取逻辑，若仍卡住，则100%是节点超时/修剪导致。")