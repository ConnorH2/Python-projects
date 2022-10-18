import math
data = [[0,0,0],
        [0,0,0],
        [0,0,0]]
turn = 0
def board():
    print(" " + data[0][0] + " |  |  ")
    print("--+--+--")
    print("  |  |  ")
    print("--+--+--")
    print("  |  |  ")
player_icon = input("Choose your icon, X(1) or O(0): ")
order = randrange(1)
while(true):
    if(order == 0):
        print("Your turn")



