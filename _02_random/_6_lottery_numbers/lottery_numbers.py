import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    n3 = random.randint(0, 9)
    n4 = random.randint(0, 9)
    n5 = random.randint(0, 9)
    n6 = random.randint(0, 9)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title = 'Lottery Ticket', message='Your ticket number was: '+ str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
