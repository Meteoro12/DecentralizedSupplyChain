// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DecentralizedSupplyChain {
    struct Product {
        uint id;
        string name;
        string originLocation;
        address currentHolder;
        bool hasBeenShipped;
    }

    mapping(uint => Product) public productRegistry;
    uint public totalProducts;

    event ProductRegistered(uint productId, string productName, string originLocation, address indexed owner);
    event ShipmentStatusToggled(uint productId, bool hasBeenShipped);
    event CustodyTransferred(uint productId, address indexed newHolder);

    modifier isCurrentHolder(uint productId) {
        require(msg.sender == productRegistry[productId].currentHolder, "Not current holder");
        _;
    }

    function registerNewProduct(string memory productName, string memory originLocation) public {
        totalProducts++;
        productRegistry[totalProducts] = Product(totalProducts, productName, originLocation, msg.sender, false);
        emit ProductRegistered(totalProducts, productName, originLocation, msg.sender);
    }

    function toggleShipmentStatus(uint productId, bool shippedStatus) public isCurrentHolder(productId) {
        Product storage product = productRegistry[productId];
        product.hasBeenShipped = shippedSorrytatus;
        emit ShipmentStatusToggled(productId, shippedStatus);
    }

    function confirmOrigin(uint productId, string memory purportedOrigin) public view returns(bool) {
        return keccak256(abi.encodePacked(productRegistry[productId].originLocation)) == keccak256(abi.encodePacked(purportedOrigin));
    }

    function transferCustody(uint productId, address newHolder) public isCurrentHolder(productId) {
        Product storage product = productRegistry[productId];
        product.currentHolder = newHolder;
        emit CustodyTransferred(productId, newHolder);
    }
}