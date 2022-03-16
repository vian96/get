import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)

dac = [10, 9, 11, 5, 6, 13, 19, 26]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        number = int(input())

        for i in range(8):
            flag = (number//(1<<i)) % 2
            print("DEB: " + str(i) + " " + str(flag))
            GPIO.output(dac[i], flag)

except KeyboardInterrupt:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    

# ------------------------------------------------------------------------
# import RPi.GPIO as GPIO
# import time

GPIO.setmode (GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(leds, GPIO.OUT)

try:
    while True:
        for led in leds:
            GPIO.output(led, 1)
            time.sleep(0.2)
            GPIO.output(led, 0)

except KeyboardInterrupt:
    GPIO.output(leds, 0)
    GPIO.cleanup()
