import RPi.GPIO as GPIO
from time import sleep

def on_button_press():
    print(True)

button_pin = 2  # Assuming the button is connected to GPIO2 (Pin 3)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

debounce_delay = 0.2

try:
    button_state = GPIO.input(button_pin)
    while True:
        current_state = GPIO.input(button_pin)
        if button_state == GPIO.HIGH and current_state == GPIO.LOW:
            on_button_press()
            sleep(debounce_delay)
        button_state = current_state
        sleep(0.01)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
