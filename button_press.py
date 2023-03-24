import RPi.GPIO as GPIO
from time import sleep

def on_button_press(channel):
    print(True)

button_pin = 2  # Assuming the button is connected to GPIO2 (Pin 3)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=on_button_press, bouncetime=300)

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
