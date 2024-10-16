# database/db.py

import sqlite3

def init_db():
    """Initialize the weather database and create tables if they don't exist."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL NOT NULL,
            weather TEXT NOT NULL,
            timestamp INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def store_weather_data(city, temperature, weather, timestamp):
    """Store the retrieved weather data in the database."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('INSERT INTO weather_data (city, temperature, weather, timestamp) VALUES (?, ?, ?, ?)',
              (city, temperature, weather, timestamp))
    conn.commit()
    conn.close()

def get_daily_weather_summary(city, day):
    """Retrieve the weather data and calculate daily aggregates for the given city and day."""
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        SELECT AVG(temperature), MIN(temperature), MAX(temperature), weather 
        FROM weather_data 
        WHERE city = ? AND DATE(timestamp, 'unixepoch') = ?
    ''', (city, day))
    summary = c.fetchone()
    conn.close()
    return summary
