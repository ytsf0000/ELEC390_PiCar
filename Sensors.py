import cv2
from picamera2 import Picamera2
import threading
from AIRecog import AISensor
from LineTracking import lineTrackingStatus
from ProximitySensor import ProximitySensor


def aiThread(self):
  while(True):
    self.ai.run(self.picam2.capture_array())


# each sensor runs in seperate thread
class Sensors:
  def ReadAI(self):
    return self.ai.results
  def ReadHardware(self):
    result={"proximity":ProximitySensor(self.car),"lineTracker":lineTrackingStatus(self.car)}
    return result
  def ReadImgProcessing(self):
    return 0
  


  def run(self):
    self.aithread=threading.Thread(target=aiThread,args=self)


  def __init__(self,car):
    self.car=car
    self.picam2 = Picamera2()
    self.picam2.configure(self.picam2.create_still_configuration(main={"size": (640, 640), "format": "RGB888"}))
    self.picam2.start()
    self.ai=AISensor()
    return 0