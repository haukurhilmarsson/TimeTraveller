#One big while loop to keep the player in the game
#Player starts in tyle 1,1
#Player enters the direction in which he wants to go
#Player's new tyle displayed
#Every tyle is its own variable with its own possible inputs
#When the player gets to the tile 3,1 the while loop stops and the player wins

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

while not win:
    if position == tile1:
        if validation == 1:
            print("You can travel: (N)orth.")
        command = str(input("Direction: "))
        if command == 'n' or command == 'N':
            position = tile2
            win = False
            validation = 1
        else:
            print("Not a valid direction!")
            validation = 0

    elif position == tile2:
        if validation == 1:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
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
            print("Not a valid direction!")
            validation = 0

    elif position == tile3:
        if validation == 1:
            print("You can travel: (E)ast or (S)outh.")
        command = str(input("Direction: "))
        if command == 'E' or command == 'e':
            position = tile4
            validation = 1
        elif command == 'S' or command == 's':
            position = tile2
            validation = 1
        else:
            print("Not a valid direction!")
            validation = 0

    elif position == tile4:
        if validation == 1:
            print("You can travel: (E)ast or (W)est.")
        command = str(input("Direction: "))
        if command == 'W' or command == 'w':
            position = tile3
            validation = 1
        elif command == 'E' or command == 'e':
            position = tile7
            validation = 1
        else:
            print("Not a valid direction!")
            validation = 0

    elif position == tile5:
        if validation == 1:
            print("You can travel: (S)outh or (W)est.")
        command = str(input("Direction: "))
        if command == 'S' or command == 's':
            position = tile6
            validation = 1
        elif command == 'W' or command == 'w':
            position = tile2
            validation = 1
        else:
            print("Not a valid direction!")
            validation = 0

    elif position == tile6:
        if validation == 1:
            print("You can travel: (N)orth.")
        command = str(input("Direction: "))
        if command == 'N' or command == 'n':
            position = tile5
            validation = 1
        else:
            print("Not a valid direction!")
            validation = 0

    elif position == tile7:
        if validation == 1:
            print("You can travel: (S)outh or (W)est.")
        command = str(input("Direction: "))
        if command == 'W' or command == 'w':
            position = tile4
            validation = 1
        elif command == 'S' or command == 's':
            position = tile8
            validation = 1
        else:
            print("Not a valid direction!")
            validation = 0

    elif position == tile8:
        if validation == 1:
            print("You can travel: (N)orth or (S)outh.")
        command = str(input("Direction: "))
        if command == 'N' or command == 'n':
            position = tile7
            validation = 1
        elif command == 'S' or command == 's':
            position = tile9
            validation = 1
        else:
            print("Not a valid direction!")
            validation = 0

    elif position == tile9:
        print("Victory!")
        win = True
