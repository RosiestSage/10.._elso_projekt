import os
from statok import statPrint, getora, idoMeres, etel, tudasPlusz, getehseg, gettudas
from tevekenyseg import furdes, tanulas, szoba, voltSzoba, alvas, dogaEredmeny


def main():
    global voltSzoba
    print('Egy kollégista élete\n')
    print('Ön egy kollégista. Ebben a játékban figyelnie kell, hogy ne haljon éhen, és megtanuljon, hisz a héten minddennap ír valamiből. Lehetőleg pénzét se verje el. Megérkezett vasárnap a kollégiumba és sok lehetőség várja...')
    #Bevezető szöveg
    input('\nFolytatáshoz ENTER...')
    m = 0
    while m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
        while getora() < 22:
            os.system('cls')    
            print('\n\n', statPrint())
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
                    furdes()
                    voltSzoba = False
                case '2':
                    voltSzoba = tanulas(voltSzoba)
                case '3':
                    print('bemegyekValakihez')#func
                    voltSzoba = False
                case '4':
                    print('bemegyekWCre')#func
                    voltSzoba = False
                case '5':
                    szoba()
                    voltSzoba = True
        if getora() >= 22:
            os.system('cls')
            alvas()
            input('\nEnter a következő naphoz..')
            m = 0
        break


def hetfo():
    global voltSzoba
    os.system('cls')
    print(f'Hétfőn kipihenten állt neki a napnak, és megírt dolgozataira {dogaEredmeny()} és {dogaEredmeny()} érdemjegyet kapott. Eljött a délután és ön éppen az iskola előtt áll és gondolkodik hogy mit csináljon.')
    input('\nFolytatáshoz ENTER...')
    idoMeres(-8, 30)
    etel(-getehseg())
    etel(30)
    tudasPlusz(-gettudas())
    tudasPlusz(20)
    m = 0
    while m != 1 and m != 2 and m != 3 and m != 4 and m != 5:
        while getora() < 22:
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
        if getora() >= 22:
            os.system('cls')
            alvas()
            input('\nEnter a következő naphoz..')
            m = '0'
