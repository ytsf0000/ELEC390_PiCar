from enum import Enum
from time import time,sleep
from Sensors import Sensors
from DrivingModule import CarController


# temp class while waiting for long term decision
class Node:
  def __init__(self):
    pass

def current_milli_time():
    return round(time.time() * 1000)

class Zone(Enum):
  NOZONE=0
  Pedestrian=1
  Risk=2
  School=3
  Residential=4
  Shops=5
  Industrial=6

class State(Enum):
  Wait=0
  Forward=1
  TurnR=2
  TurnL=3
  RoundAbout=4
  Park=5


car=CarController()
sensors=Sensors()
CURRENT_ZONE=Zone.NOZONE
CURRENT_STATE=State.Wait

destination=Node

def Wait():
  car.move_forward(0)
  return
def Forward():
  car.move_forward()
  # check to obstacles and avoidance measures
  return
def TurnR():
  # check what angle to put servo
  car.turn_right()
  return
def TurnL():
  # check what angle to put servo
  car.turn_left()
  return
def RoundAbout():
  # more complex logic
  return
def Park():
  # depends
  return
 

def iteration():
  if(CURRENT_STATE == Zone.Wait):
    Wait()
  elif(CURRENT_STATE==State.Wait):
    Wait()
  elif(CURRENT_STATE==State.Forward):
    Forward()
  elif(CURRENT_STATE==State.TurnR):
    TurnR()
  elif(CURRENT_STATE==State.TurnL):
    TurnL()
  elif(CURRENT_STATE==State.RoundAbout):
    RoundAbout()
  elif(CURRENT_STATE==State.Park):
    Park()
  else:
    print("Unknown State")
  return

# check if we reached the node and state change when reached
def nodeStateTransition():
  return

def main():
  while(True):
    startTime=time()

    iteration()
    
    nodeStateTransition()

    endTime=time()
    if(endTime-startTime<1/120):
      sleep(1/120-(endTime-startTime))



if __name__=="__main__":
  main()