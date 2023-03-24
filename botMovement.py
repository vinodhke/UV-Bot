GPIO 17 - Servo Motor 1 (look into how to reverse motor)
GPIO 27 - Servo Motor 2 

GPIO 23- Left Bump Sensor
GPIO 24- Middle Bump Sensor
GPIO 25- Right Bump Sensor

GPIO 16 Signal - UltraSonic Sensor

	gpio.setup(16, gpio.OUT)

GPIO 13 ECHO - Ultrasonic Senor

	gpio.setup(13, gpio.IN)

GPIO 26 - Encoder Wheel

GPIO 22 - Ultraviolet light





import RPi.GPIO as GPIO
import time

# Set up GPIO pins for servo motors
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

# Set up GPIO pins for bump sensors
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)

# Function to move the robot forward
def forward():
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    GPIO.output(19, False)

# Function to move the robot backward
def backward():
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    GPIO.output(19, True)

# Function to turn the robot left
def left():
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, True)
    GPIO.output(19, False)

# Function to turn the robot right
def right():
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(19, True)

# Function to stop the robot
def stop():
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    GPIO.output(19, False)

# Main loop to control the robot
while True:
    if GPIO.input(16) == 0:
        backward()
        time.sleep(1)
        stop()
    elif GPIO.input(18) == 0:
        left()
        time.sleep(1)
        stop()
    elif GPIO.input(22) == 0:
        right()
        time.sleep(1)
        stop()
    else:
        forward()


