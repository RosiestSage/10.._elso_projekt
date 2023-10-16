import os, random
from statok import *


#Változók----------------------------------
ora = 0
perc = 0
oraPlusz = 0
percPlusz = 0
ehseg = 0
penz = 5000
#------------------------------------------
def idoMeres(oraPlusz,percPlusz):
    global ora
    global perc
    perc += percPlusz
    if perc >= 60:
        ora += 1
        perc -= 60
    else:
        print("asd")
    ora += oraPlusz


# ehezes(ehseg)
# vanPenze(penz)