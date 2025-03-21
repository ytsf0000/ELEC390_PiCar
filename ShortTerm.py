from time import time,sleep
from Sensors import Sensors
from DrivingModule import CarController
from picarx import Picarx
from globals import Zone,State,Node,CURRENT_STATE,CURRENT_ZONE

from Forward import Forward


currentPosition=None
nextNode=None
stateStartIteration=0
picarx=Picarx()
car=CarController(picarx)
sensors=Sensors(picarx)

destination=Node

def Wait():
  car.turn_right(0,0)
  return True
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
 
stateTransition=False
def iteration():
  global stateTransition
  global CURRENT_STATE
  
  startTime=time()
  
  if(CURRENT_STATE == State.Wait):
    stateTransition=Wait()
  elif(CURRENT_STATE==State.Forward):
    stateTransition=Forward(car,sensors,currentPosition,nextNode)
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
  
  endTime=time()
  
  if(endTime-startTime<1/120):
    sleep(1/120-(endTime-startTime))
  return

def init():
  global CURRENT_STATE
  sensors.run()
  CURRENT_STATE=State.Wait

def main():
  init()
  while(True):
    iteration()


if __name__=="__main__":
  main()
