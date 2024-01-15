import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
motorSpeed = GPIO.PWM(22, 1000)
motorSpeed.start(0)

def forward(speed):
    print(f"Going forward at {speed}%")
    GPIO.output(16, True)
    GPIO.output(18, False)
    motorSpeed.ChangeDutyCycle(speed)

def backward(speed):
    print(f"Going backward at {speed}%")
    GPIO.output(16, False)
    GPIO.output(18, True)
    motorSpeed.ChangeDutyCycle(speed)
    
def stop():
    GPIO.output(16, False)
    GPIO.output(18, False)
    time.sleep(1)
    motorSpeed.ChangeDutyCycle(0)

try:
    speed = 0
    while speed < 100:
        speed += 1
        forward(speed)
        time.sleep(.1)
    stop()
    speed = 0
    while speed < 100:
        speed += 1
        backward(speed)
        time.sleep(.1)
    stop()
finally:
    motorSpeed.stop()
    GPIO.cleanup()

