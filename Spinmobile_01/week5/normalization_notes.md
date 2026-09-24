# Normalization Walkthrough

## Starting Point — Unnormalized Flat Table

| order_id | customer_name | customer_email | product_names | quantities |
|---|---|---|---|---|
| 1 | Mark Manoti | mark@example.com | Wireless Mouse, USB-C Cable | 2, 1 |
| 2 | Mark Manoti | mark@example.com | Keyboard | 1 |

Problems with this table:
- `product_names` and `quantities` each hold MULTIPLE values in one cell — violates 1NF.
- `customer_name` and `customer_email` are repeated on every order row for the same customer — redundant data, update anomaly risk.

## Step 1 — Apply 1NF (atomic values only)
Split multi-value cells into one row per order-product combination. Every cell now holds a single atomic value.

## Step 2 — Apply 2NF (remove partial dependencies)
Separate customer information into its own `customers` table, since it depends on the customer rather than the composite key.

## Step 3 — Apply 3NF (remove transitive dependencies)
Separate product details into a `products` table and use the `order_items` junction table to connect orders and products.