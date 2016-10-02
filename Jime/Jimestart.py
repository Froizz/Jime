from Timer import countdown
from Calculator import calcul
from Wormy import main as worm

######main loop########




def menu():
    print('=========================')
    print("\n Select operation. \n")
    print('=========================')
    print("\n 1.Calculator \n")
    print('=========================')
    print("\n 2.Wormy \n")
    print('=========================')
    print("\n 3.The Time (UNAVALIABLE) \n")
    print('=========================')
    print("\n 4.Coming soon \n")
    print('=========================')
    print("\n 9.Exit \n")
    print('=========================')
    choice = input("\n Enter choice(1/2/3/4):")
    print('=========================')

    if choice == '9':
        exit()

    if choice == '1':
       calc=calcul()
       menu()

    if choice == '2':
       wormy=worm()
       menu()

    if choice == '3':
        print('\n')
        print('Sorry UNAVAILIABLE')
        print('\n')
        menu()


    print('=========================')    
    print(' \n \n Coming soon! \n \n')
    print('=========================')
    menu()
    

a=5
instance=countdown(a)
menu()  



