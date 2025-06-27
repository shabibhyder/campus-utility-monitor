# Campus Utility Monitor

This project implements a real-time monitoring system for campus utilities, including power usage, water consumption, and CO2 levels, broken down by building. It uses Python to simulate and expose metrics, Prometheus to scrape and store the data, and Grafana to visualize it.

---

## Features

- Simulates power usage (kWh), water usage (liters), and CO2 levels (ppm) for different campus buildings.
- Provides a Python Flask exporter exposing metrics in Prometheus format.
- Prometheus scrapes metrics every 15 seconds.
- Grafana dashboards visualize the metrics for easy monitoring.
- Fully containerized with Docker and orchestrated with Docker Compose.
- Designed to be extensible for real-world data integration.

---

## Technology Stack

- Python 3.12  
- Flask  
- prometheus_client library  
- Prometheus  
- Grafana
- Docker and docker compose

---

## Setup Instructions

### Prerequisites

- Python 3.12 or later  
- Prometheus  
- Grafana  

### Steps to run

1. Clone the repository:

   ```bash
   git clone https://github.com/shabibhyder/campus-utility-monitor.git
   cd campus-utility-monitor

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   
3. Install Python dependencies:
pip install -r requirements.txt

4. Start the python exporter
   python exporter/app.py
   
6. Configure Prometheus to scrape metrics from localhost:8000 by editing prometheus.yml and restarting Prometheus.
7. Start Grafana, add Prometheus (http://localhost:9090) as a data source, and create dashboards to visualize the metrics.


