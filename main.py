import os
from statok import statPrint, getora, idoMeres, etel, tudasPlusz, getehseg, gettudas, Nap, helySzin
from tevekenyseg import furdes, tanulas, szoba, voltSzoba, alvas, dogaEredmeny, varos, WC, vacsora
furdottMar = False
voltvaros = False
vacsiMar = False

def vasarnap():
    global voltSzoba
    global furdottMar
    Nap('vasarnap')
    helySzin('Kollégium') 
    print('Egy kollégista élete\n')
    statPrint()
    print('\n Ön egy kollégista. Ebben a játékban figyelnie kell, hogy ne haljon éhen, és megtanuljon, hisz a héten minddennap ír valamiből. Lehetőleg pénzét se verje el. Megérkezett vasárnap a kollégiumba és sok lehetőség várja...')
    input('\nFolytatáshoz ENTER...')

    m = 0
    while m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
        while getora() < 22:
            os.system('cls')   
            helySzin('Folyosó') 
            statPrint()
            print('\n\n1...Elmegyek fürödni')
            print('\n2...Elmegyek tanulni')
            print('\n3...Bemegyek valakit meglátogatni')
            print('\n4...Elmegyek wcre')
            print('\n5...Bemegyek a szobámba')
            m = input('\nMit csináljak? ')
            match m:
                case '1':
                    furdes()                    
                    szoba()
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
    global vacsiMar
    Nap('hetfo')
    helySzin('Jedlik ajtaja előtt')
    os.system('cls')
    print(f'Hétfőn kipihenten állt neki a napnak, és megírt dolgozataira {dogaEredmeny()} és {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon. \n~A mai napon lehetősége nyílik különböző sportokat játszani a kollégiumban.~')
    input('\nFolytatáshoz ENTER...')
    idoMeres(-1, 30)
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
                    helySzin('Folyosó')
                    os.system('cls')
                    statPrint()
                    print('\n\n1...Elmegyek fürödni')
                    print('\n2...Elmegyek tanulni')
                    print('\n3...Bemegyek valakihez meglátogatni')
                    print('\n4...Elmegyek wcre')
                    print('\n5...Maradok a szobában')
                    if getora() >= 18 and getora() <19 and vacsiMar == False and getehseg() > 0:
                        print('\n6...Vacsora')
                    j = input('\nMit csináljak? ')
                    match j:
                        case '1':
                            furdes()
                            szoba()
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
                        case '6':
                            vacsora()
                            vacsiMar = True
        if getora() >= 22:
            os.system('cls')
            alvas()
            input('\nEnter a következő naphoz..')
            m = 0
        break


def kedd(): 
    global voltSzoba
    global furdottMar
    global voltvaros
    Nap('kedd')
    helySzin('Jedlik ajtaja előtt')
    os.system('cls')
    print(f'Sok óra alvás után kipihenten állt neki a napnak, és megírt dolgozatára és feleletére {dogaEredmeny()} és {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.\n~A mai napon még a Tanárit is meglátogathatja.~')
    input('\nFolytatáshoz ENTER...')
    idoMeres(-9, 10)
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
                    if getora() >= 18 and getora() <19 and vacsiMar == False and getehseg() > 0:
                        print('\n6...Vacsora')
                    j = input('\nMit csináljak? ')
                    match j:
                        case '1':
                            furdes()
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
        break


def szerda(): 
    global voltSzoba
    global furdottMar
    global voltvaros
    helySzin('Jedlik ajtaja előtt')
    Nap('szerda')
    os.system('cls')
    print(f'Szerdán kipihenten állt neki a napnak, és megírt dolgozatára {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.\n~A mai napon Gergő segítségedet kérte a jövő heti kollégiumi buli megszervezésében.~')
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
                    if getora() >= 18 and getora() <19 and vacsiMar == False and getehseg() > 0:
                        print('\n6...Vacsora')
                    j = input('\nMit csináljak? ')
                    match j:
                        case '1':
                            furdes()
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
        break


def csutortok(): 
    global voltSzoba
    global furdottMar
    global voltvaros
    helySzin('Jedlik ajtaja előtt')
    Nap('csutortok')
    os.system('cls')
    print(f'Csütörtökön kipihenten és a közelgő hétvége reményében ment iskolában, és megírt dolgozataira {dogaEredmeny()} és {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.')
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
                    if getora() >= 18 and getora() <19 and vacsiMar == False and getehseg() > 0:
                        print('\n6...Vacsora')
                    j = input('\nMit csináljak? ')
                    match j:
                        case '1':
                            furdes()
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
        break


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



            
