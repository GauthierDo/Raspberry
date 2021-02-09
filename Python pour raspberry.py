import RPI.GPIO as GPIO
from time import sleep

ENRight = 5
ENLeft = 6

MotTopLeft = 7
MotTopRight = 8

MotBotLeft = 9
MotBotRight = 11

carSpeed = 255

Pins = [[ENRight, MotBotRight,MotTopRight],[ENLeft,MotBotLeft,MotTopLeft]]

#Setup 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ENRight, GPIO.OUT)
GPIO.setup(MotBotRight, GPIO.OUT)
GPIO.setup(MotTopRight, GPIO.OUT)

GPIO.setup(ENLeft, GPIO.OUT)
GPIO.setup(MotBotLeft, GPIO.OUT)
GPIO.setup(MotTopLeft, GPIO.OUT)


def speedUp(carSpeed) :
        if (carSpeed<200):
            carSpeed = carSpeed + 50
        
def speedDown(carSpeed) : 
    if (carSpeed>80) :
        carSpeed = carSpeed - 50
        
def forward() :
    #GPIO.output(Pins[0][0], carSpeed)
    #GPIO.output(Pins[1][0], carSpeed)
    #GPIO.output(Pins[0][1], GPIO.LOW)
    #GPIO.output(Pins[0][2], GPIO.HIGH)
    #GPIO.output(Pins[1][1], GPIO.LOW)
    #GPIO.output(Pins[1][2], GPIO.HIGH)
    print("Avance !")
    
def back() :
    #GPIO.output(Pins[0][0], carSpeed)
    #GPIO.output(Pins[1][0], carSpeed)
    #GPIO.output(Pins[0][1], GPIO.HIGH)
    #GPIO.output(Pins[0][2], GPIO.LOW)
    #GPIO.output(Pins[1][1], GPIO.HIGH)
    #GPIO.output(Pins[1][2], GPIO.LOW)
    print("Recule !")

def right() :
    #GPIO.output(Pins[0][0], carSpeed)
    #GPIO.output(Pins[1][0], carSpeed)
    #GPIO.output(Pins[0][1], GPIO.LOW)
    #GPIO.output(Pins[0][2], GPIO.LOW)
    #GPIO.output(Pins[1][1], GPIO.HIGH)
    #GPIO.output(Pins[1][2], GPIO.HIGH)
    print("A droite !")

def left() :
    #GPIO.output(Pins[0][0], carSpeed)
    #GPIO.output(Pins[1][0], carSpeed)
    #GPIO.output(Pins[0][1], GPIO.HIGH)
    #GPIO.output(Pins[0][2], GPIO.HIGH)
    #GPIO.output(Pins[1][1], GPIO.LOW)
    #GPIO.output(Pins[1][2], GPIO.LOW)
    print("A gauche !")
    
def forwardLeft() :
    #GPIO.output(Pins[0][0], carSpeed)
    #GPIO.output(Pins[1][0], carSpeed/4)
    #GPIO.output(Pins[0][1], GPIO.LOW)
    #GPIO.output(Pins[0][2], GPIO.LOW)
    #GPIO.output(Pins[1][1], GPIO.LOW)
    #GPIO.output(Pins[1][2], GPIO.LOW)
    print("Avant gauche !")
    
def forwardRight() :
    #GPIO.output(Pins[0][0], carSpeed/4)
    #GPIO.output(Pins[1][0], carSpeed)
    #GPIO.output(Pins[0][1], GPIO.LOW)
    #GPIO.output(Pins[0][2], GPIO.LOW)
    #GPIO.output(Pins[1][1], GPIO.LOW)
    #GPIO.output(Pins[1][2], GPIO.LOW)
    print("Avant droit !")
    
def arretComplet() :
    #GPIO.output(Pins[0][0], carSpeed)
    #GPIO.output(Pins[1][0], carSpeed)
    #GPIO.output(Pins[0][1], GPIO.LOW)
    #GPIO.output(Pins[0][2], GPIO.LOW)
    #GPIO.output(Pins[1][1], GPIO.LOW)
    #GPIO.output(Pins[1][2], GPIO.LOW)
    print("Moteurs arretes.")
 
def F() :
    forward()

def B() :
    back()

def L() :
    left()

def R() :
    right()

def S() :
    arretComplet()

def E() :
    forwardRight()

def A() :
    forwardLeft()

def U() :
    speedUp()

def D() :
    speedDown()

def main () :
        switcher = {
        1: "F",
        2: "B",
        3: "L",
        4: "R",
        5: "S",
        6: "E",
        7: "A",
        8: "U",
        9: "D"
    }
