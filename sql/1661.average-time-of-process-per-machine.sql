--
-- @lc app=leetcode id=1661 lang=mysql
--
-- [1661] Average Time of Process per Machine
--

-- @lc code=start
# Write your MySQL query statement below
/*
# Sol_1
SELECT A1.machine_id, 
    round((SELECT avg(A2.timestamp) FROM Activity A2 WHERE A2.activity_type='end' AND A1.machine_id=A2.machine_id)
        - (SELECT avg(A2.timestamp) FROM Activity A2 WHERE A2.activity_type='start' AND A1.machine_id=A2.machine_id), 3)
    as processing_time
FROM Activity A1
GROUP BY A1.machine_id;
*/

# Sol_2
SELECT A1.machine_id, round(avg(A2.timestamp - A1.timestamp), 3) as processing_time
FROM Activity A1
JOIN Activity A2 
ON A1.machine_id = A2.machine_id and 
   A1.process_id = A2.process_id and
   A1.activity_type = "start" and A2.activity_type = "end"
GROUP BY A1.machine_id
-- @lc code=end

