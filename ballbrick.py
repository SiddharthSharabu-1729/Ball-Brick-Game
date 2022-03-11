print("\t\t!! Welcome to the Ball & Brick game using Python !!\n1. Firstly you need to specify the size of the game environment")
print("2. Now yo need to specify the place and value of the bricks\n3. There are the special blocks like DE, B & DS which will destroy the entire row, extends the ball base plate & destroys all the blocks around it respectively")
print("4. If the ball is not placed at the previous position of the ball then ballcount wll be reduced by 1\n5. If the ballcount is 0 and Still bricks are present then you will lose the game")
print("5. If you can able able to break all the bricks within the balls then you will win the game\n")

n = int(input("Enter the size of the game Matrix: "))

bricks = []

## Taking the input Brick position from the User

while True :
    try :
        x,y,v = input("Enter the x,y position of bricks & value: ").split()
    except :
        ValueError
        print("Invalid Input")
        continue
    if str(x).isdigit() and str(y).isdigit() and (v in ["DE","DS","B","de","ds","b"] or str(v).isdigit()):
        if int(x) in range(n) and int(y) in range(n) :
            bricks.append([int(x),int(y),v])
        else :
            print("\nEnter Valid Range of Numbers to Place the Bricks from 0 to ",n)
            continue
        s = input("Enter Y to continue and N to terminate: ")
        if s == "Y" or s == "y" :
            continue
        elif s == "N" or s == "n" :
            break
        else :
            print("\nInvalid Option")
    else :
        print("\nInvalid values\nEnter the Correct Values")
        continue


ballcount = int(input("\nEnter the ballcount: "))
summ = 0
game = [[" " for i in range(n)] for i in range(n)]
flag = 0
a,b = 0,0

## Intitialising and calculating all the values of the Bricks into summ

for brick in bricks :
    game[brick[0]][brick[1]] = brick[2]
    if str(brick[2]).isdigit() :
        summ += int(brick[2])
    else :
        summ += 1

## Calculating the Position of the Ball

mid = n // 2
game[-1] = ['G' for i in range(n)]
game[-1][mid] = "O"

balpos = [len(game)-1,mid]

game[0] = ["W" for i in range(n)]

for tmp in range(n) :
    game[tmp][-1] = "W"
    game[tmp][0] = "W"


## Defining all the Required Functions 

def pri(x,y):
    for i in game :
        for j in i :
            print(j,end="\t")
        print()
    print("\nNo.of Brick values left: ",x)
    print("Ballcount Left: ",y)
        

def star(x,y,game):
    if game[x][y] == "W":
        return 0
    elif game[x][y] == " ":
        return star(x-1,y,game)
    else :
        return [x,y]
        
def DS(x,y,game,n) :
    c = 0
    if (x > 1 and y > 1) and (x < n-2 and y < n-2) :
        l = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    elif (x == 1 and y == 1):
        l = [[0,1],[1,1],[1,0]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    elif (x > 1 and y == 1) and (x > 1 and x < n-2) :
        l = [[-1,0],[-1,1],[0,1],[1,1],[1,0]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    elif (x == n-2 and y == 1) :
        l = [[-1,0],[-1,1],[0,1]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    elif (x == n-2 and y > 1) and y < n-2 :
        l = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    elif (x == n-2 and y == n-2) :
        l = [[0,-1],[-1,-1],[-1,0]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    elif (x > 1 and y == n-2) and x < n-2 :
        l = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    elif x == 1 and y < n-2 :
        l = [[0,-1],[1,-1],[1,0]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    elif (x == 1 and y > 1) and y < n-2 :
        l = [[0,-1],[1,-1],[1,0],[1,1],[0,1]]
        for i in l :
            if game[x+i[0]][y+i[1]] != " " :
                if str(game[x+i[0]][y+i[1]]).isdigit() :
                    game[x+i[0]][y+i[1]] = int(game[x+i[0]][y+i[1]])
                    c += game[x+i[0]][y+i[1]]
            game[x+i[0]][y+i[1]] = " "
    game[x][y] = " "
    c += 1

    return [game,c]

def dia(x,y,game,n):
    if n == "l" :
        if game[x][y] == " " :
            return dia(x-1,y-1,game,"l")
        elif game[x][y] == "W" :
            i = 0
            while i < len(game)-1 :
                if game[x][i] != " " and game[x][i] != "W" :
                    break
                else :
                    i += 1
            return [x,i]
        else :
            return [x,y]
    elif n == "r" :
        if game[x][y] == " " :
            return dia(x-1,y+1,game,"r")
        elif game[x][y] == "W" :
            i = len(game)-1
            while i != 0 :
                if game[x][i] != " " and game[x][i] != "W" :
                    break
                else :
                    i -= 1
            return [x,i]
        else :
            return [x,y]   

def DE(g):
    ss = []
    for i in g:
        if i != " " and i != "W" :
            if str(i).isdigit() :
                ss.append(1)
            else :
                ss.append(1)
    return ss

pri(summ,ballcount)


"""  
  Taking the Inputs from the User for playing the game 
  The Inputs are as follows :
        ST or st for Straright Movement
        LD or ld for Left Diagonal Movement
        Rd or rd for Right Diagonal Movement

"""


while True :
    if ballcount != 0 and summ != 0:
        x,y = n-1,mid
        Input = input("Enter the direction of ball or N: ")
        if Input in ["ST","st","LD","ld","RD","rd"] :
            if Input == "N" or Input == "n":
                break
            elif Input == "ST" or Input == "st":
                t = star(x-1,y,game)
                if t == 0 :
                    pass
                elif game[t[0]][t[1]] == "DE" :
                    lst = DE(game[t[0]])
                    summ -= sum(lst)
                    game[t[0]] = ["W" if i==0 or i==n-1 else " " for i in range(n)]
                elif game[t[0]][t[1]] == "DS" :
                    tmp = DS(t[0],t[1],game,n)
                    game = tmp[0]
                    summ -= tmp[1]
                elif str(game[t[0]][t[1]]).isdigit() :
                    if int(game[t[0]][t[1]]) > 1 :
                        game[t[0]][t[1]] = int(game[t[0]][t[1]])
                        game[t[0]][t[1]] -= 1
                        summ -= 1
                    else:
                        game[t[0]][t[1]] = " "
                        summ -= 1
                elif game[t[0]][t[1]] == "B" :
                    if flag == 0 :
                        b += 1
                        game[-1][mid+b] = "_"
                        flag = 1
                        game[t[0]][t[1]] = " "
                        summ -= 1
                    else :
                        a += 1
                        game[-1][mid-a] = "_"
                        flag = 0
                        game[t[0]][t[1]] = " "
                        summ -= 1
                pri(summ,ballcount)
            elif Input == "LD" or Input == "ld":
                t = dia(x-1,y-1,game,"l")
                if game[t[0]][t[1]] == "DE" :
                    lst = DE(game[t[0]])
                    summ -= sum(lst)
                    game[t[0]] = ["W" if i==0 or i==n-1 else " " for i in range(n)]
                    if t[1] != mid and game[-1][t[1]] != "_":
                        ballcount -= 1
                elif game[t[0]][t[1]] == "DS" :
                    tmp = DS(t[0],t[1],game,n)
                    game = tmp[0]
                    summ -= tmp[1]
                    if t[1] != mid and game[-1][t[1]] != "_" :
                        ballcount -= 1
                elif str(game[t[0]][t[1]]).isdigit() :
                    if int(game[t[0]][t[1]]) > 1 :
                        game[t[0]][t[1]] = int(game[t[0]][t[1]])
                        game[t[0]][t[1]] -= 1
                        summ -= 1
                        if t[1] != mid and game[-1][t[1]] != "_":
                            ballcount -= 1
                    else:
                        game[t[0]][t[1]] = " "
                        summ -= 1
                        if t[1] != mid and game[-1][t[1]] != "_":
                            ballcount -= 1
                elif game[t[0]][t[1]] == "B" :
                    if flag == 0 :
                        b += 1
                        game[-1][mid+b] = "_"
                        flag = 1
                        game[t[0]][t[1]] = " "
                        summ -= 1
                    else :
                        a += 1
                        game[-1][mid-a] = "_"
                        flag = 0
                        game[t[0]][t[1]] = " "
                        summ -= 1
                elif game[t[0]][t[1]] == "W":
                    ballcount -= 1
                pri(summ,ballcount)
            elif Input == "RD" or Input == "rd":
                t = dia(x-1,y+1,game,"r")
                if game[t[0]][t[1]] == "DE" :
                    lst = DE(game[t[0]])
                    summ -= sum(lst)
                    game[t[0]] = ["W" if i==0 or i==n-1 else " " for i in range(n)]
                    if t[1] != mid and game[-1][t[1]] != "_":
                        ballcount -= 1
                elif game[t[0]][t[1]] == "DS" :
                    tmp = DS(t[0],t[1],game,n)
                    game = tmp[0]
                    summ -= tmp[1]
                    if t[1] != mid and game[-1][t[1]] != "_":
                        ballcount -= 1
                elif str(game[t[0]][t[1]]).isdigit() :
                    if int(game[t[0]][t[1]]) > 1 :
                        game[t[0]][t[1]] = int(game[t[0]][t[1]])
                        game[t[0]][t[1]] -= 1
                        summ -= 1
                        if t[1] != mid and game[-1][t[1]] != "_":
                            ballcount -= 1
                    else:
                        game[t[0]][t[1]] = " "
                        summ -= 1
                        if t[1] != mid and game[-1][t[1]] != "_":
                            ballcount -= 1
                elif game[t[0]][t[1]] == "B" :
                    if flag == 0 :
                        b += 1
                        game[-1][mid+b] = "_"
                        flag = 1
                        game[t[0]][t[1]] = " "
                        summ -= 1
                    else :
                        a += 1
                        game[-1][mid-a] = "_"
                        flag = 0
                        game[t[0]][t[1]] = " "
                        summ -= 1
                elif game[t[0]][t[1]] == "W":
                    ballcount -= 1
                pri(summ,ballcount)
        else :
            print("\nInvalid Option\nPlease Enter a Valid Option LD or ST or RD\n")
            continue
    elif ballcount == 0 and summ != 0 :
        print("Sorry\n!!GameOver!!\nYou Didn't Won the Game")
        break
    elif (ballcount != 0 and summ == 0) or (ballcount == 0 and summ == 0) :
        print("\n!!!  Hurray You Won the Game  !!!")
        break
