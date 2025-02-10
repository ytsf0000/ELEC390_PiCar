from picarx import Picarx
import time

POWER = 50
SAFEDISTANCE = 40   # > 40 safe
DANGERDISTANCE = 20 # > 20 && < 40 turn around,
                    # < 20 backward

def ProximitySensor():
    try:
        px = Picarx()
        # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo

        distance = round(px.ultrasonic.read(), 2)
        print("distance: ",distance)
        if distance >= 40:
            #px.set_dir_servo_angle(0)
            #px.forward(POWER)
            return 0 #Code 0: safe distance maintained
        elif distance >= 20:
            #px.set_dir_servo_angle(30)
            #px.forward(POWER)
            #time.sleep(0.1)
            return 1 #Code 1: dangerous distance, let control logic handle
        else:
            #px.set_dir_servo_angle(-30)
            #px.backward(POWER)
            #time.sleep(0.5)
            return 2 #Code 2: object is too close

    #finally:
        #px.forward(0)
