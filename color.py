from colorama import Fore,Back
while True:
    ion=input('enter ion:')
    print(Fore.BLACK+'1.KI')
    print(Fore.BLACK+'2.Nh4Cl+ NH4OH')
    print(Fore.BLACK+'3.K4[Fe(CN)6]')
    print(Fore.BLACK+'4.dimethy+l glyoxime +NaOH')
    x=int(input('enter the number your desired chemical:  '))
    
    if ion=='Pb':
        if x==1:
            print(Fore.YELLOW+'yellow ppt produced')
            print('congratulations!,you are awsome:)')
        else:
            print('no ppt produced')
    elif ion=='Al':
        if x==2:
            print(BACK.BLACK);
            print(Fore.WHITE+'Gelatinous white ppt produced')
            print('congratulations!,proud of u:)')
        else:
            print('sorry :( no ppt produced')
    elif ion=='Cu':
        if x==3:
            print(Fore.BROWN+'Choclate brown ppt produced')
            print('congratulations! HATS OFF :)')
        else:
            print('No ppt produced :( better luck next time')
    elif ion=='Ni':
        if x==4:
            print(Fore.RED+'cherry red ppt prouced')
            print('congratulation! YOU ROCK!!!!!!!!!!!!!!!!!')
        else:
             print('no ppt found sorry :(')
    else:
        print(Fore.BLACK+'Invalid ion')
