# SIC_stage2_ZFlip4

## Overview
This project integrates **LDR, PIR Motion, and DHT sensors** with an **ESP32** to collect environmental data and send it to **Ubidots** for visualization. The backend is built using **Flask** and stores data in **MongoDB**.

## Features
- **ESP32 MicroPython Script** to read data from LDR, PIR Motion, and DHT sensors.
- **Data Transmission** via REST API to Ubidots.
- **Ubidots Dashboard** with 4 visualizations (Thermometer, Gauge, Indicator widget, Line chart).
- **Flask API** to store sensor data in MongoDB for further processing.

## Setup Guide
### 1. ESP32 Setup
1. Install MicroPython on ESP32.
2. Upload the script to read sensor data and send it to Ubidots.
3. Configure Wi-Fi credentials and Ubidots API key.

### 2. Flask Backend Setup
1. Install dependencies:
   ```bash
   pip install flask pymongo
   ```
2. Run the Flask server:
   ```bash
   python app.py
   ```

### 3. Ubidots Dashboard
1. Create an Ubidots account.
2. Add new variables for LDR, PIR, and DHT.
3. Set up visualizations.
