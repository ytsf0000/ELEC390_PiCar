from time import time,sleep
from Sensors import Sensors
from DrivingModule import CarController
from picarx import Picarx
from globals import Zone,State,Node,CURRENT_STATE,CURRENT_ZONE

from Forward import Forward


picarx=Picarx()
car=CarController(picarx)
sensors=Sensors(picarx)

destination=Node

def Wait():
  car.stop()
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
  if(CURRENT_STATE == State.Wait):
    stateTransition=Wait()
  elif(CURRENT_STATE==State.Forward):
    stateTransition=Forward(car,sensors)
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
  global CURRENT_STATE
  CURRENT_STATE=State.Wait 
  return

def main():
  global CURRENT_STATE
  sensors.run()
  CURRENT_STATE=State.Forward
  while(True):
    #print(CURRENT_STATE)
    startTime=time()
    iteration()
    
    if(stateTransition):
      nodeStateTransition()

    endTime=time()
    if(endTime-startTime<1/120):
      sleep(1/120-(endTime-startTime))



if __name__=="__main__":
  main()
