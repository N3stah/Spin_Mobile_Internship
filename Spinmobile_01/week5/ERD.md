# Retail ERD

## Entities & Attributes

### Customers
- id (PK)
- name
- email (unique)
- phone

### Products
- id (PK)
- name
- price
- stock_quantity

### Orders
- id (PK)
- customer_id (FK → Customers.id)
- order_date
- status

### Order_Items (junction table for Orders <-> Products)
- order_id (FK → Orders.id)
- product_id (FK → Products.id)
- quantity
- unit_price_at_purchase

## Relationships

- Customers 1:N Orders — one customer can place many orders, each order belongs to exactly one customer
- Orders N:M Products (resolved via Order_Items) — one order can contain many products, one product can appear in many orders