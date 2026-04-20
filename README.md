# EVerest EVSE Integration Project

## Overview
This project demonstrates the integration of the EVerest EVSE simulator with MQTT communication, a Node-RED dashboard for control, and a basic Python-based OCPP backend.

## Features
- EVSE control using Node-RED dashboard
- MQTT-based communication with EVerest
- Command-line control using mosquitto_pub and mosquitto_sub
- Basic OCPP backend implemented in Python
- Handling of core OCPP messages (BootNotification, Heartbeat, StatusNotification)
- Real-time EVSE state display on dashboard

## Components
- EVerest Simulator (SIL mode)
- Mosquitto MQTT Broker
- Node-RED Dashboard
- Python OCPP Server

## Project Files
- ocpp_server.py → Python-based OCPP backend server
- flows.json → Node-RED dashboard flow for EVSE control
- README.md → Project documentation

## How to Run

1. Start MQTT Broker:
sudo systemctl start mosquitto

2. Run OCPP Server:
python3 ocpp_server.py

3. Run EVerest:
manager --config <config-file>

4. Start Node-RED (Optional):
Open http://localhost:1880  
Import flows.json  
Use dashboard to control EVSE  

## Outcome
- Successfully controlled EVSE using both UI and MQTT commands  
- Established communication between EVerest and backend server  
- Verified real-time message exchange  

## Status
Custom module development in EVerest is pending.
