ZERION_TOKEN_ADAPTER_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "token", "type": "address"}],
        "name": "getComponents",
        "outputs": [
            {
                "components": [
                    {"internalType": "address", "name": "token", "type": "address"},
                    {"internalType": "string", "name": "tokenType", "type": "string"},
                    {"internalType": "uint256", "name": "rate", "type": "uint256"},
                ],
                "internalType": "struct Component[]",
                "name": "",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "address", "name": "token", "type": "address"}],
        "name": "getMetadata",
        "outputs": [
            {
                "components": [
                    {"internalType": "address", "name": "token", "type": "address"},
                    {"internalType": "string", "name": "name", "type": "string"},
                    {"internalType": "string", "name": "symbol", "type": "string"},
                    {"internalType": "uint8", "name": "decimals", "type": "uint8"},
                ],
                "internalType": "struct TokenMetadata",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
]
