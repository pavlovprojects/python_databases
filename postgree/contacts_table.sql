CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    email TEXT,
    phone TEXT NOT NULL,
    adress TEXT
);
