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

while win == False:
    if position == tile1:
        command = input("You can travel: (N)orth.")
            if command = 'n' or command = 'N':
                position = tile2
            else:
                print("Not a valid direction! ")
    if position == tile2:
        command = input("You can travel: (N)orth or (E)ast or (S)outh.")
    if position == tile3:
        command = input("You can travel: (E)east or (S)outh.")
    if position == tile4:
        command = input("You can travel: (W)est or (S)outh.")
    if position == tile5:
        command = input("You can travel: (W)est or (S)outh.")
    if position == tile6:
        command = input("You can travel: (N)orth.")
    if position == tile7:
        command = input("You can travel: (W)est or (S)outh.")
    if position == tile8:
        command = input("You can travel: (N)orth or (S)outh.")
    if position == tile9:
        win = True
