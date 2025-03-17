
def ReadAI():
  print("a") 
def ReadHardware():
  print("a")
def ReadImgProcessing():
  print("a")


# each sensor runs in seperate thread
class Sensors:
  def ReadAI(self):
    return 0
  def ReadHardware(self):
    return 0
  def ReadImgProcessing(self):
    return 0
  

  def __init__(self):
    return 0