from enum import Enum


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

# temp class while waiting for long term decision
class Node:
  def __init__(self):
    pass

CURRENT_ZONE=Zone.NOZONE
CURRENT_STATE=State.Wait
NEXT_STATE=State.Wait