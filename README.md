# DecentralizedSupplyChain

This project is a decentralized supply chain management system that leverages blockchain technology to ensure transparency, security, and efficiency in tracking products from manufacturers to consumers. It uses Solidity for smart contracts, Python for data analysis, and Node.js for the backend.

## Structure

- **HTML/CSS/JavaScript**: Handles the frontend interface.
- **Node.js**: Manages backend processing and database interactions.
- **Python**: Analyzes supply chain data and generates reports.
- **Solidity**: Manages decentralized supply chain transactions.

## Setup

### HTML/CSS/JavaScript
1. Open the `index.html` file in a web browser to view the frontend interface.

### Node.js
1. Install Node.js if it is not already installed.
2. Navigate to the project directory and install the required dependencies:
    ```
    npm install
    ```
3. Set up the environment variables by creating a `.env` file in the `root` directory with the following content:
    ```
    MONGODB_URI=your_mongodb_connection_string
    PORT=3000
    ETH_NETWORK=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
    ```
4. Start the Node.js server:
    ```
    npm start
    ```

### Python
1. Install Python if it is not already installed.
2. Navigate to the `root` directory and create a virtual environment:
    ```
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```
        source venv/bin/activate
        ```
4. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

### Solidity
1. Install the Solidity compiler if it is not already installed:
    ```
    npm install -g solc
    ```
2. Compile the smart contract:
    ```
    solc --optimize --bin --abi contracts/SupplyChain.sol -o build
    ```
3. Deploy the smart contract using a tool like Truffle or Hardhat.

## Overview

1. **HTML/CSS/JavaScript**: Provides a user interface for managing products, viewing shipment statuses, and user registration/login.
2. **Node.js**: Processes product and shipment data, interacts with a MongoDB database, and handles requests from the frontend.
3. **Python**: Analyzes supply chain data, generates reports, and provides insights into efficiency and bottlenecks.
4. **Solidity**: Defines the smart contract for managing supply chain transactions and ensuring transparency and security.
