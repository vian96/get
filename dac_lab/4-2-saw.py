import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try:
    period = float(input("Type period in secs: "))
    step = period / 256
    while True:
        for n in range(256):
            GPIO.output(dac, decimal2binary(n))
            time.sleep(step)

except ValueError:
    print("It was not float! Exiting...")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

