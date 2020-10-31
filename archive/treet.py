# '''
# This example will print the proximity value
# '''
# # import RPi.GPIO as GPIO
# # from time import sleep
# # from communitysdk import list_connected_devices, MotionSensorKit
# 
# # devices = list_connected_devices()
# # msk_filter = filter(lambda device: isinstance(device, MotionSensorKit), devices)
# # msk = next(msk_filter, None) # Get first Motion Sensor Kit
# 
# # GPIO.setmode(GPIO.BOARD)
# # GPIO.setup(3, GPIO.OUT)
# # pwm=GPIO.PWM(3, 50)
# # pwm.start(0)
# 
# def SetAngle(angle):
#     duty = angle / 18 + 2
#     GPIO.output(3, True)
#     pwm.ChangeDutyCycle(duty)
#     sleep(1)
#     GPIO.output(3, False)
#     pwm.ChangeDutyCycle(0)
# 
# # currAngle = 90
# 
# #if msk == None:
#   #  print('No Motion Sensor was found :(')
# # else:
#     # def on_proximity(proximityValue):
#         # Avoid printing `0` all the time
#        # if proximityValue > 0:
#         #    print('Proximity value:', proximityValue)
#     # msk.set_mode('proximity')
#     # msk.on_proximity = on_proximity
#     # print('Move your hand above the Motion Sensor:')
#     
#     # currAngle += 90
#     # print(currAngle)
#     # SetAngle(currAngle)
#     
# 
# 