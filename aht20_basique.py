# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "adafruit-blinka",
#   "adafruit-circuitpython-ahtx0",
#   "adafruit-circuitpython-vcnl4200",
#   "rpi.gpio",
# ]
# ///
"""
Lecture basique du capteur AHT20 (I2C)
Cours 243-4-SH, Semaine 3
"""

import board
import adafruit_ahtx0
import adafruit_vcnl4200

i2c = board.I2C()

capteur = adafruit_ahtx0.AHTx0(i2c)

print("=== Lecture AHT20 ===")
print(f"Adresse I2C : 0x38")
print(f"Adresse VCNL4200 : 0x51")
print()

temperature = capteur.temperature
humidite = capteur.relative_humidity

print(f"Temperature : {temperature:.1f} C")
print(f"Humidite    : {humidite:.1f}%")


vcnl = adafruit_vcnl4200.Adafruit_VCNL4200(i2c)
print("=== Lecture donnees spatiales (VCNL4200) ===")
print(f"Proximite   : {vcnl.proximity}")
print(f"Lumiere     : {vcnl.lux:.1f} lux")

if vcnl.proximity > 100:
    print("Objet detecte a proximite!")
if vcnl.lux < 50:
    print("Faible eclairage ambiant")

print("\n=== Termine ===")