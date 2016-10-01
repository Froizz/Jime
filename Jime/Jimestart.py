from Timer import countdown
from Calculator import calcul

######main loop########




def menu():
    print("Select operation.")
    print("1.Calculator")
    print("2.Coming soon")
    print("3.Coming soon")
    print("4.Coming soon")
    print("9.Exit")
    choice = input("Enter choice(1/2/3/4):")

    if choice == '9':
        exit()

    if choice == '1':
       calc=calcul()
       menu()

    print('=========================')    
    print(' \n \n Coming soon! \n \n')
    print('=========================')
    menu()
    

a=5
instance=countdown(a)
menu()  



