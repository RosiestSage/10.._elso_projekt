import os, random


#Változók----------------------------------
ora = 18
perc = 0
oraPlusz = 0
percPlusz = 0
ehseg = 0
tudas = 40
penzem = 5000
#------------------------------------------
def idoMeres(oraPlusz,percPlusz):
    global ora
    global perc
    perc += percPlusz
    if perc >= 60:
        ora += 1
        perc -= 60
    ora += oraPlusz

#Stat print placeholder
def statPrint():
    global ora
    global perc
    global ehseg
    global tudas
    global penzem
    print(f'Idő: {ora}:{perc:02}', end='')
    print(f'\t\t\t\tÉhség: {ehseg}')
    print(f'Pénz: {penzem}', end='')
    print(f'\t\t\t\tTudás: {tudas}')

# ehezes(ehseg)

def etel(etelek):
    global ehseg
    ehseg += etelek
    if ehseg >= 100:
        print("Éhezem meghaltam")
    elif ehseg >= 70:
        print(f'{ehseg}% az éhséged, menj el enni!')
    
#tudas

def tudasPlusz(pluszTudas):
    global tudas
    tudas += pluszTudas

# vanPenze(penz)

def penz(penzPlusz):
    global penzem
    penzem += penzPlusz
    if penzem <= 0:
        print("Nincs pénz")
    else:           #Később átírni ha nem biztos van pénze ételre
        print(f"Jelenleg {penzem} forintod van")

