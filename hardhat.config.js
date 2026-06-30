// hardhat.config.js (ESM 版本)
import hardhatToolboxViem from "@nomicfoundation/hardhat-toolbox-viem";

const PRIVATE_KEY = "your private key here";

export default {
    solidity: {
      version:"0.8.19"
    },
    plugins: [hardhatToolboxViem], // 使用新的插件格式
    networks: {
        sepolia: {
            type: "http",
            url: "https://sepolia.infura.io/v3/cd03cfcd5b9841bda10062b23096cfbc", //https://sepolia.infura.io
            accounts: [PRIVATE_KEY],
        },
    },
};

//cd03cfcd5b9841bda10062b23096cfbc https://sepolia.infura.io/v3/cd03cfcd5b9841bda10062b23096cfbc