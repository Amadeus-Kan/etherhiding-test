// hardhat.config.js (ESM 版本)
import hardhatToolboxViem from "@nomicfoundation/hardhat-toolbox-viem";

const PRIVATE_KEY = "4fa8bc0dd849e59e58df302f1da221aa3d3cf3f1b879fcd0baabed33ade1226b";

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