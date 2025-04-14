CREATE TABLE IF NOT EXISTS ambulances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    status TEXT DEFAULT 'available'
);
