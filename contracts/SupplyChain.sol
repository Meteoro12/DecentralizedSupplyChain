pragma solidity ^0.8.0;

contract DecentralizedSupplyChain {
    struct Product {
        uint id;
        string name;
        string originLocation;
        address owner;
        bool shippedStatus;
    }

    mapping(uint => Product) public productRegister;
    uint public totalProducts;

    event ProductRegistered(uint productId, string name, string originLocation, address indexed owner);
    event ShipmentStatusUpdated(uint productId, bool shippedStatus);
    event OwnershipTransferred(uint productId, address indexed newOwner);

    modifier isProductOwner(uint productId) {
        require(msg.sender == productRegister[productId].owner, "Caller is not the product owner");
        _;
    }

    function registerProduct(string memory productName, string memory originLocation) public {
        totalProducts++;
        productRegister[totalProducts] = Product(totalProducts, productName, originLocation, msg.sender, false);
        emit ProductRegistered(totalProducts, productName, originLocation, msg.sender);
    }

    function updateProductShipment(uint productId, bool newShippedStatus) public isProductOwner(productId) {
        Product storage product = productRegister[productId];
        product.shippedStatus = newShippedStatus;
        emit ShipmentStatusUpdated(productId, newShippedStatus);
    }

    function confirmProductOrigin(uint productId, string memory originToVerify) public view returns(bool) {
        return keccak256(abi.encodePacked(productRegister[productId].originLocation)) == keccak256(abi.encodePacked(originToVerify));
    }

    function changeProductOwner(uint productId, address newOwner) public isProductOwner(productId) {
        Product storage product = productRegister[productId];
        product.owner = newOwner;
        emit OwnershipTransferred(productId, newOwner);
    }
}