-- Schema para S&BM (PostgreSQL)

CREATE TABLE IF NOT EXISTS client (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS plan (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL CHECK (price > 0),
    frequency VARCHAR(20) NOT NULL CHECK (frequency IN ('monthly', 'yearly')),
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'inactive'))
);

CREATE TABLE IF NOT EXISTS subscription (
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES client(id),
    plan_id INTEGER NOT NULL REFERENCES plan(id),
    date_start DATE NOT NULL,
    date_end DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    cancellation_requested BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS invoice (
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES client(id),
    broadcast DATE NOT NULL,
    expiration DATE NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS payment (
    id SERIAL PRIMARY KEY,
    invoice_id INTEGER NOT NULL REFERENCES invoice(id),
    date DATE NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    method VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL
);
