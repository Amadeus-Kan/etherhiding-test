// scripts/deploy.js
import { network } from "hardhat";

async function main() {
    // 1. 连接到网络，获取 viem 实例
    const { viem } = await network.getOrCreate();

    // 2. 使用 viem.deployContract 部署合约
    //    参数1: 合约名称 "UrlStorage"
    //    参数2: 构造函数的参数数组，这里传入初始 URL
    const urlStorage = await viem.deployContract("urlstorage", ["https://www.bilibili.com/"]);

    // 3. 打印部署成功的合约地址
    console.log(`合约部署成功! 地址是: ${urlStorage.address}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});