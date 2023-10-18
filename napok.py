import os
global ora
from statok import ora
from statok import statPrint
from tevekenyseg import furdes
from tevekenyseg import tanulas

def vasarnap():
    global ora
    print('Fhú, holnap megint iskola, neki kellene állnom tanulni, úgyse a legjobbak a jegyeim.')
    #Bevezető szöveg
    input('\nENTER...')
    
    while ora < 22:   
        m = 0
        while m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
            os.system('cls')    
            print('\n\n', statPrint())
            print('\n\n1...Elmegyek fürödni')
            print('\n2...Elmegyek tanulni')
            print('\n3...Bemegyek valakihez meglátogatni')
            print('\n4...Elmegyek wcre')
            print('\n5...Bemegyek a szobámba')
            m = input('\nMit csináljak? ')
            match m:
                case '1':
                    furdes()
                case '2':
                    tanulas()
                case '3':
                    print('bemegyekValakihez')#func
                case '4':
                    print('bemegyekWCre')#func
                case '5':
                    print('bemegyekSzobamba')#func

        input('Enter a folytatáshoz..')

    if ora >= 22:
        print('Elég fáradt vagyok, elmegyek aludni.')
        print('alvas')#func

