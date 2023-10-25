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
                    n = input('Igen/Nem:')
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

def WC():
    x = random.randint(1, 5)
    problema = ""
    valasz = ""
    match x:
        case 1:
            problema = "de bele kell állnom a pisibe"
            valasz = "de bele kellett állnom a pisibe"
        case 2:
            problema = "de nem húzódik le"
            valasz = "de nem húzódik le, hugyszag van"
        case 3:
            problema = "de foglalt"
        case 4:
            problema = "de körbe van pisilve"
        case 5:
            problema = "és nincs semmi baja"
    os.system('cls')
    statPrint()
    print('\nHol wc-zzek?')

    print('\n1.. Első piszoár')
    print('\n2.. Második piszoár')
    print('\n3.. Harmadik piszoár')
    print('\n4.. Első fülke')
    print('\n5.. Második fülke')
    print('\n6.. Harmadik fülke')
    print('\n7.. Negyedik fülke')
    
    m = 0
    while m != 1 and m != 2 and m != 3 and m != 4 and m != 5 and m != 6 and m != 7:
        m = input('Döntésem: ')
        match m:
            case '1':
                os.system('cls')
                statPrint()
                print(f'Odamentem, {problema}')

                n = 0
                while n != 'Igen' and n != 'Nem':
                    n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                    match n:
                        case 'Igen':
                            print('Elvégeztem a dolgomat.')

            case '2':
                os.system('cls')
                statPrint()
                print('\nKözépen buzis pisilni.')
                input('\nENTER...')
                WC()

            case '3':
                os.system('cls')
                statPrint()
                print(f'Odamentem, {problema}')

                n = 0
                while n != 'Igen' and n != 'Nem':
                    n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                    match n:
                        case 'Igen':
                            print('Elvégeztem a dolgomat.')
                        case 'Nem':
                            print(f'Elvégeztem a dolgomat, {valasz}')

            case '4':
                os.system('cls')
                statPrint()
                print(f'Odamentem, {problema}')

                n = 0
                while n != 'Igen' and n != 'Nem':
                    n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                    match n:
                        case 'Igen':
                            print('Elvégeztem a dolgomat.')
                        case 'Nem':
                            print(f'Elvégeztem a dolgomat, {valasz}')
            case '5':
                os.system('cls')
                statPrint()
                print(f'Odamentem, {problema}')

                n = 0
                while n != 'Igen' and n != 'Nem':
                    n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                    match n:
                        case 'Igen':
                            print('Elvégeztem a dolgomat.')
                        case 'Nem':
                            print(f'Elvégeztem a dolgomat, {valasz}')

            case '6':
                os.system('cls')
                statPrint()
                print(f'Odamentem, {problema}')

                n = 0
                while n != 'Igen' and n != 'Nem':
                    n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                    match n:
                        case 'Igen':
                            print('Elvégeztem a dolgomat.')
                        case 'Nem':
                            print(f'Elvégeztem a dolgomat, {valasz}')

            case '7':
                os.system('cls')
                statPrint()
                print(f'Odamentem, {problema}')

                n = 0
                while n != 'Igen' and n != 'Nem':
                    n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                    match n:
                        case 'Igen':
                            print('Elvégeztem a dolgomat.')
                        case 'Nem':
                            print(f'Elvégeztem a dolgomat, {valasz}')