import RPi.GPIO as GPIO

import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
comp = 4
GPIO.setup(comp, GPIO.IN)
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = 1)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    k = 7
    n = 0
    while k:
        n += 2**k
        GPIO.output(dac, decimal2binary(n))
        time.sleep(0.0007)
        if GPIO.input(comp) == 0: # higher
            n -= 2**k
        k -= 1
    return n

try:
    while True:
        n = adc()
        n += 14 # compensation of loss
        voltage = n/256*3.3
        bright = n*8//256
        GPIO.output(leds[:bright], 1)
        GPIO.output(leds[bright:], 0)
        print(f"OUT: {n}\nCalculated voltage is {voltage}\nBright is {bright}")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

    