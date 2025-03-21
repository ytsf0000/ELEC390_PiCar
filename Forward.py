import re
import math
from globals import State,NEXT_STATE


# V1 classes
classes=['duck_regular', 'sign_noentry', 'sign_oneway_left', 'sign_oneway_right', 'sign_stop', 'sign_yield']
# full classes
# classes=['duck_regular','duck_specialty','sign_stop','sign_oneway_right','sign_oneway_left','sign_noentry','sign_yield','road_crosswalk','road_oneway','vehicle']


MAX_ANGLE=40
camAngle=0
drivingSpeed=30
distance=0
angle=0
timeToTurn=0

# move camera and return closest sign
def trackSign(aiData,controller):
  global camAngle
  if(aiData is None or aiData.boxes is None):
    return None

  largestArea=0
  closestSign=None
  for b in aiData.boxes:
    if(b.conf<0.70):
      continue
    if(b.xywh.w*b.xywh.h>largestArea):
      if(re.search("^sign_.*$",classes[b.cls]) is not None):
        largestArea=b.xywh.w*b.xywh.h
        closestSign=b
  if(b is None):
    return None
  
  delta=0
  if(b.xywhn.x>0.5):
    delta=-controller.speed/15-math.exp(-2*camAngle/MAX_ANGLE)

  camAngle=max(min(MAX_ANGLE,camAngle+delta),-MAX_ANGLE)

  controller.turnCam(camAngle)
  return closestSign

def dodge():
  return False

# return true if unable to continue without checking long term, false otherwise
def Forward(controller,sensors):
  global angle
  global drivingSpeed
  global timeToTurn
  hardware=sensors.ReadHardware()
  if (timeToTurn>0):
    angle=0
  timeToTurn=max(timeToTurn-1,0)
  
  print(hardware["lineTracker"])
  if(hardware["lineTracker"]==[1,0,0]):
    angle=60
    timeToTurn=20
  elif(hardware["lineTracker"]==[0,0,1]):
    angle=-60
    turnToTurn=20
  # check image tracking for lines ig
  angle=-60
  aiData=sensors.ReadAI()

  sign=trackSign(aiData,controller)

  # store last known sign somewhere since cam might see it when we are besides it
  if(sign is not None and 1):# at sign
    signType=classes[sign.cls]
    if signType=='sign_noentry':
      return 1
    elif signType == 'sign_oneway_left':
      if(NEXT_STATE==State.TurnR):
        print("wrong way one way")
      return 1
    elif signType == 'sign_oneway_right':
      if(NEXT_STATE==State.TurnL):
        print("wrong way one way")
      return 1
    elif signType == 'sign_stop':
      return 0
    elif signType == 'sign_yield':
      return 0

  # avoid things on read
  if(dodge()):
    return 0

  controller.turn_right(angle=angle,speed=drivingSpeed)
  return 0
