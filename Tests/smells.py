

while True:
    print('how many times?')
    numberof=input()

    try:

        for i in range(int(numberof)):
            print('Jimmy smells')
    except:
        print(str(numberof)+' is not a number!')
    
