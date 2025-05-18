from djitellopy import Tello
import time

tello = Tello()
tello.connect()

print("Battery level:", tello.get_battery())
tello.takeoff()
time.sleep(3)
tello.land()