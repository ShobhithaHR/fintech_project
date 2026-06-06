-- 1 Top 5 Funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV

SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3 NAV by AMFI Code

SELECT amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 4 SIP Transactions

SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP';

-- 5 Transactions by State

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 6 Total Investment Amount by State

SELECT state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 7 Funds with Expense Ratio < 1

SELECT amfi_code,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 8 Top 5 Funds by 5-Year Return

SELECT amfi_code,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 9 Average Expense Ratio

SELECT AVG(expense_ratio_pct)
AS avg_expense_ratio
FROM fact_performance;

-- 10 KYC Status Distribution

SELECT kyc_status,
COUNT(*)
FROM fact_transactions
GROUP BY kyc_status;