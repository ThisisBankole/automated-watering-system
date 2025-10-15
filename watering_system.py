from m5stack import *
from m5stack_ui import *
from uiflow import *
import time
import unit


screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0x191919)
env3_0 = unit.get(unit.ENV3, unit.PORTA)
Watering_0 = unit.get(unit.WATERING, unit.PORTB)


moistureValue = None
scale = None
minValue = None
maxValue = None
soilPercentage = None



temp = M5Label('temperature', x=14, y=30, color=0xe7e7e7, font=FONT_MONT_14, parent=None)
humidity = M5Label('humidity', x=14, y=70, color=0xffffff, font=FONT_MONT_14, parent=None)
pressure = M5Label('pressure', x=14, y=110, color=0xffffff, font=FONT_MONT_14, parent=None)
soilMoisture = M5Label('soil moisture', x=12, y=151, color=0xfcfcfc, font=FONT_MONT_14, parent=None)
water = M5Label('water', x=14, y=190, color=0xfcfcfc, font=FONT_MONT_14, parent=None)
switch0 = M5Switch(x=209, y=189, w=70, h=30, bg_c=0xCCCCCC, color=0x022afb, parent=None)
tempValue = M5Label('0', x=209, y=30, color=0xffffff, font=FONT_MONT_14, parent=None)
humValue = M5Label('0', x=209, y=70, color=0xffffff, font=FONT_MONT_14, parent=None)
presValue = M5Label('0', x=209, y=110, color=0xfaf7f7, font=FONT_MONT_14, parent=None)
smValue = M5Label('0', x=209, y=150, color=0xf9f7f7, font=FONT_MONT_14, parent=None)



def switch0_on():
  global moistureValue, scale, minValue, maxValue, soilPercentage
  Watering_0.set_pump_status(1)
  pass
switch0.on(switch0_on)

def switch0_off():
  global moistureValue, scale, minValue, maxValue, soilPercentage
  Watering_0.set_pump_status(0)
  pass
switch0.off(switch0_off)


moistureValue = 0
scale = 0
minValue = 1620
maxValue = 1800
while True:
  moistureValue = Watering_0.get_adc_value()
  scale=(100/(minValue-maxValue))
  soilPercentage=int((moistureValue-maxValue)*scale)
  tempValue.set_text(str(env3_0.temperature))
  humValue.set_text(str(env3_0.humidity))
  presValue.set_text(str(env3_0.pressure))
  smValue.set_text(str(Watering_0.get_adc_value()))
  if soilPercentage <= 10:
    switch0.set_on()
    Watering_0.set_pump_status(1)
  else:
    switch0.set_off()
    Watering_0.set_pump_status(0)
  wait(1)
  wait_ms(2)
