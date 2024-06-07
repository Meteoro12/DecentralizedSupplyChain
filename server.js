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
    const newShipment = {
        id: shipments.length + 1,
        product_id,
        quantity,
        destination
    };
    shipments.push(newShipment);
    res.status(201).json(newShipment);
});

app.use((req, res, next) => {
    res.status(404).send('Endpoint not found!');
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});