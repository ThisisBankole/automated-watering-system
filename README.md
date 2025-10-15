# Automated Watering System

This project uses M5Stack devices (see details under hardware requirements) to build an automated watering system that monitors environmental conditions and soil moisture, and controls a water pump accordingly. I built this for one of my plants as a proof of concept. I plan to repeat the process for the others. 



![IMG_5480](https://github.com/user-attachments/assets/761b863a-3946-45b1-a770-c48ed9b88c29)

I will update the repo with both the picture and OpenSCAD code for the 3d printed stand some time in the future. 

## Features

- **Environmental Sensing:** Reads temperature, humidity, and pressure using the ENV3 sensor module.
- **Soil Moisture Sensing:** Monitors soil moisture via the WATERING unit.
- **Automated Watering:** Activates the water pump automatically when soil moisture drops below a user-defined threshold.
- **Manual Control:** Includes a UI switch for manual control of the water pump.
- **Live Display:** Shows live environmental and soil readings on the M5Stack screen.

## Hardware Requirements

- M5Stack Core device
- ENV3 sensor (connected to PORTA)
- WATERING unit (connected to PORTB)

## How It Works

1. **Setup:** The device initializes the display and sensor modules.
2. **Measurement:** It continuously reads temperature, humidity, pressure, and soil moisture.
3. **Display:** All readings are shown on the screen.
4. **Watering Logic:** If soil moisture drops below 10% (adjustable threshold), the water pump turns on; otherwise, it remains off.
5. **Manual Override:** Use the UI switch to manually start or stop the pump.

## Usage

Flash the `watering_system.py` script to your M5Stack device. Connect the ENV3 and WATERING units to the correct ports. Power on the device to start monitoring and automatic watering.

## Customization

- The soil moisture threshold can be adjusted in the code by changing the value in the logic (`if soilPercentage <= 10:`).
- Min/max values for calibration (`minValue`, `maxValue`) may need to be tweaked per your soil and sensor setup.

## Code Overview

See [`watering_system.py`](https://github.com/ThisisBankole/automated-watering-system/blob/main/watering_system.py) for the complete implementation.

## License

MIT License (or specify your preferred license here)
