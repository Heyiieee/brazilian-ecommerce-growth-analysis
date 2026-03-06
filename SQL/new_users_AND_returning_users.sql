-- 每月新、老客数量及占比
WITH first_order AS (
    SELECT
        c.customer_unique_id,
        MIN(o.order_purchase_timestamp) AS first_date
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_unique_id
)

SELECT
    DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,

    COUNT(DISTINCT c.customer_unique_id) AS total_users,

    COUNT(DISTINCT CASE
        WHEN DATE_FORMAT(f.first_date, '%Y-%m') =
             DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m')
        THEN c.customer_unique_id
    END) AS new_users,

    COUNT(DISTINCT CASE
        WHEN DATE_FORMAT(f.first_date, '%Y-%m') <
             DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m')
        THEN c.customer_unique_id
    END) AS returning_users,

    COUNT(DISTINCT CASE
        WHEN DATE_FORMAT(f.first_date, '%Y-%m') =
             DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m')
        THEN c.customer_unique_id
    END)
    /
    COUNT(DISTINCT c.customer_unique_id) AS new_user_ratio,

    COUNT(DISTINCT CASE
        WHEN DATE_FORMAT(f.first_date, '%Y-%m') <
             DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m')
        THEN c.customer_unique_id
    END)
    /
    COUNT(DISTINCT c.customer_unique_id) AS returning_user_ratio

FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN first_order f
    ON c.customer_unique_id = f.customer_unique_id

WHERE o.order_status = 'delivered'

GROUP BY month
ORDER BY month;