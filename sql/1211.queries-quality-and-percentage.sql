--
-- @lc app=leetcode id=1211 lang=mysql
--
-- [1211] Queries Quality and Percentage
--

-- @lc code=start
# Write your MySQL query statement below
SELECT query_name, 
    round(avg(rating/position), 2) as quality, 
    round(sum(CASE WHEN rating<3 THEN 1 ELSE 0 END) / count(*) *100, 2) 
    as poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name

# case when... then... (else...) end
-- @lc code=end

