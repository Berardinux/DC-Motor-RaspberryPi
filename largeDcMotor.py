import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
motorSpeedPin29 = GPIO.PWM(29, 1000)
motorSpeedPin31 = GPIO.PWM(31, 1000)
motorSpeedPin29.start(0)
motorSpeedPin31.start(0)

def forward(speed):
    print(f"Going forward at {speed}%")
    GPIO.output(31, False)
    motorSpeedPin29.ChangeDutyCycle(speed)

def backward(speed):
    print(f"Going backward at {speed}%")
    GPIO.output(29, True)
    motorSpeedPin31.ChangeDutyCycle(speed)
    
def stop():
    GPIO.output(29, False)
    GPIO.output(31, False)
    time.sleep(1)

try:
    speed = 0
    while speed < 100:
        speed += 1
        forward(speed)
        time.sleep(.1)
    while speed > 0:
        speed -= 1
        forward(speed)
        time.sleep(.1)
    stop()
    speed = 0
    while speed < 100:
        speed += 1
        backward(speed)
        time.sleep(.1)
    while speed > 0:
        speed -= 1
        backward(speed)
        time.sleep(.1)
    stop()
finally:
    motorSpeed.stop()
    GPIO.cleanup()

