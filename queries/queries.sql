-- 10000 new contract balance and transaction

SELECT 
  c.address AS smart_contract_address, 
  COUNT(*) AS transaction_count, 
  SUM(value) AS balance
FROM 
  `bigquery-public-data.crypto_ethereum.transactions` AS t
JOIN 
  `bigquery-public-data.crypto_ethereum.contracts` AS c
ON 
  t.to_address = c.address
WHERE 
  t.to_address IS NOT NULL
  AND c.bytecode IS NOT NULL
GROUP BY 
  smart_contract_address
ORDER BY 
  balance DESC
LIMIT 
  10000


-- top 20 contract query
SELECT to_address AS smart_contract_address, COUNT(*) AS tx_count
FROM `bigquery-public-data.crypto_ethereum.transactions`
WHERE to_address IS NOT NULL
GROUP BY to_address
ORDER BY tx_count DESC
LIMIT 20



-- Query for top 20 smart contracts based on transaction count
SELECT to_address AS smart_contract_address, COUNT(*) AS tx_count
FROM `bigquery-public-data.crypto_ethereum.transactions`
WHERE to_address IS NOT NULL
GROUP BY to_address
ORDER BY tx_count DESC
LIMIT 20


-- Top 10000 smart contract based on balance
SELECT to_address AS smart_contract_address, SUM(value) AS balance
FROM `bigquery-public-data.crypto_ethereum.transactions`
WHERE to_address IS NOT NULL
GROUP BY to_address
ORDER BY balance DESC
LIMIT 10000
