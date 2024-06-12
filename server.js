require('dotenv').config();
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

let products = [
    { id: 1, name: 'Product A', category: 'Electronics', quantity: 100 },
    { id: 2, name: 'Product B', category: 'Clothing', quantity: 200 }
];

let shipments = [
    { id: 1, product_id: 1, quantity: 20, destination: 'New York' },
    { id: 2, product_id: 2, quantity: 30, destination: 'California' }
];

app.get('/api/users', (req, res) => {
    res.json([{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }]);
});

app.get('/api/products', (req, res) => {
    res.json(products);
});

app.post('/api/products', (req, res) => {
    const { name, category, quantity } = req.body;
    if (!name || !category || !quantity) {
        return res.status(400).json({ error: "Please provide name, category, and quantity for the product." });
    }
    const newProduct = {
        id: products.length + 1,
        name,
        category,
        quantity
    };
    products.push(newProduct);
    res.status(201).json(newProduct);
});

app.get('/api/shipments', (req, res) => {
    res.json(shipments);
});

app.post('/api/shipments', (req, res) => {
    const { product_id, quantity, destination } = req.body;
    if (!product_id || !quantity || !destination) {
        return res.status(400).json({ error: "Please provide product_id, quantity, and destination for the shipment." });
    }
    const newShipment = {
        id: shipments.length + 1,
        product_id,
        quantity,
        destination
    };
    shipments.push(newShipment);
    res.status(201).json(newShipment);
});

app.post('/api/batch/products', (req, res) => {
    const productsToAdd = req.body.products;
    if (!productsToAdd || !productsToAdd.length) {
        return res.status(400).json({ error: "Please provide an array of products." });
    }
    productsToAdd.forEach(product => {
        if (!product.name || !product.category || !product.quantity) {
            return; // This silently ignores invalid products; consider adding more robust error handling
        }
        const newProduct = {
            id: products.length + 1,
            name: product.name,
            category: product.category,
            quantity: product.quantity
        };
        products.push(newProduct);
    });
    res.status(201).json({ message: "Products added successfully", addedCount: productsToAdd.length });
});

app.post('/api/batch/shipments', (req, res) => {
    const shipmentsToAdd = req.body.shipments;
    if (!shipmentsToAdd || !shipmentsToAdd.length) {
        return res.status(400).json({ error: "Please provide an array of shipments." });
    }
    shipmentsToAdd.forEach(shipment => {
        if (!shipment.product_id || !shipment.quantity || !shipment.destination) {
            return; // This silently ignores invalid shipments; consider adding more robust error handling
        }
        const newShipment = {
            id: shipments.length + 1,
            product_id: shipment.product_id,
            quantity: shipment.quantity,
            destination: shipment.destination
        };
        shipments.push(newShipment);
    });
    res.status(201).json({ message: "Shipments added successfully", addedCount: shipmentsToAdd.length });
});

app.use((req, res, next) => {
    res.status(404).send('Endpoint not found!');
});

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});