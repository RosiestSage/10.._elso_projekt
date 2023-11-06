import random, os
from statok import etel, getehseg, idoMeres, tudas, tudasPlusz, statPrint, getora, perc, getperc, getnap, ora, penz, getpenz, gettudas

def kezmosas():
    os.system('cls')
    statPrint()
    
    j = '0'
    print('\n1.. Kezet mosok')
    print('2.. Nem mosok kezet')
    while j != '1' and j != '2':
        j = input('\nMit tegyek:')
        match j:
            case '1':
                print('Kezet mostam, és kimentem a WC-ből')
                input('\nENTER...')
                WC()
            case '2':
                print('Nem mostam kezet, ezért koszos maradt.')
                input('\nENTER...')
                WC()

def WC():
    x = random.randint(1, 4)
    problema = ""
    valasz = ""
    match x:
        case 1: 
            problema = "de bele kell állnom a pisibe."
            valasz = "de bele kellett állnom a pisibe."
        case 2:
            problema = "de nem húzódik le."
            valasz = "de nem húzódott le, hugyszag volt."
        case 3:
            problema = "de körbe van pisilve." 
            valasz = "de hugyszag volt."
        case 4:
            problema = ""
        
    m = '0'
    while m != '1' and m != '2' and m != '3' and m != '4' and m != '5' and m != '6' and m != '7':
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
        m = input('\nDöntésem: ')

        if x == 1 or x == 2 or x == 3:
            match m:
                case '1' :
                    os.system('cls')
                    statPrint()

                    n = 0
                    while n != 'Igen' and n != 'Nem':
                        print(f'\nOdamentem, {problema}')
                        n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                        os.system('cls')
                        statPrint()
                        match n:
                            case 'Igen':
                                print(f'\nElvégeztem a dolgomat, {valasz}')
                                input('ENTER...')
                                kezmosas()
                            case 'Nem':
                                WC()
                case '2':
                        os.system('cls')
                        statPrint()
                        print('\nKözépen buzis pisilni...')
                        input('\nENTER...')
                        kezmosas()

                case '3':
                    os.system('cls')
                    statPrint()

                    n = 0
                    while n != 'Igen' and n != 'Nem':
                        print(f'\nOdamentem, {problema}')
                        n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                        os.system('cls')
                        statPrint()
                        match n:
                            case 'Igen':
                                print(f'\nElvégeztem a dolgomat, {valasz}')
                                input('ENTER...')
                                kezmosas()
                            case 'Nem':
                                WC()

                case '4':
                    os.system('cls')
                    statPrint()

                    n = 0
                    while n != 'Igen' and n != 'Nem':
                        print(f'\nOdamentem, {problema}')
                        n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                        os.system('cls')
                        statPrint()
                        match n:
                            case 'Igen':
                                print(f'\nElvégeztem a dolgomat, {valasz}')
                                input('ENTER...')
                                kezmosas()
                            case 'Nem':
                                WC()

                case '5':
                    os.system('cls')
                    statPrint()

                    n = 0
                    while n != 'Igen' and n != 'Nem':
                        print(f'\nOdamentem, {problema}')
                        n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                        os.system('cls')
                        statPrint()
                        match n:
                            case 'Igen':
                                print(f'\nElvégeztem a dolgomat, {valasz}')
                                input('ENTER...')
                                kezmosas()
                            case 'Nem':
                                WC()

                case '6':
                    os.system('cls')
                    statPrint()

                    n = 0
                    while n != 'Igen' and n != 'Nem':
                        print(f'\nOdamentem, {problema}')
                        n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                        os.system('cls')
                        statPrint()
                        match n:
                            case 'Igen':
                                print(f'\nElvégeztem a dolgomat, {valasz}')
                                input('ENTER...')
                                kezmosas()
                            case 'Nem':
                                WC()

                case '7':
                    os.system('cls')
                    statPrint()

                    n = 0
                    while n != 'Igen' and n != 'Nem':
                        print(f'\nOdamentem, {problema}')
                        n = input('Mégis itt végzed el a dolgodat? (Igen/Nem): ')
                        os.system('cls')
                        statPrint()
                        match n:
                            case 'Igen':
                                print(f'\nElvégeztem a dolgomat, {valasz}')
                                input('ENTER...')
                                kezmosas()
                            case 'Nem':
                                WC()
            

        elif x == 4:
            if m == '2':
                os.system('cls')
                statPrint()
                print('\nKözépen buzis pisilni...')
                input('\nENTER...')
                kezmosas()
            else:
                os.system('cls')
                statPrint()
                print('\nElvégeztem a dolgomat.')
                input('\nENTER...')
                kezmosas()
WC()