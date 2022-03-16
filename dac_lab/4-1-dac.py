import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try:
    str = input("Type number from 0 to 255: ")
    if (str == "q"):
        print("Okay, exiting...")
    else:
        n = int(str)
        if n > 255 or n < 0:
            print("This value is out of range! Exiting...")
        else:
            GPIO.output(dac, decimal2binary(n))
            print(f"Success! Suggested voltage is {n/255*3.3}")
            input("Type enter to exit the program ")

except ValueError:
    print("It was not int! Exiting...")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()