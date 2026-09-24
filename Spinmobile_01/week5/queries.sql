-- Query 1: What did each customer order, with product details?
SELECT
    customers.name AS customer_name,
    orders.order_date,
    orders.status,
    products.name AS product_name,
    order_items.quantity,
    order_items.unit_price_at_purchase
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN order_items ON order_items.order_id = orders.id
JOIN products ON order_items.product_id = products.id
ORDER BY orders.order_date;

-- Query 2: What is the total value of each completed order?
SELECT
    orders.id AS order_id,
    customers.name AS customer_name,
    SUM(order_items.quantity * order_items.unit_price_at_purchase) AS order_total
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN order_items ON order_items.order_id = orders.id
WHERE orders.status = 'completed'
GROUP BY orders.id, customers.name;

-- Query 3: Which products has each customer ever purchased, listed once each?
SELECT DISTINCT
    customers.name AS customer_name,
    products.name AS product_name
FROM customers
JOIN orders ON orders.customer_id = customers.id
JOIN order_items ON order_items.order_id = orders.id
JOIN products ON order_items.product_id = products.id
ORDER BY customers.name, products.name;