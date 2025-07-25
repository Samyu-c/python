w=True
while w:
    print('1.guess no.')
    print('2. guess floating no.')
    print('3.guess character')
    print('0 to exit')
x=int(input('enter choice '))
if x==1:
    def guessno(a,b):
        import random
        y=int(input('enter you guessing no.:'))
        z=random.randint(a,b)
        if y==z:
            print ('SUPER')
        else:
            print('no')
    a=int(input('enter upper limit'))
    b=int(input('enter lower limit:'))
    guessno(a,b)
if x==2:
    def floatno(a,b):
        import random
        y=int(input('enter you guessing no.:'))
        z=random.random()*(b-a)+a
        if y==z:
            print ('SUPER')
        else:
            print('no')
    a=int(input('enter upper limit'))
    b=int(input('enter lower limit:'))
    floatno(a,b)
if x==3:
    def character():
        l=['vijay', 'ajith', 'rajini','jeeva']
        print(l)
        q=input('enter guessed character')
        import random
        z=random.randomint(0,len(l))
        if y==z:
            print ('SUPER')
        else:
            print('no')
if x==0:
    w=False
        
        
                   
         
        
