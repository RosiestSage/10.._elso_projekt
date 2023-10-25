import os
global ora
from statok import ora
from statok import statPrint
from tevekenyseg import furdes
from tevekenyseg import tanulas
from david import szoba, voltSzoba


def vasarnap():
    global ora
    global voltSzoba
    print('Egy kollégista élete\n')
    print('Ön egy kollégista. Ebben a játékban figyelnie kell, hogy ne haljon éhen, és megtanuljon, hisz a héten minddennap ír valamiből. Lehetőleg pénzét se verje el. Megérkezett vasárnap a kollégiumba és sok lehetőség várja...')
    #Bevezető szöveg
    input('\nFolytatáshoz ENTER...')
    
    while ora < 22:   
        m = 0
        while m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
            os.system('cls')    
            print('\n\n', statPrint())
            print('\n\n1...Elmegyek fürödni')
            print('\n2...Elmegyek tanulni')
            print('\n3...Bemegyek valakihez meglátogatni')
            print('\n4...Elmegyek wcre')
            if voltSzoba == False:
                print('\n5...Bemegyek a szobámba')
            else:
                print('\n5...Maradok a szobában')
            m = input('\nMit csináljak? ')
            match m:
                case '1':
                    furdes()
                    voltSzoba = False
                case '2':
                    tanulas()
                case '3':
                    print('bemegyekValakihez')#func
                    voltSzoba = False
                case '4':
                    print('bemegyekWCre')#func
                    voltSzoba = False
                case '5':
                    szoba()
                    voltSzoba = True

        input('Enter a folytatáshoz..')

    if ora >= 22:
        print('Elég fáradt vagyok, elmegyek aludni.')
        print('alvas')#func

