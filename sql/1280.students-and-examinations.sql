--
-- @lc app=leetcode id=1280 lang=mysql
--
-- [1280] Students and Examinations
--

-- @lc code=start
# Write your MySQL query statement below
# Sol 1
SELECT T1.student_id, T1.student_name, T2.subject_name, 
    count(T3.subject_name) as attended_exams
FROM Students T1
CROSS JOIN Subjects T2 
LEFT JOIN Examinations T3 
    ON T1.student_id = T3.student_id AND T2.subject_name = T3.subject_name
GROUP BY T1.student_id, T2.subject_name
ORDER BY T1.student_id, T2.subject_name

/*
# Sol 2
SELECT T1.student_id, T1.student_name, T2.subject_name, 
    count(T3.subject_name) as attended_exams
FROM Students T1, Subjects T2, Examinations T3 
WHERE T1.student_id = T3.student_id AND T2.subject_name = T3.subject_name
GROUP BY T1.student_id, T2.subject_name
ORDER BY T1.student_id, T2.subject_name
# exclude all the nulls..... */
-- @lc code=end

