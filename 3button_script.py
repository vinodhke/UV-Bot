import RPi.GPIO as GPIO
from time import sleep

def on_right_button_press():
    print("right")

def on_left_button_press():
    print("left")

def on_middle_button_press():
    print("middle")

right_button_pin = 2
left_button_pin = 3
middle_button_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(right_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(left_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(middle_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

debounce_delay = 0.2

try:
    right_button_state = GPIO.input(right_button_pin)
    left_button_state = GPIO.input(left_button_pin)
    middle_button_state = GPIO.input(middle_button_pin)
    
    while True:
        current_right_state = GPIO.input(right_button_pin)
        current_left_state = GPIO.input(left_button_pin)
        current_middle_state = GPIO.input(middle_button_pin)
        
        if right_button_state == GPIO.HIGH and current_right_state == GPIO.LOW:
            on_right_button_press()
            sleep(debounce_delay)
            
        if left_button_state == GPIO.HIGH and current_left_state == GPIO.LOW:
            on_left_button_press()
            sleep(debounce_delay)
            
        if middle_button_state == GPIO.HIGH and current_middle_state == GPIO.LOW:
            on_middle_button_press()
            sleep(debounce_delay)

        right_button_state = current_right_state
        left_button_state = current_left_state
        middle_button_state = current_middle_state
        
        sleep(0.01)
        
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
