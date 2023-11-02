#Változók----------------------------------
ora = 18
perc = 0
oraPlusz = 0
percPlusz = 0
milyenNap = ''
nap = ''
laptop = True
ehseg = 0
tudas = 20
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
        print(f'\n{ehseg}% az éhséged, menj el enni!')
    
#tudas

def tudasPlusz(pluszTudas):
    global tudas
    tudas += pluszTudas
    if tudas > 100:
        tudas -= (tudas-100)

# vanPenze(penz)

def penz(penzPlusz):
    global penzem
    penzem += penzPlusz
    if penzem <= 0:
        print("Nincs pénz")
    # else:           #Később átírni ha nem biztos van pénze ételre
    #     print(f"Jelenleg {penzem} forintod van")

#milyen nap van

def Nap(milyenNap):
    global nap
    nap = milyenNap
    return nap

#változók átvitele
def getnap():
    global nap
    return nap

def getehseg():
    global ehseg 
    return ehseg

def getora():
    global ora
    return ora

def getperc():
    global perc
    return perc

def gettudas():
    global tudas
    return tudas