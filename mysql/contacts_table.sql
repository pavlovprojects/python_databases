CREATE TABLE IF NOT EXISTS contacts (
    id INT(32) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) UNIQUE NOT NULL,
    email varchar(255),
    phone varchar(255) NOT NULL,
    adress varchar(255)
);
