# app.py
from flask import Flask, render_template, jsonify
from weather_api.weather_service import fetch_weather_data
from database.db import init_db, store_weather_data, get_daily_weather_summary
from utils.helper_functions import kelvin_to_celsius, check_alert_threshold
import time

app = Flask(__name__)

@app.before_first_request
def setup():
    """Initialize the database when the app starts."""
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/trigger_alert/<city>', methods=['GET'])
def trigger_alert(city):
    """API endpoint to trigger an alert for a specific city."""
    weather_data = fetch_weather_data(city)
    if weather_data:
        temperature_k = weather_data['main']['temp']
        temperature_c = kelvin_to_celsius(temperature_k)
        weather = weather_data['weather'][0]['main']
        timestamp = int(time.time())

        # Store the weather data
        store_weather_data(city, temperature_c, weather, timestamp)

        # Check if the temperature exceeds the threshold
        alert_threshold = 35  # Example threshold
        alert_triggered = check_alert_threshold(temperature_c, alert_threshold)

        return jsonify({
            'city': city,
            'temperature': temperature_c,
            'weather': weather,
            'alert_triggered': alert_triggered
        })
    else:
        return jsonify({"error": "Failed to retrieve weather data."}), 500

if __name__ == '__main__':
    app.run(debug=True)
