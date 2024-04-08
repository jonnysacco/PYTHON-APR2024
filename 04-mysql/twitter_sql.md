# Query Language
## 1.1 Using the right schema
```sql
    use twitter; 
```

## 1.2 Basic Query
### SELECT column_name FROM table_name 
```sql
    SELECT id, first_name, last_name FROM users;
```

## 1.3 ORDER BY
### SELECT column_name1, ... FROM table_name ORDER BY column_name, ...
```sql
    SELECT * FROM users
    ORDER BY first_name DESC;
```

## 2.1 WHERE -- Adding conditions
### Can use =, !=, < , <= , >, >= 
```sql
    SELECT * FROM users
    WHERE id = 3;
```

```sql
    SELECT * FROM users
    WHERE created_at > "2010-01-01";
```

## 2.2 Conditions with String
### LIKE for string match - % for any character length
#### Select all columns from users table if handle begins with R
```sql
    SELECT * FROM users
    WHERE handle LIKE "R%";
```

## 2.3 AND, OR, NOT
### Can AND, OR, NOT for logical operator
#### Select all columns from tweets table if tweet contains "k" and user_id = 2
```sql
    SELECT * FROM tweets
    WHERE tweet LIKE "%k%"
    AND user_id = 2;
```
## 3. Aggregate functions
### GROUP BY & HAVING for aggregate functions
- AVG, COUNT, MAX, MIN, SUM
#### Find user_id and the total tweet they made in tweets table
```sql
    SELECT count(tweet), user_id FROM tweets
    GROUP BY user_id;
```

```sql
    SELECT count(tweet), user_id FROM tweets
    GROUP BY user_id
    HAVING count(tweet) > 2;
```

## 4. Joining Tables (IMPORTANT!)
### JOIN, LEFT JOIN, RIGHT JOIN 
#### Joining two tables but users id (users:PK) needs to match with tweets.user_id (tweets: FK)
```sql
    SELECT tweets.id, tweet, handle as creator FROM tweets
    LEFT JOIN users ON users.id = tweets.user_id;
```

### Joining THREE tables (ADVANCED)
#### Show each tweet and the user handle who liked the tweet
```sql
    SELECT tweets.id, tweets.tweet, users.handle AS liked_by FROM tweets
    LEFT JOIN faves ON faves.tweet_id = tweets.id
    LEFT JOIN users ON users.id = faves.user_id
```







