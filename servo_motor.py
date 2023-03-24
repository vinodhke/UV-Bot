import RPi.GPIO as GPIO
import time

def setup_gpio(servo_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    return GPIO.PWM(servo_pin, 50)

def forward(pwm):
    duty_cycle = 7.5  # Adjust the value to set the forward speed
    pwm.ChangeDutyCycle(duty_cycle)

def stop(pwm):
    pwm.ChangeDutyCycle(0)

def main():
    servo_pin = 17
    pwm = setup_gpio(servo_pin)
    pwm.start(0)

    try:
        while True:
            forward(pwm)
            # The motor will continue to run forward until the script is stopped

    except KeyboardInterrupt:
        stop(pwm)  # Stop the motor when the script is interrupted
        pwm.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
