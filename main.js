import axios from 'axios';
import Web3 from 'web3';
import supplyChainABI from './contracts/SupplyChain.json';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
const CONTRACT_ADDRESS = process.env.REACT_APP_CONTRACT_ADDRESS;
const WEB3_PROVIDER_URL = process.env.REACT_APP_WEB3_PROVIDER_URL;

const web3 = new Web3(new Web3.providers.HttpProvider(WEB3_PROVIDER_URL));

const supplyChainContract = new web3.eth.Contract(supplyChainABI.abi, CONTRACT_ADDRESS);

async function authenticateUser(username, password) {
  try {
    const response = await axios.post(`${API_BASE_URL}/auth/login`, { username, password });
    localStorage.setItem('token', response.data.token);
    console.log("Authentication successful");
    return response.data;
  } catch (error) {
    console.error("Authentication failed", error);
    throw error;
  }
}

async function addProductDetails(productId, details) {
  const accounts = await web3.eth.getAccounts();
  try {
    await supplyChainContract.methods.addProduct(productId, details).send({ from: accounts[0] });
    console.log("Product added successfully");
  } catch (error) {
    console.error("Error adding product details", error);
    throw error;
  }
}

async function addShipmentDetails(shipmentId, products) {
  const accounts = await web3.eth.getAccounts();
  try {
    await supplyChainContract.methods.addShipment(shipmentId, products).send({ from: accounts[0] });
    console.log("Shipment details added successfully");
  } catch (error) {
    console.error("Error adding shipment details", error);
    throw error;
  }
}

async function getProductStatus(productId) {
  try {
    const status = await supplyChainContract.methods.getProductStatus(productId).call();
    console.log(`Status of product ${productId}:`, status);
    return status;
  } catch (error) {
    console.error("Error fetching product status", error);
    throw error;
  }
}

function displayProductStatus(productId) {
  getProductStatus(productId)
    .then(status => {
      console.log(`Displaying status for product ${productId}: ${status}`);
    })
    .catch(error => {
      console.error("Error displaying product status", error);
    });
}

function init() {
  const loginButton = document.getElementById("loginButton");
  if (loginButton) {
    loginButton.addEventListener("click", () => {
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;
      authenticateUser(username, password)
        .then(data => console.log("Logged in successfully", data))
        .catch(error => console.error("Login error", error));
    });
  } else {
    console.error('Login button not found');
  }
}

init();