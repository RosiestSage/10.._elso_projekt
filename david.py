import random, os
from statok import tudas
voltSzoba = False
from statok import etel, getehseg
from statok import statPrint

def dogaEredmeny():
    if tudas >= 100:
        jegy = 5
    elif tudas >= 80 and tudas < 100:
        jegy = random.randint(4,5)
    elif tudas >= 40 and tudas < 80:
        jegy = random.randint(2,4)
    elif tudas < 40:
        jegy = random.randint(1,3)
    print(jegy)
    return jegy


def szoba():
    statPrint()
    ehseg = getehseg()
    global voltSzoba
    os.system('cls')
    if voltSzoba == False:
        print('Bementem a szobámba')
        voltSzoba = True
    else:
        print('A szobában maradtam')
    
    print("\n1...Leülök a székre")
    print("\n2...Leülök az ágyra")
    m = input("\nHova mész? ")
    os.system("cls")
    statPrint()
    print("\n1...Eszek")
    print("\n2...Telefonozok")
    print("\n3...Tanulok")
    print("\n4...Játszok")
    print("\n5...Beszélgetek")
    print("\n6...Alvás")
    m = input("\nMit csinálok? ")
    match m:
        case '1':
            if ehseg > 15:
                etel() -15
                input("Enter")
            elif ehseg < 15 and ehseg > 0:
                etel() - ehseg
                input("Enter")
            elif ehseg == 0:
                os.system("cls")
                print("Tele vagy, nem tudsz ennni egy falatot se")
                input("Enter")

    