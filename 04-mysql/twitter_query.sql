use twitter;

-- Basic Queries
SELECT id, first_name, last_name 
FROM users 
ORDER BY first_name;

-- Conditions
-- Get all the tweets from user_id :2 
SELECT *
FROM tweets
WHERE user_id = 2;

-- Get all the tweets that are created after 2010
SELECT *
FROM tweets
WHERE created_at >= "2010-01-01";

-- Get all the tweets that are created after 2010 OR before 2005
SELECT *
FROM tweets
WHERE created_at >= "2010-01-01"
OR created_at <= "2005-01-01";

-- Get all the tweets that contains k in tweet
SELECT * FROM tweets 
WHERE tweet LIKE "%k%";

-- TOP recent 3 tweets
SELECT * 
FROM tweets
ORDER BY created_at DESC
LIMIT 3;


-- SHOW all users_id and their number of tweets
SELECT user_id, count(tweet)
FROM tweets
GROUP BY user_id
HAVING count(tweet) > 2;


-- JOIN TABLES
-- THIS COULD WORK!!! 
SELECT tweets.id, tweets.tweet, tweets.user_id, users.id, users.handle
FROM tweets, users
WHERE users.id = tweets.user_id;

-- Using JOIN makes it more neat and more functionality in LEFT JOIN/RIGHT JOIN/JOIN 
SELECT tweets.id, tweets.tweet, tweets.user_id, users.id, users.handle
FROM tweets
LEFT JOIN users ON users.id = tweets.user_id;








