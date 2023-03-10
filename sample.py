import RPi.GPIO as GPIO
import time

# Set up GPIO pins for bump sensors and motors
GPIO.setmode(GPIO.BCM)

bump1_pin = 4
bump2_pin = 17
bump3_pin = 27

motor1_pin1 = 18
motor1_pin2 = 23
motor2_pin1 = 24
motor2_pin2 = 25

GPIO.setup(bump1_pin, GPIO.IN)
GPIO.setup(bump2_pin, GPIO.IN)
GPIO.setup(bump3_pin, GPIO.IN)

GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)

# Define functions for motor control
def forward():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

def backward():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)

def stop():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)

# Define dimensions of the room
room_width = 10
room_length = 20

# Define variables for car position and direction
car_x = 0
car_y = 0
car_direction = 0 # 0 = facing right, 1 = facing down, 2 = facing left, 3 = facing up

# Define function for moving the car
def move_car():
    global car_x, car_y, car_direction
    
    # Move the car forward
    forward()
    time.sleep(0.5)
    stop()
    
    # Update car position and direction
    if car_direction == 0:
        car_x += 1
        if car_x >= room_width:
            car_direction = 1
    elif car_direction == 1:
        car_y += 1
        if car_y >= room_length:
            car_direction = 2
    elif car_direction == 2:
        car_x -= 1
        if car_x < 0:
            car_direction = 3
    elif car_direction == 3:
        car_y -= 1
        if car_y < 0:
            car_direction = 0

# Main loop
while True:
    # Check bump sensors
    if GPIO.input(bump1_pin) == GPIO.HIGH or GPIO.input(bump2_pin) == GPIO.HIGH or GPIO.input(bump3_pin) == GPIO.HIGH:
        backward()
        time.sleep(0.5)
        stop()
    else:
        move_car()
