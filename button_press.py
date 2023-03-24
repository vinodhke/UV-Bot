import RPi.GPIO as GPIO
from time import sleep

def on_button_press(channel):
    if GPIO.input(channel) == GPIO.LOW:
        print(True)

button_pin = 2  # Assuming the button is connected to GPIO2 (Pin 3)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        GPIO.wait_for_edge(button_pin, GPIO.FALLING)
        sleep(0.01)  # Adding a debounce time
        on_button_press(button_pin)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
