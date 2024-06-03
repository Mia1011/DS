--
-- @lc app=leetcode id=1070 lang=mysql
--
-- [1070] Product Sales Analysis III
--

-- @lc code=start
# Write your MySQL query statement below
SELECT product_id, year as first_year, quantity, price
FROM Sales
WHERE (product_id, year) in (
    SELECT product_id, min(year)
    FROM Sales
    GROUP BY product_id
)

/* debug: 
WHERE裡面不能只放year，因為是用in判斷的，如果只放year可能會有多個結果（？反正我測了都是錯的。
同時用product_id和year判斷，因為是primary key，才能肯定只有一種結果。
*/

-- @lc code=end

