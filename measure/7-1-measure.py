import RPi.GPIO as GPIO
import matplotlib.pyplot as plt

import time
from datetime import datetime

############################
# GPIO setup
GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
comp = 4
GPIO.setup(comp, GPIO.IN)
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = 0)
leds = [21, 20, 16, 12, 7, 8, 25, 24][::-1]
GPIO.setup(leds, GPIO.OUT)
############################


############################
# adc, dac functions

# converts decimal to binary
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

# reads adc value with some kind of bs
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

# sets "volume" according to val
def set_volume(val):
    val += 14 # compensation of loss
    bright = val*8//256
    GPIO.output(leds[:bright], 1)
    GPIO.output(leds[bright:], 0)
############################

values = []
highest = 0.97 
lowest = 0.02 

try:
    start_time = time.time()
    GPIO.output(troyka, 1)

    while True:
        n = adc()
        set_volume(n)
        values.append(n)
        print(f"n={n}    ", end='\r')
        if n >= highest * 255:
            break
    
    highest_time = time.time() - start_time
    print(f"First part ended after {highest_time}")
    GPIO.output(troyka, 0)

    while True:
        n = adc()
        set_volume(n)
        values.append(n)
        print(f"n={n}    ", end='\r')
        if n <= lowest * 255:
            break
    
    lowest_time = time.time() - start_time
    print(f"Second part ended after {lowest_time}")

    date = datetime.now().strftime('%y.%m.%d-%H.%M.%S')
    with open(f"data-{date}.txt", 'w') as f:
        f.write('\n'.join(str(i) for i in values))
    
    with open(f"settings-{date}.txt", 'w') as f:
        f.write(f"Average frequency: {lowest_time/len(values)} s \nDiscretization is {3.3/256} V\n")

    print(
        f"Experiment lasted: {lowest_time} s", 
        f"Average time of measurement: {lowest_time/2} s", 
        f"Average frequency: {lowest_time/len(values)} s", 
        f"Discretization is {3.3/256} V", 
        sep='\n'
    )

    plt.plot(values)
    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

    