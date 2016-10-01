import time


# Define function to count down
def countdown(t):
    print('This Program will load in 5 seconds...')
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('\nWelcome to Jime!')
