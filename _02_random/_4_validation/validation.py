import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment
    if random_number == 1:
        print('Happy early birthday!')
    elif random_number == 2:
        print('You are good at coding!')
    elif random_number == 3:
        print('You look fine.')
    elif random_number == 4:
        print('You are fast.')
    else:
        print('Nice job coding this project')
    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
