import math
import random
data = [[0,0,0],
        [0,0,0],
        [0,0,0]]
turn = 0
def getstr(a):
    if a==0:
        return " "
    elif a==1:
        return "X"
    else:
        return "O"
def board():
    print(" " + getstr(data[0][0]) + " | " + getstr(data[0][1]) + " | " + getstr(data[0][2]))
    print("---+---+---")
    print(" " + getstr(data[1][0]) + " | " + getstr(data[1][1]) + " | " + getstr(data[1][2]))
    print("---+---+---")
    print(" " + getstr(data[2][0]) + " | " + getstr(data[2][1]) + " | " + getstr(data[2][2]))

def checkwin():
    for x in data: #row check
        if(x[0]==x[1] and x[1]==x[2]):
            if(x[0] == inum):
                win()
            if(x[0] == onum):
                lose()
    for i in range(3): #column check
        if(data[0][i]==data[1][i] and data[1][i]==data[2][i]):
            if(data[0][i] == inum):
                win()
            if(data[0][i] == onum):
                lose()
    if(data[0][0]==data[1][1] and data[1][1]==data[2][2]): #diag 1 check
        if(data[0][0] == inum):
            win()
        if(data[0][0] == onum):
            lose()
    if(data[2][0]==data[1][1] and data[1][1]==data[0][2]): #diag 2 check
        if(data[2][0] == inum):
            win()
        if(data[2][0] == onum):
            lose()

def win():
    board()
    print("YOU WIN!!!")
    quit()
def lose():
    board()
    print("You lose...")
    quit()
    

player_icon = input("Choose your icon, X(1) or O(0): ")
if(player_icon == "1"):
    inum = 1
    onum = 2
    print("X selected!")
else:
    inum = 2
    onum = 1
    print("O selected!")
order = random.randrange(2)
#order = 1
while(True):
    board()
    if(order == 0):
        print("Your turn!")
        while(True):
            irow = int(input("Choose a row, 1, 2, or 3: ")) - 1
            icolumn = int(input("Choose a column, 1, 2, or 3: ")) - 1
            if(data[irow][icolumn] == 0):
                break;
            elif(data[irow][icolumn] == inum):
                print("You already filled that spot!")
            else:
                print("Your opponent already filled that spot!")
        data[irow][icolumn] = inum
        order = 1
    else:
        print("Opponent's turn")
        while(True):
            irow = random.randrange(3)
            icolumn = random.randrange(3)
            if(data[irow][icolumn] == 0):
                print(str(irow) + " " + str(icolumn))
                break;
        data[irow][icolumn] = onum
        print(getstr(data[irow][icolumn]))
        order = 0
    checkwin()
    turn += 1
        



