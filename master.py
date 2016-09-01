# to avoid bloat, we can just call this as: 
# import master as (whatever), otherwise it'll just get tedious :P
# feel free to add parameters as you  feel appropriate

def __init__(): # everything within this definition is called when the lib is imported. 
  import RPi.GPIO as GPIO #we'll definitely need this
  import time #we'll probably need this. 
  import math #we might need this?

def initialise(frequency):
#settings
  GPIO.setmode(GPIO.BCM) # using the mode setting from the previous script
  GPIO.setwarnings(False) # disable warnings

#Define when  we find out the pin layout --- Frequency could be defined as an input within the individual scripts and then called with initialise(frequency)?
  pinMotorAForwards = #use format (pin,frequency) 
  pinMotorABackwards = #use format (pin,frequency)
  pinMotorBForwards = #use format (pin,frequency)
  pinMotorBBackwards = #use format (pin,frequency)

#Duty Cycles
  DutyCycleA = 30
  DutyCycleB = 30

  pinLineFollower = #no idea. 

#set to outputs

  GPIO.setup(pinMotorAForwards, GPIO.OUT)
  GPIO.setup(pinMotorABackwards, GPIO.OUT)
  GPIO.setup(pinMotorBForwards, GPIO.OUT)
  GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# PWM setup
  pwmMotorAForwards = GPIO.PWM(pinMotorAForwards,frequency)
  pwmMotorABackwards = GPIO.PWM(pinMotorABackwards,frequency)
  pwmMotorBForwards = GPIO.PWM(pinMotorBForwards,frequency)
  pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards,frequency)

# Null duty cycles
  pwmMotorAForwards.start(0)
  pwmMotorABackwards.start(0)
  pwmMotorBForwards.start(0)
  pwmMotorBBackwards.start(0)

def stop():  
  print("Stopped")
  pwm.stop()
  GPIO.cleanup()
