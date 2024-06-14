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

    event ProductAdded(uint productId, string name, string origin, address indexed owner);
    event ProductShipmentUpdated(uint productId, bool isShipped);
    event ProductOwnershipTransferred(uint productId, address indexed newOwner);

    modifier onlyOwner(uint _productId) {
        require(msg.sender == products[_productId].currentOwner, "Not the product's owner");
        _;
    }

    function addProduct(string memory _name, string memory _origin) public {
        productCount ++;
        products[productCount] = Product(productCount, _name, _origin, msg.sender, false);
        emit ProductAdded(productCount, _name, _origin, msg.sender);
    }

    function updateShipmentStatus(uint _productId, bool _isShipped) public onlyOwner(_productId) {
        Product storage product = products[_productId];
        product.isShipped = _isShipped;
        emit ProductShipmentUpdated(_productId, _isShipped);
    }

    function verifyProductOrigin(uint _productId, string memory _origin) public view returns(bool) {
        return keccak256(abi.encodePacked(products[_productId].origin)) == keccak256(abi.encodePacked(_origin));
    }

    function transferOwnership(uint _productId, address _newOwner) public onlyOwner(_productId) {
        Product storage product = products[_productId];
        product.currentOwner = _newOwner;
        emit ProductOwnershipTransferred(_productId, _newOwner);
    }
}