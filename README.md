# Author
Edmound Njoori


# Date
11/06/2024

# Store Management System

## Problem Statement
Many small to medium-sized businesses struggle with manual inventory management processes, which are prone to errors, inefficiencies, and delays. These businesses need an automated system to streamline their inventory management, allowing for real-time tracking of stock levels, efficient order processing, and accurate record-keeping.

## Solution
- Maintain accurate records of product quantities in stock, ensuring real-time updates when items are added, sold, or restocked.
- Facilitate the creation, tracking, and management of customer orders.
- Keep detailed records of customers and suppliers, allowing for efficient order processing and communication.
- Provide insights into inventory levels, sales trends, and order histories to inform business decisions.

## Project Description
An effective Store Management System is essential for businesses to streamline their operations, reduce costs, and enhance customer satisfaction. This project aims to develop a robust system that meets these needs, leveraging modern technologies and best practices in software development.

### System Components
The system consists of four main tables:
1. **Customer**: Stores customer details like customer ID, name, and email.
2. **Order**: Stores order details including order ID, customer ID (foreign key), and order date.
3. **Product**: Stores product details such as product ID, name, and price.
4. **OrderItem**: Stores the relationship between orders and products, including order ID, product ID, and quantity. This table uses a composite primary key.

### Table Definitions

#### Customer
- **Primary Key**: `customer_id`
- **Columns**:
  - `customer_id`: INTEGER, PRIMARY KEY
  - `name`: TEXT
  - `email`: TEXT

#### Product
- **Primary Key**: `product_id`
- **Columns**:
  - `product_id`: INTEGER, PRIMARY KEY
  - `name`: TEXT
  - `price`: REAL

#### Order
- **Composite Primary Key**: (`order_id`, `product_id`)
- **Foreign Keys**: 
  - `order_id` (references `Order.order_id`)
  - `product_id` (references `Product.product_id`)
- **Columns**:
  - `order_id`: INTEGER, FOREIGN KEY, PART OF COMPOSITE KEY
  - `product_id`: INTEGER, FOREIGN KEY, PART OF COMPOSITE KEY
  - `quantity`: INTEGER