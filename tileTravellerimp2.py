#https://github.com/haukurhilmarsson/TimeTraveller
#One big while loop to keep the player in the game
#Player starts in tyle 1,1
#Player enters the direction in which he wants to go
#Player's new tyle displayed
#Every tyle is its own variable with its own possible inputs
#When the player gets to the tile 3,1 the while loop stops and the player wins
#1. Implementaion 2 wasnt so much easire, the if statements took a lot of time and I couldn't find a way to make a good function out of them.
#2. Imp 2 is a little more readable, because the function names make it clear what each tile is going to print out.
#3. No problems solved, only made the code look a little better

tile1 = 1.1
tile2 = 1.2
tile3 = 1.3
tile4 = 2.3
tile5 = 2.2
tile6 = 2.1
tile7 = 3.3
tile8 = 3.2
tile9 = 3.1

position = tile1

win = False

validation = 1

def unvalid(val):
    print("Not a valid direction!")
    val = 0
    return val

def ti1():
    print("You can travel: (N)orth.")
    return
def ti2():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    return
def ti3():
    print("You can travel: (E)ast or (S)outh.")
    return
def ti4():
    print("You can travel: (E)ast or (W)est.")
    return
def ti5():
    print("You can travel: (S)outh or (W)est.")
    return
def ti6():
    print("You can travel: (N)orth.")
    return
def ti7():
    print("You can travel: (S)outh or (W)est.")
    return
def ti8():
    print("You can travel: (N)orth or (S)outh.")
    return
def ti9():
    print("Victory!")
    return


while not win:
    if position == tile1:
        if validation == 1:
            ti1()
        command = str(input("Direction: "))
        if command == 'n' or command == 'N':
            position = tile2
            win = False
            validation = 1
        else:
            unvalid(validation)

    elif position == tile2:
        if validation == 1:
            ti2()
        command = str(input("Direction: "))
        if command == 'N' or command == 'n':
            position = tile3
            validation = 1
        elif command == 'E' or command == 'e':
            position = tile5
            validation = 1
        elif command == 'S' or command == 's':
            position = tile1
            validation = 1
        else:
            unvalid(validation)

    elif position == tile3:
        if validation == 1:
            ti3()
        command = str(input("Direction: "))
        if command == 'E' or command == 'e':
            position = tile4
            validation = 1
        elif command == 'S' or command == 's':
            position = tile2
            validation = 1
        else:
            unvalid(validation)

    elif position == tile4:
        if validation == 1:
            ti4()
        command = str(input("Direction: "))
        if command == 'W' or command == 'w':
            position = tile3
            validation = 1
        elif command == 'E' or command == 'e':
            position = tile7
            validation = 1
        else:
            unvalid(validation)

    elif position == tile5:
        if validation == 1:
            ti5()
        command = str(input("Direction: "))
        if command == 'S' or command == 's':
            position = tile6
            validation = 1
        elif command == 'W' or command == 'w':
            position = tile2
            validation = 1
        else:
            unvalid(validation)

    elif position == tile6:
        if validation == 1:
            ti6()
        command = str(input("Direction: "))
        if command == 'N' or command == 'n':
            position = tile5
            validation = 1
        else:
            unvalid(validation)

    elif position == tile7:
        if validation == 1:
            ti7()
        command = str(input("Direction: "))
        if command == 'W' or command == 'w':
            position = tile4
            validation = 1
        elif command == 'S' or command == 's':
            position = tile8
            validation = 1
        else:
            unvalid(validation)

    elif position == tile8:
        if validation == 1:
            ti8()
        command = str(input("Direction: "))
        if command == 'N' or command == 'n':
            position = tile7
            validation = 1
        elif command == 'S' or command == 's':
            position = tile9
            validation = 1
        else:
            unvalid(validation)

    elif position == tile9:
        ti9()
        win = True
