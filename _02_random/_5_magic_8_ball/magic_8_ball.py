import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    q = simpledialog.askstring(None, prompt='Enter a question for the Magic 8 Ball.')
    # Make a variable and initialize it to a random number between 0 and 3
    ran = random.randint(0, 3)
    # If the random number is 0
    if ran == 0:
        print('Yes')
        # tell the user "Yes"

    # If the random number is 1
    if ran == 1:
        print('No')
        # tell the user "No"

    # If the random number is 2
    if ran == 2:
        print('Maybe you should ask Google?')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if ran == 3:
        print('I was told to write an answer but I am not sure about that one. ')
        # write your own answer
