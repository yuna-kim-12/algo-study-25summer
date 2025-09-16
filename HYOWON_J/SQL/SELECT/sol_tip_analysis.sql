SELECT day, time, ROUND(SUM(tip)/COUNT(tip),2) as avg_tip, ROUND(SUM(size)/COUNT(size), 2) as avg_size
FROM tips
GROUP BY day, time
ORDER BY day, time