import os
from statok import statPrint, getora, idoMeres, etel, tudasPlusz, getehseg, gettudas, Nap, helySzin
from tevekenyseg import furdes, tanulas, szoba, voltSzoba, alvas, dogaEredmeny, varos, WC, vacsora, sport, tanari, csocsoBajnoksag, buliszervezes, bulistatok, jegyek, jatekvege, valakiSzobaja
furdottMar = False
voltvaros = False
vacsiMar = False
csocso = False
megszervezve = False

def vasarnap():
    global voltSzoba
    global furdottMar
    Nap('vasarnap')
    helySzin('Kollégium') 
    print('Egy kollégista élete')
    print('\nEbben a játékban egy kollégista tanuló vagy. Figyelned kell, hogy ne halj éhen, és megtanulj, hisz a héten mindennap írsz vagy felelsz valamiből. Pénzed se verdd el (nem kötelező). A játék a Kollégium területén játszódik, ezen belül mászkálhatsz különböző helyszínekre, ahol statisztikáid változnak, amik a következő képpen jelennek meg: \n')
    statPrint()
    print('\nSok sikert és eredményes hetet!')
    input('\nFolytatáshoz ENTER..')
    m = 0
    
    while m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
        while getora() < 22:
            ehseg = getehseg()
            if ehseg < 100:
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
                        valakiSzobaja()
                        voltSzoba = False
                    case '4':
                        WC()
                        voltSzoba = False
                    case '5':
                        szoba()
            else:
                n = '0'
                while n != '1':
                    os.system('cls')
                    print('\nÉhen haltál')
                    input("Enter a kilépéshez..")
                    quit()
            if getora() >= 22:
                os.system('cls')
                alvas()
                input('\nEnter a következő naphoz..')
                # m = 0
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
    jegy = dogaEredmeny()
    jegy2 = dogaEredmeny()
    jegyek(jegy)
    jegyek(jegy2)
    print(f'Hétfőn kipihenten állt neki a napnak, és megírt dolgozataira {jegy} és {jegy2} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon. \n~A mai naptól lehetősége nyílik különböző sportokat játszani a kollégiumban.~')
    input('\nFolytatáshoz ENTER..')
    idoMeres(-8, 30)
    etel(-getehseg())
    etel(40)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    visszament = False
    while m != 1 and m != 2 :
        while getora() < 22:
            ido = getora()
            ehseg = getehseg()
            if ehseg < 100:
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
                        if visszament == False:
                            idoMeres(0, 20)
                            visszament = True
                        helySzin('Folyosó')
                        os.system('cls')
                        statPrint()
                        print('\n\n1...Elmegyek fürödni')
                        print('\n2...Elmegyek tanulni')
                        print('\n3...Bemegyek valakit meglátogatni')
                        print('\n4...Elmegyek wcre')
                        print('\n5...Bemegyek a szobámba')
                        print('\n6...Sport')
                        if ido >= 18 and ido <19 and vacsiMar == False and ehseg > 0:
                            print('\n7...Vacsora')
                        j = input('\nMit csináljak? ')
                        match j:
                            case '1':
                                furdes()
                                szoba()
                            case '2':
                                tanulas(voltSzoba)
                            case '3':
                                valakiSzobaja()
                                voltSzoba = False
                            case '4':
                                WC()
                                voltSzoba = False
                            case '5':
                                szoba()
                                voltSzoba = True
                            case '6':
                                sport()
                            case '7':
                                vacsiMar = vacsora(vacsiMar)
            else:
                n = '0'
                while n != '1':
                    os.system('cls')
                    print('\nÉhen haltál')
                    input('Enter a kilépéshez..')
                    quit()        
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
    global vacsiMar
    Nap('kedd')
    helySzin('Jedlik ajtaja előtt')
    os.system('cls')
    jegy = dogaEredmeny()
    jegy2 = dogaEredmeny()
    jegyek(jegy)
    jegyek(jegy2)
    print(f'Kedden a sok óra alvás után kipihenten állt neki a napnak, és megírt dolgozatára és feleletére {jegy} és {jegy2} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.\n~Csak mai napon még a Tanárit is meglátogathatja.~')
    input('\nFolytatáshoz ENTER..')
    idoMeres(-9, 10)
    etel(-getehseg())
    etel(40)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    while m != 1 and m != 2 :
        while getora() < 22:
            ido = getora()
            ehseg = getehseg()
            if ehseg < 100:
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
                        print('\n3...Bemegyek valakit meglátogatni')
                        print('\n4...Elmegyek wcre')
                        print('\n5...Bemegyek a szobámba')
                        print('\n6...Sport')
                        print('\n7...Tanári')
                        if ido >= 18 and ido <19 and vacsiMar == False and ehseg > 0:
                            print('\n8...Vacsora')
                        j = input('\nMit csináljak? ')
                        match j:
                            case '1':
                                furdes()
                                szoba()
                            case '2':
                                tanulas(voltSzoba)
                            case '3':
                                valakiSzobaja()
                                voltSzoba = False
                            case '4':
                                WC()
                                voltSzoba = False
                            case '5':
                                szoba()
                                voltSzoba = True
                            case '6':
                                sport()
                            case '7':
                                tanari()
                            case '8':
                                vacsiMar = vacsora(vacsiMar)
            else:
                n = '0'
                while n != '1':
                    os.system('cls')
                    print('\nÉhen haltál')
                    input('Enter a kilépéshez..')
                    quit()
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
    global vacsiMar
    global megszervezve
    helySzin('Jedlik ajtaja előtt')
    Nap('szerda')
    os.system('cls')
    jegy = dogaEredmeny()
    jegyek(jegy)
    print(f'Szerdán kipihenten állt neki a napnak, és megírt dolgozatára {jegy} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.\n~A mai napon Gergő segítségedet kérte a jövő heti kollégiumi buli megszervezésében.~')
    input('\nFolytatáshoz ENTER..')
    idoMeres(-8, 30)
    etel(-getehseg())
    etel(40)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    while m != 1 and m != 2 :
        while getora() < 22:
            ido = getora()
            ehseg = getehseg()
            if ehseg < 100:
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
                        print('\n3...Bemegyek valakit meglátogatni')
                        print('\n4...Elmegyek wcre')
                        print('\n5...Bemegyek a szobámba')
                        print('\n6...Sport')
                        print('\n7...Buliszervezés')
                        if ido >= 18 and ido <19 and vacsiMar == False and ehseg > 0:
                            print('\n8...Vacsora')
                        j = input('\nMit csináljak? ')
                        match j:
                            case '1':
                                furdes()
                                szoba()
                            case '2':
                                tanulas(voltSzoba)
                            case '3':
                                valakiSzobaja()
                                voltSzoba = False
                            case '4':
                                WC()
                                voltSzoba = False
                            case '5':
                                szoba()
                                voltSzoba = True
                            case '6':
                                sport()
                            case '7':
                                if megszervezve == False:
                                    buliszervezes()
                                    megszervezve = True
                                else:
                                    bulistatok()
                            case '8':
                                vacsiMar = vacsora(vacsiMar)
            else:
                n = '0'
                while n != '1':
                    os.system('cls')
                    print('\nÉhen haltál')
                    input('Enter a kilépéshez..')
                    quit()
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
    global vacsiMar
    global csocso 
    helySzin('Jedlik ajtaja előtt')
    Nap('csutortok')
    os.system('cls')
    jegy = dogaEredmeny()
    jegy2 = dogaEredmeny()
    jegyek(jegy)
    jegyek(jegy2)
    print(f'Csütörtökön kipihenten és a közelgő hétvége reményében ment iskolában, és megírt dolgozataira {jegy} és {jegy2} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.')
    input('\nFolytatáshoz ENTER..')
    idoMeres(-8, 30)
    etel(-getehseg())
    etel(40)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    while m != 1 and m != 2 :
        while getora() < 22:
            ido = getora()
            ehseg = getehseg()
            if ehseg < 100:
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
                        print('\n3...Bemegyek valakit meglátogatni')
                        print('\n4...Elmegyek wcre')
                        print('\n5...Bemegyek a szobámba')
                        print('\n6...Csocsóbajnokság')
                        print('\n7...Sport')
                        if ido >= 18 and ido <19 and vacsiMar == False and ehseg > 0:
                            print('\n7...Vacsora')
                        j = input('\nMit csináljak? ')
                        match j:
                            case '1':
                                furdes()
                                szoba()
                            case '2':
                                tanulas(voltSzoba)
                            case '3':
                                valakiSzobaja()
                                voltSzoba = False
                            case '4':
                                WC()
                                voltSzoba = False
                            case '5':
                                szoba()
                                voltSzoba = True
                            case '6':
                                if csocso == False:
                                    gyozelem = csocsoBajnoksag(csocso)
                                    csocso = True
                                else:
                                    os.system("cls")
                                    statPrint()
                                    if gyozelem == True:
                                        print('\nA bajnokságnak már vége, győztél')
                                        input('\nENTER')
                                    else:
                                        print('\nA bajnokságnak már vége, vesztettél')
                                        input('\nENTER')
                            case '7':
                                sport()
                            case '8':
                                vacsiMar = vacsora(vacsiMar)
            else:
                n = '0'
                while n != '1':
                    os.system('cls')
                    print('\nÉhen haltál')
                    input('Enter a kilépéshez..')
                    quit()
            if getora() >= 22:
                os.system('cls')
                alvas()
                input('\nEnter a következő naphoz..')
                m = '0'
        break

'''
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
'''
csutortok()
jatekvege()




            
