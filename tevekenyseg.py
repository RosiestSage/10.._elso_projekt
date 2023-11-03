import random, os
from statok import etel, getehseg, idoMeres, tudas, tudasPlusz, statPrint, getora, perc, getperc, getnap, ora, penz
furdottMar = False
voltSzoba = False
toltott = False
voltmar = True
elso = True
keddentoltott = False
javitas = False

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
                problema = "de koszos a szabad kabin"
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


def tanulas(voltSzoba):
    os.system('cls')
    statPrint()

    m = '0'
    while m != '1' and m != '2' and m != '3':
        print('\n\nHol tanuljak?')

        print('\n1.. Tanszoba')
        print('2.. Szoba')
        print('3.. Kistanuló')
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
            
            case '2':
                os.system('cls')
                statPrint()
                print('\n\nMaradok a szobában tanulni, de szobatársam zavar.')
                print('\n1.. Szólok, hogy hagyja abba')
                print('2.. Elmegyek máshova tanulni')
                n = '0'
                while n != '1' and n != '2' and n != '3':
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
                os.system('cls')
                statPrint()
                print('\n\nElmentem a kistanulóba, de az ajtó zárva.')
                print('\n1.. Elkérem a kulcsot')
                print('2.. Tanulok máshol')
                n = '0'
                while n != '1' and n != '2':
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
    print('Megtanultam a mai anyagot egy részét, holnap jobban fognak menni a dolgozatok.')
    etel(20)
    idoMeres(1, 0)


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
    
    
    m = 0
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
                                WC()
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
                                WC()
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
                                WC()
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
                                WC()
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
                                WC()
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
                                WC()
                            case 'Nem':
                                WC()
    
        elif x == 4:
            if m == '2':
                os.system('cls')
                statPrint()
                print('\nKözépen buzis pisilni...')
                input('\nENTER...')
                WC()
            else:
                os.system('cls')
                statPrint()
                print('\nElvégeztem a dolgomat.')
                input('\nENTER...')
                WC()

def dogaEredmeny():
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
    statPrint()
    global voltSzoba
    global toltott
    global voltmar
    global elso
    global keddentoltott
    global javitas
    ehseg = getehseg()
    nap = getnap()
    if voltSzoba == False:
        print('\nBementem a szobámba')
        print("\n1...Leülök a székre")
        print("\n2...Leülök az ágyra")
        m = input("\nHova mész? ")
        voltSzoba = True
    else:
        os.system("cls")
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
    m = input("\nMit csinálok? ")

    match m:
        case '1':
            if ehseg > 15:
                os.system("cls")
                print("Ettél valamennyit és így már kevésbé vagy éhes")
                input("Enter")
                etel(-15)
                idoMeres(0, 20)
            elif ehseg <= 15 and ehseg > 0:
                os.system("cls")
                print("Ettél valamennyit és már egyáltalán nem vagy éhes")
                input("Enter")
                etel(-ehseg)
                idoMeres(0, 20)
            elif ehseg == 0:
                os.system("cls")
                print("Tele vagy, nem tudsz ennni egy falatot se")
                input("Enter")
        case '2':
            os.system("cls")
            print("Elfeküdtél és jól körbenéztél a közösségi oldalokon")
            input("Enter") 
            etel(5)
            idoMeres(0, 45)           
        case '3':   
            os.system("cls")
            print("Mivel úgy döntöttél, hogy tanulsz, mégjobban készen állsz a holnapi napra")
            input("Enter")
            etel(20)
            idoMeres(0, 45)  
            tudasPlusz(20)
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
                                print('\nA laptopot felraktad töltőre')
                                idoMeres(0, 5)
                                toltott = True
                                input('\nEnter folytatáshoz...')
                            case '2':
                                os.system('cls')
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
                                print('\nA laptopot felraktad töltőre')
                                idoMeres(0, 5)
                                toltott = True
                                input('\nEnter folytatáshoz...')
                            case '2':
                                os.system('cls')
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
                                    print("\nEgy órán keresztül szórákoztál ezzel az idegfeszítő játékkal, de sikeresen lemerítetted a gépet és sajnos az összes konnektor foglalt")
                                    idoMeres(1, 0)
                                    etel(20)
                                    input('\nEnter folytatáshoz...')
                                case '2':
                                    os.system('cls')
                                    print("\nEgy órán keresztül cukroztál, de sikeresen lemerítetted a gépet és sajnos az összes konnektor foglalt")
                                    idoMeres(1, 0)
                                    etel(20)
                                    tudasPlusz(-10)
                                    input('\nEnter folytatáshoz...')
                            elso = False
                        else:
                            os.system('cls')
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
                                print('\nA laptopot felraktad töltőre')
                                idoMeres(0, 5)
                                keddentoltott = True
                                input('\nEnter folytatáshoz...')
                            case '2':
                                os.system('cls')
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
                                        print("\nAndrás sikeresen megjavította a géped és fizetned kellett 1000 Ft-ot nagylelkűsége miatt")
                                        penz(-1000)
                                        idoMeres(0, 30)
                                        etel(10)
                                        input("\nEnter a folytatáshoz")
                                        javitas = True
                                    case 2:
                                        os.system('cls')
                                        print("\nAndrás nem volt valami ügyes és most mégrosszabb, kárpótlásul ő adott egy ezrest")
                                        penz(1000)
                                        idoMeres(0, 15)
                                        etel(5)
                                        input("\nEnter a folytatáshoz")
                                        javitas = True
                    else:
                        if x == 1 and javitas == True:
                            os.system('cls')
                            print("\nA laptop megvan javulva")
                            input("\nEnter a folytatáshoz")
                        if x == 2 and javitas == True:
                            os.system('cls')
                            print("\nA laptop el van romolva")
                            input("\nEnter a folytatáshoz")
    
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
                            print("\nBarni sajnos játszik így nem nagyon tud rád koncentrálni")
                            input("\nENTER folytatáshoz...")
                        case '2':
                            os.system('cls')
                            x = random.randint(1,3)
                            if x == 1:
                                mese = "Radics Peti idézete"
                            if x == 2:
                                mese = "iskolai története"
                            else:
                                mese = "otthon történt eseménye"
                            print(f"\nOlivér {mese} nagyon megnevettetett")
                            idoMeres(0, 30)
                            etel(10)
                            input("\nENTER folytatáshoz...")
                        case '3':
                            os.system("cls")
                            print("\nPeti egy békés ember és erősen hisz mindenkinek az egyenjogúságában. Érdekes történeteiből és mély metaforáiból sokat tanulsz")
                            idoMeres(0, 30)
                            etel(10)
                            tudasPlusz(1)
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
                            print("\nOlivérnek nagy szenvedélye az airsoft, így rengeteg újat mesél neked a játékról")
                            idoMeres(0, 30)
                            etel(10)
                            tudasPlusz(1)
                            input("\nENTER folytatáshoz...")
                        case '3':
                            os.system('cls')
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
                            print("\nBarni segítséget kér projektjében")
                            print("\n1...Segítesz")
                            print("\n2...Hagyod")
                            j = input("\nHogy döntessz? ")
                            match j:
                                case '1':
                                    os.system('cls')
                                    print("\n1.5 óra kemény munka után befejeztétek és Barni nagy segítséged házi készítésű hókiflijével jutalmazta")
                                    idoMeres(1, 30)
                                    if ehseg >= 10:
                                        etel(-10)
                                    else:
                                        etel(-ehseg)
                                    input("\nENTER folytatáshoz...")
                                case '2':
                                    os.system("cls")
                                    print("Csalódottan, de megértően elfogadja hogy nem segítesz")
                                    input("\nENTER folytatáshoz...")
                        case '2':
                            os.system("cls")
                            x = random.randint(1,2)
                            if x == 1:
                                print(f"\nOlivér ma három egyest is szerzett, emiatt mikor beszéltél vele felhúztad és megvert, de nagyobb bajod nem lett")
                                idoMeres(20)
                                etel(15)
                                input("\nENTER folytatáshoz...")
                
                            else:
                                print(f"\nOlivér ma három egyest is szerzett, és bár beszélgetés közbe felhúztad, végül nem vert meg")
                                idoMeres(0, 30)
                                etel(10)
                                input("\nENTER folytatáshoz...")

                        case '3':
                            os.system("cls")
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
                            print("\nBarninak gondjai akadtak a matekkal és segítséged kéri")
                            print("\n1...Segítesz")
                            print("\n2...Hagyod")
                            j = input("\nHogy döntessz? ")
                            match j:
                                case '1':
                                    os.system('cls')
                                    print("\n1.5 óra kemény munka után jobban érti az anyagot, de a gyakorlás neked is jót tett")
                                    idoMeres(1, 30)
                                    tudasPlusz(10)
                                    etel(15)
                                    input("\nENTER folytatáshoz...")
                                case '2':
                                    os.system("cls")
                                    print("Csalódottan, de megértően elfogadja hogy nem segítesz")
                                    input("\nENTER folytatáshoz...")    
                        case '2':
                            os.system('cls')
                            print("\nFelhozza kedvenc metál együttesét és mivel mindketten hatalmas fanok, így jó hosszan beszélgettek a metál zenéről")
                            idoMeres(0, 45)
                            input("\nENTER a folytatáshoz")
                        case '3':
                            os.system('cls')
                            print("\nPetivel elbeszélgettek egymás barátnőiről és beszélgetés közben kedvesen megkínál sütijéből")
                            idoMeres(0, 30)
                            if ehseg >= 10:
                                etel(-10)
                            else:
                                etel(-ehseg)
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
                            print('\nBarni és Olivér elment az Árkádba így sajnos nem tudsz beszélni velük')
                            input("\nENTER a folytatáshoz")
                        case '2':
                            os.system('cls')
                            print('\nBarni és Olivér elment az Árkádba így sajnos nem tudsz beszélni velük')
                            input("\nENTER a folytatáshoz")
                        case '3':
                            os.system('cls')
                            print("\nPeti jó szokásához híven ma is elment edzeni, így nem tudsz vele beszélni")
                            input("\nENTER folytatáshoz...")
def alvas():
    print("\nElmúlt 22:00 óra így kényszerülsz aludni, a következő statokkal zártad a mai napot:\n")
    idoMeres(0, -getperc())
    statPrint()
    