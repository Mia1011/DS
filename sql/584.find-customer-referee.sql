--
-- @lc app=leetcode id=584 lang=mysql
--
-- [584] Find Customer Referee
--

-- @lc code=start
# Write your MySQL query statement below
SELECT name
FROM Customer
#WHERE referee_id != 2 OR referee_id is null;  
# or...
WHERE id not in (select id from Customer where referee_id = 2);
-- @lc code=end

