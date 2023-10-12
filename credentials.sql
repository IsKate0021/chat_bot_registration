USE MyDB;

CREATE TABLE credentials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255),
    user_password VARCHAR(255),
    user_phone_number VARCHAR(255)
);