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

def etel(etelek):
    global ehezes
    ehezes += etelek
    if ehezes >= 100:
        print("Éhezem meghaltam")
    else:
        print(f"Éhség szint: {ehezes}")

# vanPenze(penz)

def penz(penzek):
    global forint
    forint += becsuletesseg
    if forint <= 0:
        print("Nincs pénz")
    else:
        print(f"Jelenleg {penz} forintod van")