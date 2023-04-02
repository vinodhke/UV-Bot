import RPi.GPIO as GPIO
from time import sleep

right_button_pin = 2
left_button_pin = 3
middle_button_pin = 4

servo_pin1 = 17
servo_pin2 = 27

def setup_buttons():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(right_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(left_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(middle_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

def main():
    setup_buttons()

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
