from ultralytics import YOLO

Path_to_model="models/best_full_integer_quant_edgetpu.tflite"

class AISensor:
  def run(self,frame):
    # this runs infintely without trigger, result is stored into variable then read
    # change once camera is implemented
    self.results=self.model.predict(frame)
  def read(self):
    return self.results
  def __init__(self):
    self.results=None
    self.model = YOLO(Path_to_model)  # Load an official model or custom model
