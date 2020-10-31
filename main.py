'''
This example will print the proximity value
'''
import RPi.GPIO as GPIO
from time import sleep
from communitysdk import list_connected_devices, MotionSensorKit

devices = list_connected_devices()
msk_filter = filter(lambda device: isinstance(device, MotionSensorKit), devices)
msk = next(msk_filter, None) # Get first Motion Sensor Kit

currDist = 0;

if msk == None:
    print('No Motion Sensor was found :(')
else:
    def on_proximity(proximityValue):
        print(currDist)
        if (proximityValue > 200):
#             currDist = proximityValue
#             # do stuff
#             sleep(1)
#             currDist=0
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(3, GPIO.OUT)
            GPIO.setup(5, GPIO.OUT)
            pwm=GPIO.PWM(3, 50)
            pwm2=GPIO.PWM(5, 50)
            pwm.start(0)
            pwm2.start(0)
                        
            def SetValve(angle):
                duty = angle / 18 + 2
                GPIO.output(3, True)
                pwm.ChangeDutyCycle(duty)
                sleep(0.8)
#                 GPIO.output(3, False)
                pwm.ChangeDutyCycle(0)

            def HoldValve(angle):
                duty = angle / 18 + 2
                GPIO.output(3, True)
                pwm.ChangeDutyCycle(duty)
                sleep(0.8)
                
            def ReleaseValve():
                GPIO.output(3, False)
                pwm.ChangeDutyCycle(0)

            def SpinnerAngle(angle):
                duty = angle / 18 + 2
                GPIO.output(5, True)
                pwm2.ChangeDutyCycle(duty)
                sleep(0.8)
                GPIO.output(5, False)
                pwm.ChangeDutyCycle(0)
                
            SetValve(0)
            SetValve(90)
            SetValve(0)
            #HoldAngle
            SpinnerAngle(0)
            SpinnerAngle(10)
            
#             pwm.stop()
#             pwm2.stop()
#             GPIO.cleanup()
            
            

    msk.set_mode('proximity')
    msk.set_interval(1000)
    msk.on_proximity = on_proximity
    print('Move your hand above the Motion Sensor:')