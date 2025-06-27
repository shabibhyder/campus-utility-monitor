from flask import Flask, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
import random
import time

app = Flask(__name__)

# Gauges simulate metrics (labels allow per-building metrics)
power_usage = Gauge('campus_power_usage', 'Power usage in kWh', ['building'])
water_usage = Gauge('campus_water_usage', 'Water usage in liters', ['building'])
co2_level = Gauge('campus_air_co2', 'CO2 level in ppm', ['building'])

buildings = ['library', 'lab', 'gym', 'dorm', 'admin']

@app.route("/metrics")
def metrics():
    for building in buildings:
        power_usage.labels(building=building).set(random.uniform(50, 200))
        water_usage.labels(building=building).set(random.uniform(100, 500))
        co2_level.labels(building=building).set(random.uniform(350, 600))
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/")
def home():
    return "Campus Utility Exporter Running. Visit /metrics to see metrics."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
