##This is our dump for everything that is used in more than one script to avoid bloating the code to much. 
##Declare all variables as global in __init__ so they can be used outside the functions within the module, without the need for master.varname.
##For the sake of convenience, import master as m. 
def __init__():
  #import modules
  import RPi.GPIO as GPIO
	import time
  #declare all objects we're going to use as global. They can be referenced by master.varname, but this is just to be safe. 
  global pinMotorAForwards
  global pinMotorABackwards
  global pinMotorBForwards
  global pinMotorBBackwards
  global Frequency
  global DutyCycleA
  global DutyCycleB
  global pinLineFollower
  global pwmMotorAForwards
  global pwmMotorBForwards
  global pwmMotorABackwards
  global pwmMotorBBackwards
  global stop

def initialise(frequency): 
  stop = 0
  #Set modes. Maybe a switch for warnings ^, to debug? 
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  
  pinMotorAForwards = #define when we know pin layout
  pinMotorABackwards = #define when we know pin layout
  pinMotorBForwards = #define when we know pin layout
  pinMotorBBackwards = #define when we know pin layout
  
  pinLineFollower = 25 #define when we know pin layout
  DutyCycleA = 30 #define when we find an optimal value for this
  DutyCycleB = 30 #define when we find an optimal value for this
  
  GPIO.setup(pinMotorAForwards, GPIO.OUT) #set output for Motor A
  GPIO.setup(pinMotorABackwards, GPIO.OUT) #set output for Motor A
  GPIO.setup(pinMotorBForwards, GPIO.OUT) #set output for Motor B
  GPIO.setup(pinMotorBBackwards, GPIO.OUT) #set output for Motor B
  GPIO.setup(pinLineFollower, GPIO.IN) #set input for controller
  
  pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency) #set PWM for Motor A
  pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency) #set PWM for Motor A
  pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency) #set PWM for Motor B
  pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency) #set PWM for Motor B
  
  pwmMotorAForwards.start(0) #not moving
  pwmMotorABackwards.start(0) #not moving
  pwmMotorBForwards.start(0) #not moving
  pwmMotorBBackwards.start(0) #not moving

##Imported from Line-Following.py##
# Turn all motors off
def StopMotors():
  pwmMotorAForwards.ChangeDutyCycle(Stop)
  pwmMotorABackwards.ChangeDutyCycle(Stop)
  pwmMotorBForwards.ChangeDutyCycle(Stop)
  pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors forwards
def Forwards():
  pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
  pwmMotorABackwards.ChangeDutyCycle(Stop)
  pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
  pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors backwards
def Backwards():
  pwmMotorAForwards.ChangeDutyCycle(Stop)
  pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
  pwmMotorBForwards.ChangeDutyCycle(Stop)
  pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
# Turn left
def Left():
  pwmMotorAForwards.ChangeDutyCycle(Stop)
  pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
  pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
  pwmMotorBBackwards.ChangeDutyCycle(Stop)

 # Turn Right
def Right():
  pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
  pwmMotorABackwards.ChangeDutyCycle(Stop)
  pwmMotorBForwards.ChangeDutyCycle(Stop)
  pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

#call it like this within the main routine, after a "try" statement.:
#except KeyboardInterrupt():
##stop()
#This ensures that everything is in the right state when the program is terminated. 
def stop()
  GPIO.cleanup()
  pwm.stop() ##change to working variable##

#can be used to quickly change to debug mode when on the command line. 
def debug(x)
  if x == True:
    GPIO.setwarnings(true)
  elif x == False:
    GPIO.setwarnings(false)
  else:
    print("Invalid input")
