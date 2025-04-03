-- Create Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    Address VARCHAR(100)
);

-- Create Items table
CREATE TABLE Items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    price DECIMAL(10,2),
    department VARCHAR(50)
);

-- Create Sales table
-- (We include a unique sale_id for each row; sale_date represents the date of completion)
CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    sale_date DATE,
    order_id INT,
    item_id INT,
    customer_id INT,
    quantity INT,
    revenue DECIMAL(10,2)
);

-- Insert sample data into Customers
INSERT INTO Customers (customer_id, first_name, last_name, Address) VALUES
(1, 'John', 'Doe', '123 Main St'),
(2, 'Jane', 'Smith', '456 Elm St'),
(3, 'Alice', 'Johnson', '789 Maple Ave'),
(4, 'John', 'Doe', '321 Oak St');

-- Insert sample data into Items
INSERT INTO Items (item_id, item_name, price, department) VALUES
(101, 'Widget A', 25.00, 'Electronics'),
(102, 'Widget B', 40.00, 'Home'),
(103, 'Widget C', 15.00, 'Toys'),
(104, 'Widget D', 30.00, 'Garden'),
(105, 'Widget E', 100.00, 'Luxury'),
(106, 'Widget F', 20.00, 'Books');

-- Insert sample data into Sales
-- Sales for March 18, 2023
INSERT INTO Sales (sale_id, sale_date, order_id, item_id, customer_id, quantity, revenue) VALUES
(1, '2023-03-18', 1001, 101, 1, 2, 50.00),   -- John Doe (customer_id 1)
(2, '2023-03-18', 1002, 102, 2, 1, 40.00),
(3, '2023-03-18', 1003, 103, 3, 3, 45.00),
(4, '2023-03-18', 1004, 104, 4, 1, 30.00);   -- John Doe (customer_id 4)

-- Sales for January 2023
INSERT INTO Sales (sale_id, sale_date, order_id, item_id, customer_id, quantity, revenue) VALUES
(5, '2023-01-05', 2001, 101, 1, 1, 25.00),
(6, '2023-01-15', 2002, 102, 2, 2, 80.00),
(7, '2023-01-20', 2003, 103, 3, 1, 15.00),
(8, '2023-01-25', 2004, 104, 1, 1, 30.00);

-- Sales for 2022 (to use for department revenue)
INSERT INTO Sales (sale_id, sale_date, order_id, item_id, customer_id, quantity, revenue) VALUES
(9,  '2022-06-10', 3001, 106, 2, 1, 20.00),
(10, '2022-07-15', 3002, 106, 3, 2, 40.00),
(11, '2022-08-20', 3003, 105, 4, 1, 100.00),
(12, '2022-09-25', 3004, 104, 1, 1, 30.00);

SELECT COUNT(DISTINCT order_id) AS total_orders_18Mar2023
FROM Sales
WHERE sale_date = '2023-03-18';

SELECT COUNT(DISTINCT s.order_id) AS total_orders_18Mar2023_JohnDoe
FROM Sales s
JOIN Customers c ON s.customer_id = c.customer_id
WHERE s.sale_date = '2023-03-18'
  AND c.first_name = 'John'
  AND c.last_name = 'Doe';

WITH JanPurchases AS (
  SELECT customer_id, SUM(revenue) AS total_spent
  FROM Sales
  WHERE sale_date BETWEEN '2023-01-01' AND '2023-01-31'
  GROUP BY customer_id
)
SELECT COUNT(*) AS total_customers,
       AVG(total_spent) AS avg_spent_per_customer
FROM JanPurchases;

SELECT i.department, SUM(s.revenue) AS total_revenue
FROM Sales s
JOIN Items i ON s.item_id = i.item_id
WHERE s.sale_date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY i.department
HAVING SUM(s.revenue) < 600;

WITH OrderRevenue AS (
  SELECT order_id, SUM(revenue) AS order_total
  FROM Sales
  GROUP BY order_id
)
SELECT
  (SELECT order_total FROM OrderRevenue ORDER BY order_total DESC LIMIT 1) AS max_order_revenue,
  (SELECT order_total FROM OrderRevenue ORDER BY order_total ASC LIMIT 1) AS min_order_revenue;

WITH OrderRevenue AS (
  SELECT order_id, SUM(revenue) AS order_total
  FROM Sales
  GROUP BY order_id
),
MaxOrder AS (
  SELECT order_id
  FROM OrderRevenue
  ORDER BY order_total DESC
  LIMIT 1
)
SELECT s.*
FROM Sales s
WHERE s.order_id = (SELECT order_id FROM MaxOrder);
