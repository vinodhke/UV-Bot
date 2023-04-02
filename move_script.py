import RPi.GPIO as GPIO
import time

def setup_gpio(servo_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    return GPIO.PWM(servo_pin, 50)

def move(pwm, direction):
    if direction == 1:
        duty_cycle = 7.5  # Adjust the value to set the forward speed
    elif direction == -1:
        duty_cycle = 2.5  # Adjust the value to set the backward speed
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
    servo_pin1 = 17
    servo_pin2 = 27  # Set the GPIO pin for the second servo motor

    pwm1 = setup_gpio(servo_pin1)
    pwm2 = setup_gpio(servo_pin2)

    pwm1.start(0)
    pwm2.start(0)

    try:
        while True:
            move_forward(pwm1, pwm2)
            time.sleep(5)

            stop(pwm1)
            stop(pwm2)
            time.sleep(2)

            move_backward(pwm1, pwm2)
            time.sleep(5)

            stop(pwm1)
            stop(pwm2)
            time.sleep(2)

            move_right(pwm1, pwm2)
            time.sleep(5)

            stop(pwm1)
            stop(pwm2)
            time.sleep(2)

            move_left(pwm1, pwm2)
            time.sleep(5)

            stop(pwm1)
            stop(pwm2)
            time.sleep(2)

    except KeyboardInterrupt:
        stop(pwm1)  # Stop the first motor when the script is interrupted
        stop(pwm2)  # Stop the second motor when the script is interrupted

        pwm1.stop()
        pwm2.stop()

        GPIO.cleanup()

if __name__ == "__main__":
    main()
