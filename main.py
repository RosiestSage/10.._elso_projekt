import os, random


#Változók----------------------------------
ora = 0
perc = 0
oraPlusz = 0
percPlusz = 0
ehseg = 0
penzem = 5000
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
    global ehseg
    ehseg += etelek
    if ehseg >= 100:
        print("Éhezem meghaltam")
    else:
        print(f"Éhség szint: {ehseg}")

# vanPenze(penz)

def penz(penzPlusz):
    global penzem
    penzem += penzPlusz
    if penzem <= 0:
        print("Nincs pénz")
    else:
        print(f"Jelenleg {penzem} forintod van")