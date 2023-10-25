import random, os
from statok import idoMeres
from statok import etel
from statok import statPrint
from statok import tudasPlusz
from david import voltSzoba
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
        statPrint()
        print(f'\n\nElmentem fürödni, {problema}.')
        print('Mit tegyek? ')
        
        print(f'\n1.. {elsovalasz}')
        print('2.. Kinyomom a pattanásaim')
        print('3.. Beszélgetek')

        m = '0'
        while m != '1' and m != '2' and m != '3':
            m = input('\nDöntésem:  ')
            match m:
                case '1':
                    os.system('cls')
                    statPrint()
                    print('\n\nLefürödtem és vissza mentem a szobába.')
                    furdottMar = True
                    #SZOBA FUNCTION
                case '2':
                    os.system('cls')
                    statPrint()
                    print('\n\nKinyomtam a pattanásaimat, utána lefürödtem és visszamentem a szobába.')
                    furdottMar = True
                    #SZOBA FUNCTION
                case '3':
                    os.system('cls')
                    statPrint()
                    #JEDLIKES TÖRTÉNET
                    print('\n\nA beszélgetés után elmentem fürödni és visszamentem a szobába.')
                    furdottMar = True
                    #SZOBA FUNCTION
        
        etel(10)
        idoMeres(0, 30)
        input('\nENTER...')

    else:
        os.system('cls')
        statPrint()
        print('\n\nMa már fürödtem visszamegyek a szobába.')
        #SZOBA FUNCTION
        input('\nEnter: Vissza a szobába')

def tanulas():
    os.system('cls')
    global voltSzoba
    statPrint()

    print('\n\nHol tanuljak?')

    print('\n1.. Tanszoba')
    print('2.. Szoba')
    print('3.. Kistanuló')
    m = '0'
    while m != '1' and m != '2' and m != '3':
        m = input('\nDöntésem: ')
        match m:
            case '1':
                os.system('cls')
                statPrint()
                print('\n\nTanszobához menet barátom jött szembe.')
                print('\nBeszélgessek vele?')
                n = '0'
                while n != 'Igen' and n != 'Nem':
                    n = input('Igen/Nem: ')
                    match n:
                        case 'Igen':
                            os.system('cls')
                            statPrint()
                            #Elmeséli a történetet
                            print('\n\nA történet után elmentem a Tanszobába.')
                            tanul()
                        case 'Nem':
                            os.system('cls')
                            statPrint()
                            print('\n\nKöszöntem neki és tovább haladtam a Tanszobába.')
                            tanul()
                    voltSzoba = False
                        
    input('\nENTER...')
        

def tanul():
    tudasPlusz(30)
    print('Megtanultam a mai anyagot egy részét, holnap jobban fognak menni a dolgozatok')
    etel(20)
    idoMeres(1, 0)
#debug


'''
x = input("Fürdés_1 vagy Tanulás_2")
match x:
    case '1':
        furdes()
    case '2':
        tanul()
'''
