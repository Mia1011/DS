--
-- @lc app=leetcode id=596 lang=mysql
--
-- [596] Classes More Than 5 Students
--

-- @lc code=start
# Write your MySQL query statement below
SELECT class
FROM Courses
GROUP BY class
HAVING count(student) >= 5

/* Debug: 
用HAVING而非WHERE，是因為後面的條件會隨著GROUP BY變動～
WHERE只用來判斷單一條件，用於沒有GROUP的時候。
HAVING用來判斷聚合條件，要放在GROUP BY後面！
*/
-- @lc code=end

