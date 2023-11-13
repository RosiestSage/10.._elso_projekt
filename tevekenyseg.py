import random, os
from statok import etel, getehseg, idoMeres, tudas, tudasPlusz, statPrint, getora, perc, getperc, getnap, ora, penz, getpenz, gettudas, helySzin

#Furdo
furdottMar = False

#Szoba
voltSzoba = False
voltPenz = False
toltott = False
voltmar = True
elso = True
keddentoltott = False
javitas = False
m = '0'

#Tanari
kiulo = False

#Buli
italAr = 0
szenyoAr = 0
dj = ''
Szerep = ''

def furdes():
    helySzin('Fürdő')
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
                problema = "de koszos a szabad kabin"
                elsovalasz = "Mégis lefürdök a kabinban"

        m = '0'
        while m != '1' and m != '2' and m != '3':
            os.system('cls')
            statPrint()
            print(f'\n\nElmentem fürödni, {problema}.')
            print('Mit tegyek? ')
            
            print(f'\n1.. {elsovalasz}')
            print('2.. Kinyomom a pattanásaim')
            print('3.. Beszélgetek')
            m = input('\nDöntésem:  ')
            match m:
                case '1':
                    os.system('cls')
                    statPrint()
                    print('\n\nLefürödtem és vissza mentem a szobába.')
                    input('\nEnter: Vissza a szobába')
                    furdottMar = True
                    etel(10)
                    idoMeres(0, 30)

                case '2':
                    os.system('cls')
                    statPrint()
                    print('\n\nKinyomtam a pattanásaimat, utána lefürödtem és visszamentem a szobába.')
                    input('\nEnter: Vissza a szobába')
                    furdottMar = True
                    etel(10)
                    idoMeres(0, 30)

                case '3':
                    os.system('cls')
                    statPrint()
                    #JEDLIKES TÖRTÉNET
                    print('\n\nA beszélgetés után elmentem fürödni és visszamentem a szobába.')
                    input('\nEnter: Vissza a szobába')
                    furdottMar = True
                    etel(10)
                    idoMeres(0, 30)


    else:
        os.system('cls')
        statPrint()
        print('\n\nMa már fürödtem visszamegyek a szobába.')
        #SZOBA FUNCTION
        input('\nEnter: Vissza a szobába')
    return furdottMar


def tanulas(voltSzoba):

    m = '0'
    while m != '1' and m != '2' and m != '3':
        os.system('cls')
        statPrint()
        print('\n\nHol tanuljak?')

        print('\n1.. Tanszoba')
        print('2.. Szoba')
        print('3.. Kistanuló')
        m = input('\nDöntésem: ')
        match m:
            case '1':
                n = '0'
                while n != 'Igen' and n != 'Nem':
                    os.system('cls')
                    statPrint()
                    helySzin('Tanulószoba')
                    print('\n\nTanszobához menet barátom jött szembe.')
                    print('\nBeszélgessek vele?')
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
            
            case '2':
                n = '0'
                while n != '1' and n != '2' and n != '3':
                    os.system('cls')
                    helySzin('Szoba')
                    statPrint()
                    print('\n\nMaradok a szobában tanulni, de szobatársam zavar.')
                    print('\n1.. Szólok, hogy hagyja abba')
                    print('2.. Elmegyek máshova tanulni')
                    n = input('\nMit tegyek? ')
                    match n:
                        case '1':
                            os.system('cls')
                            statPrint()
                            print('\n\nSzobatársam csendben maradt és megtanultam.')
                            tanul()
                        case '2':
                            os.system('cls')
                            statPrint()
                            print('\n\nKimegyek a szobából és máshova megyek tanulni.')
                            input('ENTER...')
                            os.system('cls')
                            statPrint()
                            m = '0'
                voltSzoba = True
            case '3':
                n = '0'
                while n != '1' and n != '2':
                    os.system('cls')
                    statPrint()
                    helySzin('Kistanuló')
                    print('\n\nElmentem a kistanulóba, de az ajtó zárva.')
                    print('\n1.. Elkérem a kulcsot')
                    print('2.. Tanulok máshol')
                    n = input('\nMit csináljak? ')
                    match n:
                        case '1':
                            os.system('cls')
                            statPrint()
                            print('\n\nElkértem a kulcsot és megtanultam.')
                            tanul()

                        case '2':
                            os.system('cls')
                            statPrint()
                            print('\n\nElmegyek a kistanulótól máshova tanulni.')
                            input('ENTER...')

                            os.system('cls')
                            statPrint()
                            m = '0'
                voltSzoba = False
    input('\nENTER...')
    return voltSzoba                    


def tanul():
    tudasPlusz(30)
    print('Megtanulod a mai anyag egy részét, holnap jobban fognak menni a dolgozatok.')
    etel(20)
    idoMeres(1, 0)


def kezmosas():
    
    j = '0'
    while j != '1' and j != '2':
        os.system('cls')
        statPrint()
        print('\n1.. Kezet mosok')
        print('2.. Nem mosok kezet')
        j = input('\nMit tegyek:')
        match j:
            case '1':
                os.system('cls')
                idoMeres(0, 3)
                statPrint()
                print('\nKezet mostam, és kimentem a WC-ből')
                input('\nENTER...')
                # WC()
            case '2':
                os.system('cls')
                statPrint()
                print('\nNem mostam kezet, ezért koszos maradt.')
                input('\nENTER...')
                # WC()
        

def WC():
    x = random.randint(1, 4)
    problema = ""
    valasz = ""
    global m
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
    helySzin('WC')
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
                                idoMeres(0, 5)
                                kezmosas()
                            case 'Nem':
                                WC()
                
                case '2':
                        os.system('cls')
                        statPrint()
                        print('\nKözépen buzis pisilni...')
                        input('\nENTER...')
                        WC()

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
                                idoMeres(0, 5)
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
                                idoMeres(0, 15)
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
                                idoMeres(0, 15)
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
                                idoMeres(0, 15)
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
                                idoMeres(0, 15)
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
                if m == '1' or m == '2' or m == '3':
                    idoMeres(0, 5)
                else:
                    idoMeres(0, 15)
                kezmosas()

        
def dogaEredmeny():
    tudas = gettudas()
    if tudas >= 100:
        jegy = 5
    elif tudas >= 80 and tudas < 100:
        jegy = random.randint(4,5)
    elif tudas >= 40 and tudas < 80:
        jegy = random.randint(2,4)
    elif tudas < 40:
        jegy = random.randint(1,3)
    return jegy


def szoba():
    os.system('cls')
    helySzin('Szoba')
    statPrint()
    global toltott
    global voltmar
    global elso
    global keddentoltott
    global javitas
    m = '0'
    while m != '6' :
        if getora() < 22:
            ehseg = getehseg()
            nap = getnap()
            os.system("cls")
            statPrint()
            print("\n1...Eszek")
            print("\n2...Telefonozok")
            print("\n3...Tanulok")
            if nap != 'csutortok':
                print("\n4...Játszok")
            else:
                print("\n4...Gépszerelés")
            print("\n5...Beszélgetek")
            print("\n6...Kimegyek")

            m = input("\nMit csinálok? ")
            match m:
                case '1':
                    if ehseg > 15:
                        os.system("cls")
                        if ehseg >= 15:
                            etel(-15)
                        else:
                            etel(-ehseg)
                        idoMeres(0, 20)
                        statPrint()
                        print("\nEttél valamennyit és így már kevésbé vagy éhes")
                        input("Enter")
                        voltSzoba = True
                        
                    elif ehseg <= 15 and ehseg > 0:
                        os.system("cls")
                        etel(-ehseg)
                        idoMeres(0, 20)
                        statPrint()
                        print("\nEttél valamennyit és már egyáltalán nem vagy éhes")
                        input("Enter")
                        voltSzoba = True

                    elif ehseg == 0:
                        os.system("cls")
                        statPrint()
                        print("\nTele vagy, nem tudsz ennni egy falatot se")
                        input("Enter")
                        voltSzoba = True
                case '2':
                    os.system("cls")
                    etel(5)
                    idoMeres(0, 45)     
                    statPrint()
                    telefon()
                    voltSzoba = True      
                case '3':   
                    os.system("cls")
                    statPrint()
                    print('')
                    tanul()
                    tudasPlusz(-10)
                    idoMeres(-1, 45)  
                    input("Enter...")
                    voltSzoba = True
                case '4':
                    match nap:
                        case 'vasarnap':
                            os.system('cls')
                            statPrint()
                            if toltott == False:  
                                    if voltmar == True:  
                                        print("\nSajnos mikor elindítottad a laptopot észre vetted hogy le van merülve")
                                        voltmar = False
                                    else:
                                        print("\nMég mindig le van merülve")
                                    print("\n1...Feldugom töltőre")
                                    print("\n2...Hagyom")
                                    n = input("\nHogy döntesz?")
                                    match n:
                                        case '1':
                                            os.system('cls')
                                            idoMeres(0, 5)
                                            statPrint()
                                            print('\nA laptopot felraktad töltőre')
                                            toltott = True
                                            input('\nEnter folytatáshoz...')
                                        case '2':
                                            os.system('cls')
                                            statPrint()
                                            print("\nMivel nem vagy hajlandó feltölteni, így nem játszol")
                                            input('\nEnter folytatáshoz...')                                
                            else:
                                print('\nA laptop töltődik')
                                input('\nEnter folytatáshoz...')
                        case 'hetfo':
                            os.system('cls')
                            statPrint()
                            voltmar = True
                            if toltott == False:  
                                if voltmar == True:  
                                    print("\nSajnos tegnap nem töltötted fel a laptopot ezért le van merülve")
                                    voltmar = False
                                else:
                                    print("\nMég mindig le van merülve")
                                print("\n1...Feldugom töltőre")
                                print("\n2...Hagyom")
                                n = input("\nHogy döntesz?")
                                match n:
                                    case '1':
                                        os.system('cls')
                                        idoMeres(0, 5)
                                        statPrint()
                                        print('\nA laptopot felraktad töltőre')
                                        toltott = True
                                        input('\nEnter folytatáshoz...')
                                    case '2':
                                        os.system('cls')
                                        statPrint()
                                        print("\nMivel nem vagy hajlandó feltölteni, így nem játszol")
                                        input('\nEnter folytatáshoz...')                                
                            else:
                                if elso == True:
                                    print('\nA laptop fel van töltve, de sajnos az elit kollégiumban most pont nincs net')
                                    print("\n1...Játszom a Google-es dínóval")
                                    print("\n2...Candy crush")
                                    n = input("\nHogy döntesz?")
                                    match n:
                                        case '1':
                                            os.system('cls')
                                            idoMeres(1, 0)
                                            etel(20)
                                            statPrint()
                                            print("\nEgy órán keresztül szórákoztál ezzel az idegfeszítő játékkal, de sikeresen lemerítetted a gépet és sajnos az összes konnektor foglalt")
                                            input('\nEnter folytatáshoz...')
                                        case '2':
                                            os.system('cls')
                                            idoMeres(1, 0)
                                            etel(20)
                                            tudasPlusz(-10)
                                            statPrint()
                                            print("\nEgy órán keresztül cukroztál, de sikeresen lemerítetted a gépet és sajnos az összes konnektor foglalt")
                                            input('\nEnter folytatáshoz...')
                                    elso = False
                                else:
                                    os.system('cls')
                                    statPrint()
                                    print("\nLe vagy merülve, és csak holnap tudsz tölteni")
                                    input('\nEnter folytatáshoz...')
                        case 'kedd':
                            os.system('cls')
                            statPrint()
                            if keddentoltott == False:  
                                print("\nA laptop le van merülve")
                                print("\n1...Feldugom töltőre")
                                print("\n2...Hagyom")
                                n = input("\nHogy döntesz?")
                                match n:
                                    case '1':
                                        os.system('cls')
                                        idoMeres(0, 5)
                                        statPrint()
                                        print('\nA laptopot felraktad töltőre')
                                        keddentoltott = True
                                        input('\nEnter folytatáshoz...')
                                    case '2':
                                        os.system('cls')
                                        statPrint()
                                        print("\nMivel nem vagy hajlandó feltölteni, így nem játszol")
                                        input('\nEnter folytatáshoz...')                                
                            else:
                                print('\nA laptop töltődik')
                                input('\nEnter folytatáshoz...')
                        case 'szerda':
                            os.system('cls')
                            statPrint()
                            print("\nA mai napon leültél játszani, de a gép sajnos nem indult akárhogy nyomkodtad, úgy néz ki elvan romolva")
                            input("\nEnter a folytatáshoz")
                        case 'csutortok':
                            os.system('cls')
                            statPrint()
                            x = random.randint(1,2)
                            if javitas == False:
                                print("\nZoli szobatársa, András, felajánlotta hogy 1000Ft-ért megszereli laptopod")
                                print("\n1...Elfogadom")
                                print("\n2...Inkább hagyom")
                                n = input("\nHogy választasz?")
                                match n:
                                    case '1': 
                                        match x:
                                            case 1:
                                                os.system('cls')
                                                penz(-1000)
                                                idoMeres(0, 30)
                                                etel(10)
                                                statPrint()
                                                print("\nAndrás sikeresen megjavította a géped és fizetned kellett 1000 Ft-ot nagylelkűsége miatt")
                                                input("\nEnter a folytatáshoz")
                                                javitas = True
                                            case 2:
                                                os.system('cls')
                                                penz(1000)
                                                idoMeres(0, 15)
                                                etel(5)
                                                statPrint()
                                                print("\nAndrás nem volt valami ügyes és most mégrosszabb, kárpótlásul ő adott egy ezrest")
                                                input("\nEnter a folytatáshoz")
                                                javitas = True
                            else:
                                if x == 1 and javitas == True:
                                    os.system('cls')
                                    statPrint()
                                    print("\nA laptop megvan javulva")
                                    input("\nEnter a folytatáshoz")
                                if x == 2 and javitas == True:
                                    os.system('cls')
                                    statPrint()
                                    print("\nA laptop el van romolva")
                                    input("\nEnter a folytatáshoz")
                    voltSzoba = True
                case '5':
                    match nap:
                        case 'vasarnap':
                            os.system("cls")
                            statPrint()
                            print("\nÚgy döntöttél, hogy leülsz szobatársaiddal beszélni. Három lakótársad Barni, Olivár és Peti.")
                            print("\n1...Barni")
                            print("\n2...Olivér")
                            print("\n3...Peti")
                            n = input("\nKit választasz?")
                            match n:
                                case '1':
                                    os.system("cls")
                                    statPrint()
                                    print("\nBarni sajnos játszik így nem nagyon tud rád koncentrálni")
                                    input("\nENTER folytatáshoz...")
                                case '2':
                                    os.system('cls')
                                    idoMeres(0, 30)
                                    etel(10)
                                    statPrint()
                                    x = random.randint(1,3)
                                    if x == 1:
                                        mese = "Radics Peti idézete"
                                    elif x == 2:
                                        mese = "iskolai története"
                                    else:
                                        mese = "otthon történt eseménye"
                                    print(f"\nOlivér {mese} nagyon megnevettetett")
                                    input("\nENTER folytatáshoz...")
                                case '3':
                                    os.system("cls")
                                    idoMeres(0, 30)
                                    etel(10)
                                    tudasPlusz(1)
                                    statPrint()
                                    print("\nPeti egy békés ember és erősen hisz mindenkinek az egyenjogúságában. Érdekes történeteiből és mély metaforáiból sokat tanulsz")
                                    input("\nENTER folytatáshoz...")
                        case 'hetfo':
                            os.system("cls")
                            statPrint()
                            print()
                            print("\n1...Barni")
                            print("\n2...Olivér")
                            print("\n3...Peti")
                            n = input("\nKit választasz?")
                            match n:
                                case '1':
                                    os.system('cls')
                                    statPrint()
                                    x = random.randint(1,3)
                                    if x == 1:
                                        mese = "Barni sajnos WC-n van, így pont nem tudsz beszélni vele"
                                    if x == 2:
                                        mese = "Barni Gergőék szobájában animét néz."
                                    else:
                                        mese = "Barni Zoliék szobájában animét néz."
                                    print(f"\n{mese}")
                                    input("\nENTER folytatáshoz...")
                                case '2':
                                    os.system('cls')
                                    idoMeres(0, 30)
                                    etel(10)
                                    tudasPlusz(1)
                                    statPrint()
                                    print("\nOlivérnek nagy szenvedélye az airsoft, így rengeteg újat mesél neked a játékról")
                                    input("\nENTER folytatáshoz...")
                                case '3':
                                    os.system('cls')
                                    statPrint()
                                    print("\nPeti jó szokásához híven ma is elment edzeni, így nem tudsz vele beszélni")
                                    input("\nENTER folytatáshoz...")
                        case 'kedd':
                            os.system("cls")
                            statPrint()
                            print()
                            print("\n1...Barni")
                            print("\n2...Olivér")
                            print("\n3...Peti")
                            n = input("\nKit választasz?")
                            match n:
                                case '1':
                                    os.system("cls")
                                    statPrint()
                                    print("\nBarni segítséget kér projektjében")
                                    print("\n1...Segítesz")
                                    print("\n2...Hagyod")
                                    j = input("\nHogy döntessz? ")
                                    match j:
                                        case '1':
                                            os.system('cls')
                                            idoMeres(1, 30)
                                            if ehseg >= 10:
                                                etel(-10)
                                            else:
                                                etel(-ehseg)
                                            statPrint()
                                            print("\n1.5 óra kemény munka után befejeztétek és Barni nagy segítséged házi készítésű hókiflijével jutalmazta")
                                            input("\nENTER folytatáshoz...")
                                        case '2':
                                            os.system("cls")
                                            statPrint()
                                            print("Csalódottan, de megértően elfogadja hogy nem segítesz")
                                            input("\nENTER folytatáshoz...")
                                case '2':
                                    os.system("cls")
                                    statPrint()
                                    x = random.randint(1,2)
                                    if x == 1:
                                        print(f"\nOlivér ma három egyest is szerzett, emiatt mikor beszéltél vele felhúztad és megvert, de nagyobb bajod nem lett")
                                        idoMeres(0, 20)
                                        etel(15)
                                        input("\nENTER folytatáshoz...")
                        
                                    else:
                                        print(f"\nOlivér ma három egyest is szerzett, és bár beszélgetés közbe felhúztad, végül nem vert meg")
                                        idoMeres(0, 30)
                                        etel(10)
                                        input("\nENTER folytatáshoz...")

                                case '3':
                                    os.system("cls")
                                    statPrint()
                                    print("\nPeti jó szokásához híven ma is elment edzeni, így nem tudsz vele beszélni")
                                    input("\nENTER folytatáshoz...")
                        case 'szerda':
                            os.system("cls")
                            statPrint()
                            print()
                            print("\n1...Barni")
                            print("\n2...Olivér")
                            print("\n3...Peti")
                            n = input("\nKit választasz?")
                            match n:
                                case '1':
                                    os.system('cls')
                                    statPrint()
                                    print("\nBarninak gondjai akadtak a matekkal és segítséged kéri")
                                    print("\n1...Segítesz")
                                    print("\n2...Hagyod")
                                    j = input("\nHogy döntessz? ")
                                    match j:
                                        case '1':
                                            os.system('cls')
                                            idoMeres(1, 30)
                                            tudasPlusz(10)
                                            etel(15)
                                            statPrint()
                                            print("\n1.5 óra kemény munka után jobban érti az anyagot, de a gyakorlás neked is jót tett")
                                            input("\nENTER folytatáshoz...")
                                        case '2':
                                            os.system("cls")
                                            statPrint()
                                            print("Csalódottan, de megértően elfogadja hogy nem segítesz")
                                            input("\nENTER folytatáshoz...")    
                                case '2':
                                    os.system('cls')
                                    idoMeres(0, 45)
                                    statPrint()
                                    print("\nFelhozza kedvenc metál együttesét és mivel mindketten hatalmas fanok, így jó hosszan beszélgettek a metál zenéről")
                                    input("\nENTER a folytatáshoz")
                                case '3':
                                    os.system('cls')
                                    idoMeres(0, 30)
                                    if ehseg >= 10:
                                        etel(-10)
                                    else:
                                        etel(-ehseg)
                                    statPrint()
                                    print("\nPetivel elbeszélgettek egymás barátnőiről és beszélgetés közben kedvesen megkínál sütijéből")
                                    input("\nENTER a folytatáshoz")
                        case 'csutortok':
                            os.system("cls")
                            statPrint()
                            print()
                            print("\n1...Barni")
                            print("\n2...Olivér")
                            print("\n3...Peti")
                            n = input("\nKit választasz?")
                            match n:
                                case '1':
                                    os.system('cls')
                                    statPrint()
                                    print('\nBarni és Olivér elment az Árkádba így sajnos nem tudsz beszélni velük')
                                    input("\nENTER a folytatáshoz")
                                case '2':
                                    os.system('cls')
                                    statPrint()
                                    print('\nBarni és Olivér elment az Árkádba így sajnos nem tudsz beszélni velük')
                                    input("\nENTER a folytatáshoz")
                                case '3':
                                    os.system('cls')
                                    statPrint()
                                    print("\nPeti jó szokásához híven ma is elment edzeni, így nem tudsz vele beszélni")
                                    input("\nENTER folytatáshoz...")
                    voltSzoba = True
                case '6':
                    return 0
        else:
            break


def telefon():
    global voltPenz
    m = '0'
    while m != '1' and m != '2' and m != '3' and m != '4':
        os.system('cls')
        statPrint()
        print('\n1.. Hívás')
        print('2.. Instagram')
        print('3.. Tiktok')
        print('4.. Kilépés')
        m = input('\nMit válasszak: ')

        match m:
            case '1':
                n = '0'
                while n != '1' and n != '2':
                    os.system('cls')
                    statPrint()
                    print('\nNévjegyek:')
                    print('\n1.. Anya')
                    print('2.. Apa')
                    print('3.. Kilépek')
                    n = input('\nMit választasz: ')

                    match n:
                        case '1':
                            os.system('cls')
                            statPrint()
                            print('\nBeszélgettél anyukáddal, örültél neki.')
                            idoMeres(0, 5)
                            input('ENTER...')
                            telefon()
                        case '2':
                            if voltPenz == False:
                                os.system('cls')
                                statPrint()
                                print('\nBeszélgettél apukáddal és küldött 1500 Ft-ot.')
                                penz(+1500)
                                idoMeres(0, 5)
                                voltPenz = True
                                input('ENTER...')
                                telefon()
                            elif voltPenz == True:
                                os.system('cls')
                                statPrint()
                                print('\nBeszélgettél apukáddal, örültél neki.')
                                idoMeres(0, 5)
                                input('ENTER...')
                                telefon()
                        case '3':
                            telefon()
            case '2':
                n = '0'
                while n != '1' and n != '2':
                    os.system('cls')
                    statPrint()
                    print('\n1.. Megnézem Corinna Kopf bejegyzéseit.')
                    print('\n2.. Megnézem a mai bejegyzéseket.')
                    print('\n3.. Kilépek')
                    n = input('\nMit választasz: ')

                    match n:
                        case '1':
                            os.system('cls')
                            statPrint()
                            print('\nMivel megnézted Corinna Kopf bejegyzéseit, így nem bírtad ki, hogy ne huzogasd a bőrtokos calippod. Sajnos ezzel elment egy kis idő.')
                            idoMeres(0, 20)
                            input('ENTER...')
                            telefon()
                        case '2':
                            os.system('cls')
                            statPrint()
                            print('\nMegnézted a mai bejegyzéseket, semmi különös nem volt.')
                            idoMeres(0, 10)
                            input('ENTER...')
                            telefon()
                        case '3':
                            telefon()
            case '3':
                n = '0'
                while n != '1' and n != '2':
                    os.system('cls')
                    statPrint()
                    print('\nIlona néni éppen liveol és a halott férjéről beszél.')
                    print('\n1.. Küldesz neki rózsát.')
                    print('2.. Beszólsz neki.')
                    print('3.. Kilépsz')
                    n = input('\nMit választasz: ')
                    
                    match n:
                        case '1':
                            os.system('cls')
                            statPrint()
                            print('\nKüldtél neki rózsát, és mondta "Hmm... Rózsa illatos!". Nem értetted miért mondja ezt.')
                            penz(-300)
                            idoMeres(0, 5)
                            input('ENTER...')
                            telefon()
                        case '2':
                            os.system('cls')
                            statPrint()
                            print('\nBeszóltál neki, de nem vette észre.')
                            idoMeres(0, 5)
                            input('ENTER...')
                            telefon()
                        case '3':
                            telefon()
            case '4':
                szoba()


def alvas():
    print("\nElmúlt 22:00 óra így kényszerülsz aludni, a következő statokkal zártad a mai napot:\n")
    idoMeres(0, -getperc())
    statPrint()


def varos():
    penzem = getpenz()
    if penzem > 0:
        ehseg = getehseg()
        os.system('cls')
        statPrint()
        print("\nÚgy döntöttél a városba mész és egész magas éhség szinted miatt elmennél kajálni")
        print("\n1...Gyorskajálda")
        print("\n2...Bolt")
        m = input("\nHogy választasz? ")
        match m:
            case '1':
                    os.system('cls')
                    statPrint()
                    print("\nElmész gyorskajáldába, de ez Győr, rengeteg a választék, de a jelenleg csak ez a 3 étterem éri meg neked")
                    print('\n1...McDonalds')
                    print('2...KFC')
                    print('3...Burger King')
                    j = input("\nHogy választasz? ")
                    x = random. randint(1,3)
                    if x == 1:
                        problema = 'kedvenc menüdet pont nem árulják, így kényszerülsz valami drágábbat venni, cserébe teljesen jól laksz és visszagyalogolsz a koliba'
                    elif x == 2:
                        problema = 'nem volt hely, így kényszerülsz a kollégiumban megenni'
                    else:
                        problema = 'egy kellemes ebéd után visszatérsz a kollégiumba'
                    match j:
                        case '1':
                            os.system('cls')
                            helySzin('McDonalds')
                            statPrint()                            
                            print('\nA McDonaldsban', problema)
                            if x == 1:
                                idoMeres(1, 30)
                                etel(-ehseg)
                                penz(-2500)
                            elif x == 2:
                                idoMeres(1, 0)
                                if ehseg > 20:
                                    etel(-20)
                                else:
                                    etel(-ehseg)
                                penz(-2000)
                            else: 
                                idoMeres(1, 30)
                                if ehseg > 20:
                                    etel(-20)
                                else:
                                    etel(-ehseg)
                                penz(-2000)
                            input('\nENTER a folytatáshoz...')
                        case '2':
                            os.system('cls')
                            helySzin('KFC')
                            statPrint()                            
                            print('\nA KFC-ben', problema)
                            if x == 1:
                                idoMeres(1, 30)
                                etel(-ehseg)
                                penz(-3000)
                            elif x == 2:
                                idoMeres(1, 0)
                                if ehseg > 25:
                                    etel(-25)
                                else:
                                    etel(-ehseg)
                                penz(-2100)
                            else: 
                                idoMeres(1, 30)
                                if ehseg > 25:
                                    etel(-25)
                                else:
                                    etel(-ehseg)
                                penz(-1000)
                            input('\nENTER a folytatáshoz...')
                        case '3':
                            os.system('cls')
                            helySzin('Burger King')
                            statPrint()                            
                            print('\nA Burger Kingben', problema)
                            if x == 1:
                                idoMeres(2, 0)
                                etel(-ehseg)
                                penz(-2700)
                            elif x == 2:
                                idoMeres(1, 30)
                                if ehseg > 20:
                                    etel(-20)
                                else:
                                    etel(-ehseg)
                                penz(-2200)
                            else: 
                                idoMeres(2, 0)
                                if ehseg > 20:
                                    etel(-20)
                                else:
                                    etel(-ehseg)
                                penz(-2200)
                            input('\nENTER a folytatáshoz...')
            case '2':
                    os.system('cls')
                    statPrint()
                    print("\nAz olcsóbb megoldás a boltok, 3 kedvenc és legközelebbi bolt közül kell választanod")
                    print('\n1...Wellmark')
                    print('2...Reál')
                    print('3...Leo pékség')
                    j = input("\nHogy választasz? ")       
                    match j:
                        case '1':
                            os.system('cls')
                            helySzin('Wellmark')
                            statPrint()
                            print('\nEbben a boltban megtudod veni kedvenc instant levesed, miután ezt megtetted, visszamentél a kollégiumba és elkészítése után meg is etted')
                            if ehseg > 10:
                                etel(-10)
                            else:
                                etel(-ehseg)
                            idoMeres(1, 0)
                            penz(-600)                            
                            input('\nENTER a folytatáshoz...')
                        case '2':
                            os.system('cls')
                            helySzin('Reál')
                            statPrint()                            
                            print('\nEbben a boltban megtudod veni a legfinomabb előre elkészített szenvicset, miután ezt megvetted, visszamentél a kollégiumba és megetted')
                            if ehseg > 15:
                                etel(-15)
                            else:
                                etel(-ehseg)
                            idoMeres(0, 45)
                            penz(-1200)                            
                            input('\nENTER a folytatáshoz...')                                                        
                        case '3':
                            os.system('cls')
                            statPrint()
                            helySzin('Leo pékség')
                            statPrint()                            
                            print("\nMit kívánnál?")
                            print("\n1...Kakaós csiga")            
                            print("2...Pizza szelet")            
                            print("3...Sajtosrúd")
                            n = input("\nHogy választasz? ") 
                            match n:
                                case '1':
                                    if ehseg > 10:
                                        etel(-10)
                                    else:
                                        etel(-ehseg)
                                    penz(-500)
                                    kaja = 'kakaós csigát'
                                case '2':
                                    if ehseg > 15:
                                        etel(-15)
                                    else:
                                        etel(-ehseg)
                                    penz(-650)
                                    kaja = 'pizza szeletet'                                                          
                                case '3':   
                                    if ehseg > 5:
                                        etel(-5)
                                    else:
                                        etel(-ehseg)
                                    penz(-300)  
                                    kaja = 'sajtosrudat' 
                            idoMeres(0, 45)
                            os.system('cls')
                            print(f"\nMiután megvetted a {kaja} visszamentél a koliba és megetted")
                            input('\nENTER a folytatáshoz...')                                                        



    else:
        print("\nNincs pénzed, nem tudsz venno semmit magadnak")
        input("\nENTER folytatáshoz...")


def vacsora(vacsiMar):
    m = '0'
    ehseg = getehseg()
    ido = getora()
    if ido < 19 and ido >= 18:
        x = random.randint(1,2)
        if x == 1:
            while m != '1' and m!= '2':
                os.system('cls')
                statPrint()
                print("\nLementél vacsorázni, de nem annyira szereted amit adnak.")
                print("\n1...Mégis megeszem")
                print("\n2...Hagyom")
                m = input('\nMit csinálsz?')
                match m:
                    case '1':
                        idoMeres(0, 30)
                        etel(-ehseg)
        if x == 2:
            idoMeres(0, 30)
            etel(-ehseg)
            while m != '1' and m!= '2':
                os.system('cls')
                statPrint()
                print("\nVacsora közben összepiszkoltad a kezed.")
                print("\n1...Megmosom")
                print("\n2...Hagyom")
                m = input('\nMit csinálsz?')
                match m:
                    case '1':
                        idoMeres(0, 3)
        vacsiMar = True
        return vacsiMar 
    elif ido < 18:
        print('')
        vacsiMar = False
        return vacsiMar 
    

def sport():
    m = '0'
    while m != '1' and m != '2' and m != '3':
        os.system('cls')
        statPrint()
        print('\nLehetőségek kollégiumban a sportolásra:')
        print('\n1...Pingpong')
        print('\n2...Darts')
        print('\n3...Sakk')
        print('\n4...Csocsóasztal')
        m = input('\nMivel játszol? ')
        x = random. randint(1,5)
        if x == 1:
            ember = 'Barnival'
        elif x == 2:
            ember = 'Ferenccel'
        elif x == 3:
            ember = 'Áronnal'
        elif x == 4:
            ember == 'Olivérrel'
        else:
            ember == 'Attilával'

        y = random.randint(1,2)
        if y == 1:
            nyeres = 'sajnos veszítettél ellene'
        else:
            nyeres = 'nyertél ellene'
        
        match m:
            case '1':
                os.system('cls')
                helySzin('Alaksor')
                statPrint()
                print(f'\nLementél pingpongozni egyet {ember} és egy jó hosszú játszma után {nyeres}')
                idoMeres(1, 0)
                etel(20)
                input("\nENTER folytatáshoz...")

            case '2':
                os.system('cls')
                helySzin('Tanulószoba')
                statPrint()
                print(f'\nFelmentél a tanulószobába dartsozni  {ember} és egy jó hosszú játszma után {nyeres}')
                idoMeres(0, 45)
                etel(15)
                input("\nENTER folytatáshoz...")

            case '3':
                os.system('cls')
                helySzin('Foglalkoztató')
                statPrint()
                print(f'\nFelmentél a foglalkoztatóba sakkozni egyet {ember} és egy jó hosszú játszma után {nyeres}')
                idoMeres(1, 15)
                etel(25)
                input("\nENTER folytatáshoz...")

            case '4':
                os.system('cls')
                helySzin('Foglalkoztató')
                statPrint()
                print(f'\nLementél a foglalkoztatóba csocsózni {ember} és egy jó hosszú játszma után {nyeres}')
                idoMeres(0, 30)
                etel(10)
                input("\nENTER folytatáshoz...")


def tanari():
    global kiulo
    os.system('cls')
    helySzin('Tanári')
    statPrint()
    m = '0'
    while m != '1' and m != '2' and m != '3':
        print('\nJelenleg csak 3 nevelő van bennt')
        print('\n1...Székely Szabolcs')
        print('\n2...Fehér Szilárd')
        print('\n3...Módly Zoltán')
        m = input('\nKivel beszélsz? ')
        match m:
            case '1':
                os.system('cls')
                idoMeres(0, 30)
                etel(5)
                statPrint()
                print('\nSzékely tanár úrral sokat beszélgettetek, majd emlékeztett hogy jövő héten színházba mész a csoportoddal.')
                input("\nENTER folytatáshoz...")

            case '2':
                os.system('cls')
                statPrint()
                if kiulo == False:
                    n = ''
                    while n != "Igen" and n != 'Nem':
                        print('\nFehér tanár úr segítségeded kéri az új kiülő rendrakásában')
                        n= input('\nSegítesz (Igen/Nem): ')
                        match n:
                            case 'Igen':
                                os.system("cls")
                                helySzin('Udvar')
                                idoMeres(0, 45)
                                etel(20)
                                statPrint()
                                kiulo = True
                                print('\nA hosszú és fárasztó munka után végre rendben van a kiülő')
                                input("\nENTER folytatáshoz...")
                            case 'Nem':
                                os.system("cls")
                                statPrint()
                                print("\nFehér tanár úr megérti hogy más dolgod van és inkább megkérdez mást")
                                input("\nENTER folytatáshoz...")

                else:
                    os.system('cls')
                    idoMeres(0, 25)
                    etel(5)
                    statPrint()
                    print('\nFehér tanár úrral sokat beszélgettetek.')
                    input("\nENTER folytatáshoz...")



            case '3':
                os.system('cls')
                idoMeres(0, 45)
                etel(10)
                statPrint()
                print('\nMódly tanár úrral jól el lehet beszélgetni, ez most se volt másképp, sokat beszéltetek történelemről és a kollégiumban történt eseményekről')
                input("\nENTER folytatáshoz...")


def csocsoBajnoksag(csocso):
    helySzin("Foglalkoztató")
    m = '0'
    while m != '1' and m != '2' and m != '3':
        os.system('cls')
        statPrint()
        print('\nEljött az idei Csocsóbajnokság ami 5 körből áll, de először válassz csapattársad.')
        print('\n1...Barni')
        print('\n2...Máté')
        print('\n3...Gergő')
        m = input('\nKit választasz?' )
        gyoz = 0
        vesz = 0
        for i in range(1,6):
            if m == '1':
                os.system('cls')
                idoMeres(0, 10)
                etel(2)
                gyoz += 1
                statPrint()
                print(f'\n{i}. kör')
                print("\nGyőzelem")
                print(f"\nGyőzelmek száma: {gyoz}")
                print(f"\nVereségek száma: 0")
                input('\nFolytatáshoz ENTER ')
            elif m == '2' or m == '3':
                os.system('cls')
                idoMeres(0, 10)
                etel(3)
                x = random.randint(1,2)
                statPrint()
                print(f'\n{i}. kör')
                if x == 1:
                    gyoz += 1
                    print("\nGyőzelem")
                else:
                    vesz += 1
                    print("\nVeszteség")
                print(f"\nGyőzelmek száma: {gyoz}")
                print(f"\nVereségek száma: {vesz}")
                input('\nFolytatáshoz ENTER ')
        if gyoz >= 3:
            os.system('cls')    
            statPrint()
            print('\nA tavalyi után az idei bajnokságot is sikeresen megnyerted')
            input('\nFolytatáshoz ENTER ')
            csocso = True
        else:
            os.system('cls')    
            statPrint()
            print('\nA tavalyi sikerek után sajnos nem tudtad fenntartani bajnoki címed')
            input('\nFolytatáshoz ENTER ')  
            csocso = False 
    return csocso


def buliszervezes():
    global italAr
    global szenyoAr
    global dj
    global Szerep
    helySzin('Gergő szobája')
    m = 0
    ital = False
    szenyo = False
    DJ = False
    szerep = False
    while m != 1:
        os.system('cls')
        statPrint()
        print("\nGergő segítségeded kéri a közelgő avatóbuli megszervezésében. Meg kell választani a büfében lévő dolgok árát, a DJ-t és hogy milyen szerepet vállalsz")
        if ital == False:
            print('\n1...Ital ára')
        else:
            print('\n1...Ital ára (kész)')
        
        if szenyo == False:
            print('\n2...Melegszendvics ára')
        else:
            print('\n2...Melegszendvics ára (kész)')
        
        if DJ == False:
            print('\n3...DJ választás')
        else:
            print('\n3...DJ választás (kész)')
        
        if szerep == False:
            print('\n4...Szerep')
        else:
            print('\n4...Szerep (kész)')

        m = input("\nVálasztásod: ")
        match m:
            case '1':
                if ital == False:
                    n = 0
                    while n != 1:
                        os.system('cls')
                        statPrint()
                        print("\nGergő az 2 dl ital árát 50 és 150 Ft közé tenné.")
                        n = input("\nMennyi legyen az ára(Ft):")
                        italAr = n
                        ital = True
                        if n != '':
                            break
                            
                else:
                    os.system('cls')
                    statPrint()
                    print(f'\nItal ára(Ft): {italAr}')
                    input("\nENTER folytatáshoz: ")
            case '2':
                if szenyo == False:
                    n = 0
                    while n != 1:
                        os.system('cls')
                        statPrint()
                        print("\nGergő a melegszendvics árát 200 és 400 Ft közé tenné.")
                        n = input("\nMennyi legyen az ára(Ft):")
                        szenyoAr = n
                        szenyo = True
                        if n != '':
                            break
                else:
                    os.system('cls')
                    statPrint()
                    print(f'\nMelegszendvics ára(Ft): {szenyoAr}')
                    input("\nENTER folytatáshoz: ")
            case '3':
                if DJ == False:
                    n = '0'
                    while n != '1' and n != '2':
                        os.system("cls")
                        statPrint()
                        print('\nGergő a következő kettő embert találta önkéntesen dj-nek, melyiket választod?')
                        print('\n1...Máté')
                        print('\n2...Beni')
                        n = input("\nKi legyen? ")
                        match n:
                            case '1':
                                DJ = True
                                dj = 'Máté'
                            case '2':
                                DJ = True
                                dj = 'Beni'
                else:
                    os.system('cls')
                    statPrint()
                    print(f'\nA DJ: {dj}')
                    input("\nENTER folytatáshoz: ")
            case '4':
                if szerep == False:
                    n = '0'
                    while n != '1' and n != '2' and n != '3':
                        os.system("cls")
                        statPrint()
                        print('\nGergő a következő szerepeket ajánlja fel, melyiket választod?')
                        print('\n1...Ajtónálló')
                        print('\n2...Büfés')
                        print('\n3...Felügyelés')
                        n = input("\nKi legyen? ")
                        match n:
                            case '1':
                                szerep = True
                                Szerep = 'Ajtónállás'
                            case '2':
                                szerep = True
                                Szerep = 'Büfés'
                            case '3':
                                szerep = True
                                Szerep = 'Felügyelés'
                else:
                    os.system('cls')
                    statPrint()
                    print(f'\nA szereped: {Szerep}')
                    input("\nENTER folytatáshoz: ")
        if ital == True and szenyo == True and DJ == True and szerep == True:
            break


def bulistatok():
    os.system('cls')
    statPrint()
    global italAr
    global szenyoAr
    global dj
    global Szerep
    print(f'\nItal ára(Ft): {italAr}')
    print(f'\nMelegszendvics ára(Ft): {szenyoAr}')       
    print(f'\nDJ: {dj}')
    print(f'\nSzereped: {Szerep}')
    input("\nENTER folytatáshoz: ")

