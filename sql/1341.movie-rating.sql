--
-- @lc app=leetcode id=1341 lang=mysql
--
-- [1341] Movie Rating
--

-- @lc code=start
# Write your MySQL query statement below
(
SELECT name AS results
FROM Users
JOIN MovieRating USING(user_id)
GROUP BY name
ORDER BY count(user_id) DESC, name
LIMIT 1
)
UNION ALL
(
SELECT title AS results
FROM Movies
JOIN MovieRating USING(movie_id)
WHERE extract(year_month FROM created_at) = "202002"
GROUP BY title
ORDER BY avg(rating) DESC, title
LIMIT 1
)
-- @lc code=end

