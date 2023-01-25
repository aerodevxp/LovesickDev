import math
from fractions import Fraction
def printPerSentence(str):
    i = 0
    for x in str.split('.'):
        end = '.'
        if(len(x) <= i + 1):
            end = '' #The last sentence so it's not splited.
        while x.startswith(' '):
            x = x[1:]
        print(x + end)
        i += 1

printPerSentence("--- Something to make when bored ---\n Made by ComboDev")

print("\n=========\nPeriodics functions and RAD calculator\n=========")

def degToRad(deg, decimal=False):
    if decimal:
        return deg*2*math.pi/360
    else:
        return (deg*2*math.pi/360)/math.pi
        
while True:
    inp = input('Angles in DEG: ')
    
    
    print('(' + str(degToRad(float(inp)).as_integer_ratio()[0]) + '/' + str(degToRad(float(inp)).as_integer_ratio()[1])  + ')pi')

