import random
from main import idoMeres
from main import etel
from main import statPrint
from main import tudasPlusz
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
                elsovalasz = "Mégis bemész az állló vízes kabinba"
            case 2:
                problema = "de rossz a zuhany rózsa"
                elsovalasz = "Mégis bemész a kabinba"
            case 3:
                problema = "de koszos a kabin"
                elsovalasz = "Mégis lefürdesz a kabinban"
        print(f'Elmentem fürödni, {problema}.')
        print('Mit csinájak?')
        
        print(f'\n1.. {elsovalasz}')
        print('2.. Kinyomom a pattanásaim')
        print('3.. Beszélgetek')

        m = '0'
        while m != '1' and m != '2' and m != '3':
            m = input('Döntésem:  ')
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
        statPrint()

    else:
        print('Ma már fürödtem visszamegyek a szobába.')
        #SZOBA FUNCTION

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
