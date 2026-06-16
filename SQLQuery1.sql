use data_bank;
--A. Customer Nodes Exploration How many unique nodes are there on the Data Bank system? 
--What is the number of nodes per region? 
--How many customers are allocated to each region? 
--How many days on average are customers reallocated to a different node? 
--What is the median, 80th and 95th percentile for this same reallocation days metric for each region? 
SELECT COUNT(DISTINCT node_id) AS unique_nodes
FROM customer_nodes;

SELECT
    r.region_name,
    COUNT(DISTINCT cn.node_id) AS number_of_nodes
FROM customer_nodes cn
JOIN regions r
    ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;

SELECT
    r.region_name,
    COUNT(DISTINCT cn.customer_id) AS customer_count
FROM customer_nodes cn
JOIN regions r
    ON cn.region_id = r.region_id
GROUP BY r.region_name
ORDER BY r.region_name;

SELECT
    AVG(end_date - start_date) AS avg_reallocation_days
FROM customer_nodes
WHERE end_date != '9999-12-31';

WITH reallocation_days AS (
    SELECT
        r.region_name,
        DATEDIFF(DAY, cn.start_date, cn.end_date) AS days_diff
    FROM customer_nodes cn
    JOIN regions r
        ON cn.region_id = r.region_id
    WHERE cn.end_date <> '9999-12-31'
)

SELECT DISTINCT
    region_name,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY days_diff)
        OVER (PARTITION BY region_name) AS median,
    PERCENTILE_CONT(0.8) WITHIN GROUP (ORDER BY days_diff)
        OVER (PARTITION BY region_name) AS percentile_80,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY days_diff)
        OVER (PARTITION BY region_name) AS percentile_95
FROM reallocation_days
ORDER BY region_name;

--B. Customer Transactions What is the unique count and total amount for each transaction type? 
--What is the average total historical deposit counts and amounts for all customers? 
--For each month - how many Data Bank customers make more than 1 deposit and either 1 purchase or 1 withdrawal in a single month?
SELECT
    txn_type,
    COUNT(*) AS unique_count,
    SUM(txn_amount) AS total_amount
FROM customer_transactions
GROUP BY txn_type
ORDER BY txn_type;

SELECT
    AVG(deposit_count) AS avg_deposit_count,
    AVG(total_amount) AS avg_deposit_amount
FROM (
    SELECT
        customer_id,
        COUNT(*) AS deposit_count,
        SUM(txn_amount) AS total_amount
    FROM customer_transactions
    WHERE txn_type = 'deposit'
    GROUP BY customer_id
) t;

