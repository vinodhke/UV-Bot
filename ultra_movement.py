import RPi.GPIO as GPIO
from time import sleep

right_button_pin = 22
left_button_pin = 26
middle_button_pin = 27

servo_pin1 = 23
servo_pin2 = 24

GPIO_TRIGGER = 6
GPIO_ECHO = 5
GPIO_LED = 25

def setup_buttons():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(right_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(left_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(middle_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def setup_sensor():
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.setup(GPIO_LED, GPIO.OUT)

def setup_gpio(servo_pin):
    GPIO.setup(servo_pin, GPIO.OUT)
    return GPIO.PWM(servo_pin, 50)

def move(pwm, direction):
    if direction == 1:
        duty_cycle = 7.5
    elif direction == -1:
        duty_cycle = 2.5
    else:
        duty_cycle = 0
    pwm.ChangeDutyCycle(duty_cycle)

def stop(pwm):
    pwm.ChangeDutyCycle(0)

def move_forward(pwm1, pwm2):
    move(pwm1, 1)
    move(pwm2, -1)

def move_backward(pwm1, pwm2):
    move(pwm1, -1)
    move(pwm2, 1)

def move_right(pwm1, pwm2):
    move(pwm1, 1)
    move(pwm2, 1)

def move_left(pwm1, pwm2):
    move(pwm1, -1)
    move(pwm2, -1)

def distance():
    # Set trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # Set trigger after 0.01ms to LOW
    sleep(0.00001)
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

def main():
    setup_buttons()
    setup_sensor()

    pwm1 = setup_gpio(servo_pin1)
    pwm2 = setup_gpio(servo_pin2)
    pwm1.start(0)
    pwm2.start(0)

    debounce_delay = 0.2

    try:
        button_state = {
            right_button_pin: GPIO.input(right_button_pin),
            left_button_pin: GPIO.input(left_button_pin),
            middle_button_pin: GPIO.input(middle_button_pin),
        }

        while True:
            dist = distance()
            print(f"Distance: {dist:.2f}cm")

            if dist > 10:
                stop(pwm1)
                stop(pwm2)
                sleep(0.1)
                continue

            current_state = {
                right_button_pin: GPIO.input(right_button_pin),
                left_button_pin: GPIO.input(left_button_pin),
                middle_button_pin: GPIO.input(middle_button_pin),
            }

            if button_state[right_button_pin] == GPIO.HIGH and current_state[right_button_pin] == GPIO.LOW:
                move_backward(pwm1, pwm2)
                sleep(2)
                move_left(pwm1, pwm2)
                sleep(3)
                move_forward(pwm1, pwm2)
                sleep(debounce_delay)

            if button_state[left_button_pin] == GPIO.HIGH and current_state[left_button_pin] == GPIO.LOW:
                move_backward(pwm1, pwm2)
                sleep(2)
                move_right(pwm1, pwm2)
                sleep(3)
                move_forward(pwm1, pwm2)
                sleep(debounce_delay)

            if button_state[middle_button_pin] == GPIO.HIGH and current_state[middle_button_pin] == GPIO.LOW:
                move_backward(pwm1, pwm2)
                sleep(2)
                move_left(pwm1, pwm2)
                sleep(3)
                move_forward(pwm1, pwm2)
                sleep(debounce_delay)

            button_state = current_state
            sleep(0.01)

    except KeyboardInterrupt:
        stop(pwm1)
        stop(pwm2)

        pwm1.stop()
        pwm2.stop()

        GPIO.cleanup()

if __name__ == "__main__":
    main()
