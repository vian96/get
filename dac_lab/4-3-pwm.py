import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
pwm_pin = 22
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

p = GPIO.PWM(pwm_pin, 100)
p.start(0)

try:
    while True:
        dc = float(input("Type duty cycle: "))
        p.ChangeDutyCycle(dc)
        print(f"Success! Your suggested voltage is {dc/100*3.3 :.3f}")
    
except ValueError:
    print("It was not float! Exiting...")

finally:
    p.stop()
    GPIO.output(dac, 0)
    GPIO.cleanup()

