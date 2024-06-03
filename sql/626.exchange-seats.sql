--
-- @lc app=leetcode id=626 lang=mysql
--
-- [626] Exchange Seats
--

-- @lc code=start
# Write your MySQL query statement below
SELECT 
CASE
    WHEN id % 2 = 1 AND id = (select count(student) from Seat) THEN id # do nothing
    WHEN id % 2 = 1 THEN id+1
    ELSE id-1
END as id, student
FROM Seat
ORDER BY id

# 要寫(select count(student) from Seat)，不能只寫count(student)。
# 但為什麼....?

-- @lc code=end

