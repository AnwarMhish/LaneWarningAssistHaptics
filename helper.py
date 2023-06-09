from worlds import *
import numpy as np

def num_to_range(num, inMin, inMax, outMin, outMax):
  return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax
                  - outMin))

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def leftcollision(BaseCarlo):
   return BaseCarlo.car.collidesWith(BaseCarlo.leftlane)

def rightcollision(BaseCarlo):
   return BaseCarlo.car.collidesWith(BaseCarlo.rightlane)

def steeringInput(xh): 
    if(xh > 0.005):
       current_steering = -3.5
    elif (xh < -0.005):
       current_steering = 3.5
    else: 
       current_steering = 0

    return current_steering
