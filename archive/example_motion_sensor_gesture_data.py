'''
This example will print the gesture name
'''

# import RPi.GPIO as GPIO
# from time import sleep
from communitysdk import list_connected_devices, MotionSensorKit

devices = list_connected_devices()
msk_filter = filter(lambda device: isinstance(device, MotionSensorKit), devices)
msk = next(msk_filter, None) # Get first Motion Sensor Kit

msk = next(msk_filter, None) # Get first Motion Sensor Kit

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT)
# pwm=GPIO.PWM(3, 50)
# pwm.start(0)
# 
# def SetAngle(angle):
#     duty = angle / 18 + 2
#     GPIO.output(3, True)
#     pwm.ChangeDutyCycle(duty)
#     sleep(1)
#     GPIO.output(3, False)
#     pwm.ChangeDutyCycle(0)
    
# currAngle = 0

def on_gesture(gestureValue):
    print('Gesture detected:', gestureValue)
#         currAngle += 90
#         print(currAngle)
#         SetAngle(currAngle)
try:
    msk.set_mode('gesture')
except Exception as e:
    print(e)
msk.on_gesture = on_gesture
print('Wave your hand above the Motion Sensor:')

# pwm.stop()
# GPIO.cleanup()