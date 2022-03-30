import RPi.GPIO as GPIO

import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
comp = 4
GPIO.setup(comp, GPIO.IN)
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = 1)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.0007)
        if GPIO.input(comp) == 0:
            return i

try:
    while True:
        n = adc()
        print(f"OUT: {n}\nCalculated voltage is {n/256*3.3}")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()