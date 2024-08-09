# User Manual for Smart Home Automation System

## Overview

This system allows you to monitor and control various home appliances remotely using a Raspberry Pi.

## Setup Instructions

1. Connect sensors and actuators to the Raspberry Pi GPIO pins as specified in `gpio_pins.json`.
2. Update the configuration files in the `config/` directory according to your environment.
3. Run `install_dependencies.sh` to install all necessary packages.
4. Run `start_services.sh` to start the system.

## Features

- **Temperature and Humidity Monitoring**: Displays current temperature and humidity levels.
- **Relay Control**: Controls home appliances.
- **Motion Detection**: Alerts when motion is detected.
- **Security Monitoring**: Captures images from a camera.
- **Energy Monitoring**: Shows current energy usage.
- **Voice Control**: Controls appliances using voice commands.

## Troubleshooting

- Ensure all connections are secure.
- Verify that the Raspberry Pi is properly configured.
- Check log files for error messages.
