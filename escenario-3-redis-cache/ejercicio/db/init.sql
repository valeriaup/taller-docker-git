CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO usuarios (nombre, email) VALUES
    ('Ana', 'ana@test.com'),
    ('Luis', 'luis@test.com')
ON CONFLICT (email) DO NOTHING;