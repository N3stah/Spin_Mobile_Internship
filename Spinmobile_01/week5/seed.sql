INSERT INTO customers (name, email, phone) VALUES
('Mark Manoti', 'mark@example.com', '0712345678'),
('Judy Otieno', 'judy@example.com', '0723456789');

INSERT INTO products (name, price, stock_quantity) VALUES
('Wireless Mouse', 1500.00, 50),
('Keyboard', 3200.00, 30),
('USB-C Cable', 500.00, 100);

INSERT INTO orders (customer_id, status) VALUES
(1, 'completed'),
(1, 'pending'),
(2, 'completed');

INSERT INTO order_items (order_id, product_id, quantity, unit_price_at_purchase) VALUES
(1, 1, 2, 1500.00),
(1, 3, 1, 500.00),
(2, 2, 1, 3200.00),
(3, 1, 1, 1500.00);