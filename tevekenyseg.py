import random, os
from statok import idoMeres
from statok import etel
from statok import statPrint
from statok import tudasPlusz
furdottMar = False


def furdes():
    global furdottMar
    if furdottMar == False:
        x = random.randint(1, 3)
        problema = ""
        elsovalasz = ""
        match x:
            case 1:
                problema = "de a szabad kabinban áll a víz"
                elsovalasz = "Mégis bemegyek az álló vízes kabinba"
            case 2:
                problema = "de rossz a zuhany rózsa"
                elsovalasz = "Mégis bemegyek a kabinba"
            case 3:
                problema = "de koszos a kabin"
                elsovalasz = "Mégis lefürdök a kabinban"
        os.system('cls')
        print(f'\nElmentem fürödni, {problema}.')
        print('Mit tegyek? ')
        
        print(f'\n1.. {elsovalasz}')
        print('2.. Kinyomom a pattanásaim')
        print('3.. Beszélgetek')

        m = '0'
        while m != '1' and m != '2' and m != '3':
            m = input('\nDöntésem:  ')
        match m:
            case '1':
                print('\nLefürödtem és vissza mentem a szobába.')
                furdottMar = True
                #SZOBA FUNCTION
            case '2':
                print('\nKinyomtam a pattanásaimat, utána lefürödtem és visszamentem a szobába.')
                furdottMar = True
                #SZOBA FUNCTION
            case '3':
                #JEDLIKES TÖRTÉNET
                print('\nA beszélgetés után elmentem fürödni és visszamentem a szobába.')
                furdottMar = True
                #SZOBA FUNCTION
        
        etel(10)
        idoMeres(0, 30)
        # statPrint()
        input('ENTER...')

    else:
        os.system('cls')
        print('\nMa már fürödtem visszamegyek a szobába.')
        #SZOBA FUNCTION
        input('\nEnter: Vissza a szobába')

def tanul():
    tudasPlusz(30)
    print('Megtanultam a mai anyagot, holnap jobban fognak menni a dolgozatok')
    etel(20)
    idoMeres(1, 0)
    statPrint()
#debug
'''
x = input("Fürdés_1 vagy Tanulás_2")
match x:
    case '1':
        furdes()
    case '2':
        tanul()
'''
