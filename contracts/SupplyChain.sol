// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DecentralizedSupplyChain {
    struct Product {
        uint id;
        string name;
        string origin;
        address currentOwner;
        bool isShipped;
    }

    mapping(uint => Product) public products;
    uint public productCount;

    event ProductAdded(uint productId, string productName, string productOrigin, address indexed owner);
    event ShippingStatusUpdated(uint productId, bool isShipped);
    event OwnerUpdated(uint productId, address indexed newOwner);

    modifier onlyProductOwner(uint productId) {
        require(msg.sender == products[productId].currentOwner, "Caller is not the product owner");
        _;
    }

    function addProduct(string memory name, string memory origin) public {
        productCount++;
        products[productCount] = Product(productCount, name, origin, msg.sender, false);
        emit ProductAdded(productCount, name, origin, msg.sender);
    }

    function setShippingStatus(uint productId, bool shipped) public onlyProductOwner(productId) {
        Product storage product = products[productId];
        product.isShipped = shipped;
        emit ShippingStatusUpdated(productId, shipped);
    }

    function verifyProductOrigin(uint productId, string memory originVerification) public view returns(bool) {
        return keccak256(abi.encodePacked(products[productId].origin)) == keccak256(abi.encodePacked(originVerification));
    }

    function updateOwner(uint productId, address newOwner) public onlyProductOwner(productId) {
        Product storage product = products[productId];
        product.currentOwner = newOwner;
        emit OwnerUpdated(productId, newOwner);
    }
}