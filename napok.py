import os
from statok import statPrint, getora, idoMeres, etel, tudasPlusz, getehseg, gettudas, Nap
from tevekenyseg import furdes, tanulas, szoba, voltSzoba, alvas, dogaEredmeny, varos, WC
furdottMar = False
voltvaros = False


def vasarnap():
    global voltSzoba
    global furdottMar
    Nap('vasarnap')
    print('Egy kollégista élete\n')
    print('Ön egy kollégista. Ebben a játékban figyelnie kell, hogy ne haljon éhen, és megtanuljon, hisz a héten minddennap ír valamiből. Lehetőleg pénzét se verje el. Megérkezett vasárnap a kollégiumba és sok lehetőség várja...')
    input('\nFolytatáshoz ENTER...')
    m = 0
    while m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
        while getora() < 22:
            os.system('cls')    
            statPrint()
            print('\n\n1...Elmegyek fürödni')
            print('\n2...Elmegyek tanulni')
            print('\n3...Bemegyek valakit meglátogatni')
            print('\n4...Elmegyek wcre')
            if voltSzoba == False:
                print('\n5...Bemegyek a szobámba')
            else:
                print('\n5...Maradok a szobában')
            m = input('\nMit csináljak? ')
            match m:
                case '1':
                    furdes(furdottMar)
                    voltSzoba = False
                case '2':
                    voltSzoba = tanulas(voltSzoba)
                case '3':
                    print('bemegyekValakihez')#func
                    voltSzoba = False
                case '4':
                    WC()
                    voltSzoba = False
                case '5':
                    szoba()
                    voltSzoba = True
        if getora() >= 22:
            os.system('cls')
            alvas()
            input('\nEnter a következő naphoz..')
            m = 0
            furdottMar = False
        break


def hetfo(): 
    global voltSzoba
    global furdottMar
    global voltvaros
    Nap('hetfo')
    os.system('cls')
    print(f'Hétfőn kipihenten állt neki a napnak, és megírt dolgozataira {dogaEredmeny()} és {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.')
    input('\nFolytatáshoz ENTER...')
    idoMeres(-8, 30)
    etel(-getehseg())
    etel(40)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    while m != 1 and m != 2 :
        while getora() < 22:
            if voltvaros == False:
                os.system('cls')    
                statPrint()
                print('\nMit kezdesz a déutánoddal')
                print('\n1...Bemegyek a városba')
                print('\n2...Visszamegyek a koliba')
                m = input('\nMit csináljak? ')
                voltvaros = True
            else:
                m = '2'
            match m:
                case '1':
                    varos()
                case '2':
                    os.system('cls')
                    statPrint()
                    print('\n\n1...Elmegyek fürödni')
                    print('\n2...Elmegyek tanulni')
                    print('\n3...Bemegyek valakihez meglátogatni')
                    print('\n4...Elmegyek wcre')
                    if voltSzoba == False:
                        print('\n5...Bemegyek a szobámba')
                    else:
                        print('\n5...Maradok a szobában')
                    j = input('\nMit csináljak? ')
                    match j:
                        case '1':
                            furdes(furdottMar)
                            voltSzoba = False
                        case '2':
                            tanulas(voltSzoba)
                        case '3':
                            print('bemegyekValakihez')#func
                            voltSzoba = False
                        case '4':
                            WC()
                            voltSzoba = False
                        case '5':
                            szoba()
                            voltSzoba = True
        if getora() >= 22:
            os.system('cls')
            alvas()
            input('\nEnter a következő naphoz..')
            m = '0'


def kedd(): 
    global voltSzoba
    global furdottMar
    global voltvaros
    Nap('kedd')
    os.system('cls')
    print(f'Hétfőn kipihenten állt neki a napnak, és megírt dolgozataira {dogaEredmeny()} és {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.')
    input('\nFolytatáshoz ENTER...')
    idoMeres(-8, 30)
    etel(-getehseg())
    etel(40)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    while m != 1 and m != 2 :
        while getora() < 22:
            if voltvaros == False:
                os.system('cls')    
                statPrint()
                print('\nMit kezdesz a déutánoddal')
                print('\n1...Bemegyek a városba')
                print('\n2...Visszamegyek a koliba')
                m = input('\nMit csináljak? ')
                voltvaros = True
            else:
                m = '2'
            match m:
                case '1':
                    varos()
                case '2':
                    os.system('cls')
                    statPrint()
                    print('\n\n1...Elmegyek fürödni')
                    print('\n2...Elmegyek tanulni')
                    print('\n3...Bemegyek valakihez meglátogatni')
                    print('\n4...Elmegyek wcre')
                    if voltSzoba == False:
                        print('\n5...Bemegyek a szobámba')
                    else:
                        print('\n5...Maradok a szobában')
                    j = input('\nMit csináljak? ')
                    match j:
                        case '1':
                            furdes(furdottMar)
                            voltSzoba = False
                        case '2':
                            tanulas(voltSzoba)
                        case '3':
                            print('bemegyekValakihez')#func
                            voltSzoba = False
                        case '4':
                            WC()
                            voltSzoba = False
                        case '5':
                            szoba()
                            voltSzoba = True
        if getora() >= 22:
            os.system('cls')
            alvas()
            input('\nEnter a következő naphoz..')
            m = '0'


def szerda(): 
    global voltSzoba
    global furdottMar
    global voltvaros
    Nap('szerda')
    os.system('cls')
    print(f'Hétfőn kipihenten állt neki a napnak, és megírt dolgozataira {dogaEredmeny()} és {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.')
    input('\nFolytatáshoz ENTER...')
    idoMeres(-8, 30)
    etel(-getehseg())
    etel(40)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    while m != 1 and m != 2 :
        while getora() < 22:
            if voltvaros == False:
                os.system('cls')    
                statPrint()
                print('\nMit kezdesz a déutánoddal')
                print('\n1...Bemegyek a városba')
                print('\n2...Visszamegyek a koliba')
                m = input('\nMit csináljak? ')
                voltvaros = True
            else:
                m = '2'
            match m:
                case '1':
                    varos()
                case '2':
                    os.system('cls')
                    statPrint()
                    print('\n\n1...Elmegyek fürödni')
                    print('\n2...Elmegyek tanulni')
                    print('\n3...Bemegyek valakihez meglátogatni')
                    print('\n4...Elmegyek wcre')
                    if voltSzoba == False:
                        print('\n5...Bemegyek a szobámba')
                    else:
                        print('\n5...Maradok a szobában')
                    j = input('\nMit csináljak? ')
                    match j:
                        case '1':
                            furdes(furdottMar)
                            voltSzoba = False
                        case '2':
                            tanulas(voltSzoba)
                        case '3':
                            print('bemegyekValakihez')#func
                            voltSzoba = False
                        case '4':
                            WC()
                            voltSzoba = False
                        case '5':
                            szoba()
                            voltSzoba = True
        if getora() >= 22:
            os.system('cls')
            alvas()
            input('\nEnter a következő naphoz..')
            m = '0'


def csutortok(): 
    global voltSzoba
    global furdottMar
    global voltvaros
    Nap('csutortok')
    os.system('cls')
    print(f'Hétfőn kipihenten állt neki a napnak, és megírt dolgozataira {dogaEredmeny()} és {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.')
    input('\nFolytatáshoz ENTER...')
    idoMeres(-8, 30)
    etel(-getehseg())
    etel(40)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    while m != 1 and m != 2 :
        while getora() < 22:
            if voltvaros == False:
                os.system('cls')    
                statPrint()
                print('\nMit kezdesz a déutánoddal')
                print('\n1...Bemegyek a városba')
                print('\n2...Visszamegyek a koliba')
                m = input('\nMit csináljak? ')
                voltvaros = True
            else:
                m = '2'
            match m:
                case '1':
                    varos()
                case '2':
                    os.system('cls')
                    statPrint()
                    print('\n\n1...Elmegyek fürödni')
                    print('\n2...Elmegyek tanulni')
                    print('\n3...Bemegyek valakihez meglátogatni')
                    print('\n4...Elmegyek wcre')
                    if voltSzoba == False:
                        print('\n5...Bemegyek a szobámba')
                    else:
                        print('\n5...Maradok a szobában')
                    j = input('\nMit csináljak? ')
                    match j:
                        case '1':
                            furdes(furdottMar)
                            voltSzoba = False
                        case '2':
                            tanulas(voltSzoba)
                        case '3':
                            print('bemegyekValakihez')#func
                            voltSzoba = False
                        case '4':
                            WC()
                            voltSzoba = False
                        case '5':
                            szoba()
                            voltSzoba = True
        if getora() >= 22:
            os.system('cls')
            alvas()
            input('\nEnter a következő naphoz..')
            m = '0'


vasarnap()
voltSzoba = False
voltvaros = False
furdottMar = False
hetfo()
voltSzoba = False
voltvaros = False
furdottMar = False
kedd()
voltSzoba = False
voltvaros = False
furdottMar = False
szerda()
voltSzoba = False
voltvaros = False
furdottMar = False
csutortok()



            
