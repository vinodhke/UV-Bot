import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 16
GPIO_ECHO = 13
GPIO_LED = 26
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LED, GPIO.OUT)

def distance():
    # Set trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # Set trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    start_time = time.time()
    stop_time = time.time()

    # Save start time
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()

    # Save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()

    # Calculate time difference
    time_elapsed = stop_time - start_time

    # Calculate distance in cm
    distance_cm = (time_elapsed * 34300) / 2

    return distance_cm

# Main loop
while True:
    dist = distance()
    print(f"Distance: {dist:.2f}cm")

    if dist < 10: # Check if distance is less than 10cm (4 inches)
        GPIO.output(GPIO_LED, True)
    else:
        GPIO.output(GPIO_LED, False)

    time.sleep(0.1)

# Clean up GPIO pins
GPIO.cleanup()
