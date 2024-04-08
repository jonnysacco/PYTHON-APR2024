# Using our own schema

## 0. Create the ERD on MySQL workbench
- Look at the wireframe and decide on the database structure (Create a draft on your own)
- Click on the ERD button and add a diagram 
- Build all the tables & relationships 

## 1. Forward engineer & Reverse engineer
- ERD is just a visual representation of the database. Creating the models does not create the schema. 
- Forward engineer : Create the schema based on ERD
- Reverse engineer : Create the ERD based on the schema

## 2. INSERT
### INSERT ONE RECORD
```sql
    INSERT INTO table_name (column_name1, column_name2) 
    VALUES('column1_value', 'column2_value');
```

### INSERT MULTIPLE RECORD
```sql
    INSERT INTO users (first_name, last_name, email) 
    VALUES('Heidi', 'Chen', 'heidi@anything.com') 
    , ('Pepper', 'Chen', 'pepper@cat.com');
```

## 3. UPDATE
```sql
    UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
```
