import random, os
voltSzoba = False
from statok import etel, getehseg, idoMeres, tudas, tudasPlusz
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
        print("\n1...Leülök a székre")
        print("\n2...Leülök az ágyra")
        m = input("\nHova mész? ")
        voltSzoba = True
    else:
        os.system("cls")
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
                os.system("cls")
                print("Ettél valamennyit és így már kevésbé vagy éhes")
                input("Enter")
                etel(-15)
                idoMeres(0, 20)
            elif ehseg <= 15 and ehseg > 0:
                os.system("cls")
                print("Ettél valamennyit és már egyáltalán nem vagy éhes")
                input("Enter")
                etel(-ehseg)
                idoMeres(0, 20)
            elif ehseg == 0:
                os.system("cls")
                print("Tele vagy, nem tudsz ennni egy falatot se")
                input("Enter")
        case '2':
            os.system("cls")
            print("Elfeküdtél és jól körbenéztél a közösségi oldalokon")
            input("Enter") 
            etel(5)
            idoMeres(0, 45)           
        case '3':   
            os.system("cls")
            print("Mivel úgy döntöttél, hogy tanulsz, mégjobban készen állsz a holnapi napra")
            input("Enter")
            etel(20)
            idoMeres(0, 45)  
            tudasPlusz(20)
        # case '4':
        # case '5':
        # case '6':
    
