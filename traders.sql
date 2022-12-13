WITH trader_volume_2022 as (
SELECT 
    MAX(block_time) AS last_trade,
    CONCAT('0x', ENCODE(trader, 'hex')) as trader,
    SUM(trade_value_usd) AS usd_volume_2022
FROM gnosis_protocol_v2.trades
WHERE block_time between '2022-01-01' and '2023-01-01'
GROUP BY trader)

SELECT trader, usd_volume_2022
FROM trader_volume_2022
WHERE usd_volume_2022 > 50
ORDER BY usd_volume_2022 DESC