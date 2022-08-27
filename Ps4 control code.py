from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
from time import sleep
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#motor A
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

# GPIO.output(23,GPIO.LOW)
# GPIO.output(24,GPIO.HIGH)

#motor B
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

# GPIO.output(26,GPIO.LOW)
# GPIO.output(25,GPIO.HIGH)

#motor C
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

#motor D
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
    
pygame.init()
pygame.display.set_mode((500,500))

pwm1 = GPIO.PWM(23,100)
pwm2 = GPIO.PWM(25,100)
pwm3 = GPIO.PWM(5,100)
pwm4 = GPIO.PWM(22,100)

clock = pygame.time.Clock()
run = True
x= 0

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)


class MyController(Controller):
    
    def on_x_press(self):
        pass
#         print("on_x_press")

    def on_x_release(self):
        pass
#         print("on_x_release")


    def on_triangle_press(self):
        pass
#         print("on_triangle_press")

    def on_triangle_release(self):
        pass
#         print("on_triangle_release")

    def on_circle_press(self):
        pass
#         print("on_circle_press")

    def on_circle_release(self):
        pass
#         print("on_circle_release")

    def on_square_press(self):
        pass
#         print("on_square_press")

    def on_square_release(self):
        pass
#         print("on_square_release")

    def on_L1_press(self):
        pass
#         print("on_L1_press")

    def on_L1_release(self):
        pass
#         print("on_L1_release")

    def on_L2_press(self, value):
#         pass
#         print("on_L2_press: ", value)
        global x
        #Motor 1
        GPIO.output(24,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        #Motor 2
        GPIO.output(25,GPIO.LOW)
        GPIO.output(26,GPIO.HIGH)
        #Motor 3
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        #Motor 4
        GPIO.output(27,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
        x +=10
        if x>100:
            x=100
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("LEFT UTURN")

    def on_L2_release(self):
#         pass
        global x
        x = 0
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("on_L2_release")

    def on_R1_press(self):
        pass
#         print("on_R1_press")

    def on_R1_release(self):
        pass
#         print("on_R1_release")

    def on_R2_press(self, value):
#         pass
#         print("on_R2_press: ", value)
        global x
        #Motor 1
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.HIGH)
        #Motor 2
        GPIO.output(26,GPIO.LOW)
        GPIO.output(25,GPIO.HIGH)
        #Motor 3
        GPIO.output(6,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        #Motor 4
        GPIO.output(22,GPIO.LOW)
        GPIO.output(27,GPIO.HIGH)
        x +=10
        if x>100:
            x=100
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("RIGHT UTURN")

    def on_R2_release(self):
#         pass
        global x
        x = 0
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("on_R2_release")

    #UP
    def on_up_arrow_press(self):
        global x
        #Motor 1
        GPIO.output(24,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        #Motor 2
        GPIO.output(26,GPIO.LOW)
        GPIO.output(25,GPIO.HIGH)
        #Motor 3
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        #Motor 4
        GPIO.output(22,GPIO.LOW)
        GPIO.output(27,GPIO.HIGH)
        x +=10
        if x>100:
            x=100
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("UP")
#         print("on_up_arrow_press")

    def on_up_down_arrow_release(self):
        global x
        x = 0
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("on_up_down_arrow_release")

    #DOWN
    def on_down_arrow_press(self):
        global x
        #Motor 1
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.HIGH)
        #Motor 2
        GPIO.output(25,GPIO.LOW)
        GPIO.output(26,GPIO.HIGH)
        #Motor 3
        GPIO.output(6,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        #Motor 4
        GPIO.output(27,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
        x +=10
        if x>100:
            x=100
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("DOWN")
#         print("on_down_arrow_press")

    #LEFT
    def on_left_arrow_press(self):
        global x
        #Motor 1
        GPIO.output(24,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        #Motor 2
        GPIO.output(26,GPIO.LOW)
        GPIO.output(25,GPIO.HIGH)
        #Motor 3
        GPIO.output(6,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
        #Motor 4#Motor 1
        GPIO.output(24,GPIO.LOW)
        GPIO.output(23,GPIO.HIGH)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(22,GPIO.HIGH)
        x +=10
        if x>100:
            x=100
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("LEFT")
#         print("on_left_arrow_press")

    def on_left_right_arrow_release(self):
        global x
        x = 0
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("on_left_right_arrow_release")

    #RIGHT
    def on_right_arrow_press(self):
        global x
        #Motor 1
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.HIGH)
        #Motor 2
        GPIO.output(25,GPIO.LOW)
        GPIO.output(26,GPIO.HIGH)
        #Motor 3
        GPIO.output(5,GPIO.LOW)
        GPIO.output(6,GPIO.HIGH)
        #Motor 4
        GPIO.output(22,GPIO.LOW)
        GPIO.output(27,GPIO.HIGH)
        x +=10
        if x>100:
            x=100
        pwm1.ChangeDutyCycle(x)
        pwm2.ChangeDutyCycle(x)
        pwm3.ChangeDutyCycle(x)
        pwm4.ChangeDutyCycle(x)
        print("RIGHT")
#         print("on_right_arrow_press")

    def on_L3_up(self, value):
        pass
#         print("on_L3_up: ", value)

    def on_L3_down(self, value):
        pass
#         print("on_L3_down: ", value)

    def on_L3_left(self, value):
        pass
#         print("on_L3_left: ", value)

    def on_L3_right(self, value):
        pass
#         print("on_L3_right: ", value)

    def on_L3_release(self):
        pass
#         print("on_L3_release")

    def on_R3_up(self, value):
        pass
#         print("on_R3_up: ", value)

    def on_R3_down(self, value):
        pass
#         print("on_R3_down: ", value)

    def on_R3_left(self, value):
        pass
#         print("on_R3_left: ", value)

    def on_R3_right(self, value):
        pass
#         print("on_R3_right: ", value)

    def on_R3_release(self):
        pass
#         print("on_R3_release")

    def on_options_press(self):
        pass
#         print("on_options_press")

    def on_options_release(self):
        pass
#         print("on_options_release")

    def on_L3_x_at_rest(self):
        pass
    
    def on_L3_y_at_rest(self):
        pass
        
        
controller = MyController(interface="/dev/input/js0",connecting_using_ds4drv=False)
controller.listen()

pwm.stop()
GPIO.cleanup()
pygame.quit()
exit()

