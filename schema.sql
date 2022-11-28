CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    grade FLOAT DEFAULT 0
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    grade INTEGER,
    message TEXT,
    restaurant_id INTEGER REFERENCES restaurants ON DELETE CASCADE,
    sent_at TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
