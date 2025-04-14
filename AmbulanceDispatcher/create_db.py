import sqlite3

# Connect to the database (will create if it doesn't exist)
conn = sqlite3.connect('dispatcher.db')
cursor = conn.cursor()

# Create Hospitals table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hospitals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL
    )
''')

# Create Ambulances table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ambulances (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hospital_id INTEGER,
        status TEXT NOT NULL,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL,
        FOREIGN KEY(hospital_id) REFERENCES hospitals(id)
    )
''')

# Optional: Insert sample data
cursor.execute("INSERT INTO hospitals (name, latitude, longitude) VALUES (?, ?, ?)", ("City Hospital", 1.0, 2.0))
cursor.execute("INSERT INTO hospitals (name, latitude, longitude) VALUES (?, ?, ?)", ("Metro Hospital", 5.0, 5.0))

cursor.execute("INSERT INTO ambulances (hospital_id, status, latitude, longitude) VALUES (?, ?, ?, ?)", (1, "available", 2.0, 3.0))
cursor.execute("INSERT INTO ambulances (hospital_id, status, latitude, longitude) VALUES (?, ?, ?, ?)", (2, "available", 6.0, 1.0))
cursor.execute("INSERT INTO ambulances (hospital_id, status, latitude, longitude) VALUES (?, ?, ?, ?)", (2, "busy", 7.0, 8.0))

# Commit and close
conn.commit()
conn.close()

print("Database created and sample data inserted.")
