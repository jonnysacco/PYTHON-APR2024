-- insert users
INSERT INTO users (username, phone_number, email)
VALUES('Pepper', '1112223333', 'pepper@cat.com');

INSERT INTO users (username, phone_number, email)
VALUES('Heidi', '1112223333', 'heidi@anything.com'), 
('Alex', '1112223333', 'alex@miller.com'), 
('John', '1112223333', 'john@doe.com');

SELECT * FROM users;

-- Adding a donation with a foreign key: donor_id
INSERT INTO donations(item_name, quantity, available_date, description, donor_id)
VALUES ('jeans', 3, '2024-04-09', 'Good conditions! ', 3);

INSERT INTO donations(item_name, quantity, available_date, description, donor_id)
VALUES ('TV', 1, '2024-04-05', 'It works!', 2),
 ('Black belt', 27, '2024-04-20', 'Good for coding dojo', 2),
 ('Cat food', 24, '2024-04-05', 'Very fishy', 1);


SELECT * FROM donations;

SELECT donations.id, item_name, quantity, users.id, users.username
FROM donations
LEFT JOIN users ON donations.donor_id = users.id;


-- UPDATE
-- Update the id 2 donation: for quantity & donor_id
UPDATE donations 
SET quantity = 2, donor_id = 1      -- What to update
WHERE id = 2;


-- DELETE
-- DELETE the item with ID 4
DELETE FROM donations
WHERE id = 4;

-- Can I delete John if he is not any donor
DELETE FROM users
WHERE id = 4;

DELETE FROM users
WHERE id = 1;


