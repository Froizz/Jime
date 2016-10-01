import time


# Define function to count down
def countdown(t):
    print('This window will remain open for'+str(t) +'more seconds...')
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('Goodbye! \n \n \n \n \n')
    value = ["custard","Ham","Eggs","Spam","Baked Beans"]
    return(value)





def custard():
    print("custard")
    return


def countdown2(t):
    print('This window will remain open for 3 more seconds...')
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('Goodbye! \n \n \n \n \n')
    Food ="SPAM"

    
    value = {"Food":Food,"Pudding":"Custard"}
    return(value)
