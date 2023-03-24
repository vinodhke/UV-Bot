import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def toggle_led(state):
    GPIO.output(LED_PIN, state)

try:
    while True:
        user_input = input("Type 'y' to turn the LED on or 'n' to turn it off: ")

        if user_input.lower() == 'y':
            toggle_led(True)
            print("LED is ON")
        elif user_input.lower() == 'n':
            toggle_led(False)
            print("LED is OFF")
        else:
            print("Invalid input. Please type 'y' or 'n'.")

except KeyboardInterrupt:
    print("\nExiting the program...")

finally:
    GPIO.cleanup()
