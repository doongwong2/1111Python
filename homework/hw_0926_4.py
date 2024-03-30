import sys
import math

def bye():
    sys.exit()
    
def sin(inputval):
    return math.sin((inputval*math.pi) / 180)

def cos(inputval):
    return math.cos((inputval*math.pi) / 180)

while True:
    inputval = input()
    if "<-" in inputval:
        exec(inputval.replace("<-","="))
    else:
        eval(inputval)
