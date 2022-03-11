# Ball-Brick-Game

### To Play this game 

To play this game just clone this repository and run ` python ballbrick.py `

### Read the Instructions carefully below

1. Firstly you need to specify the size of the game environment    
2. Now yo need to specify the place and value of the bricks
3. There are the special blocks like DE, B & DS which will destroy the entire row, extends the ball base plate & destroys all the blocks around it respectively
4. If the ball is not placed at the previous position of the ball then ballcount wll be reduced by 1
5. If the ballcount is 0 and Still bricks are present then you will lose the game
5. If you can able able to break all the bricks within the balls then you will win the game


### Below shown is a demo of the game played

` 
!! Welcome to the Ball & Brick game using Python !!
1. Firstly you need to specify the size of the game environment    
2. Now yo need to specify the place and value of the bricks
3. There are the special blocks like DE, B & DS which will destroy the entire row, extends the ball base plate & destroys all the blocks around it respectively
4. If the ball is not placed at the previous position of the ball then ballcount wll be reduced by 1
5. If the ballcount is 0 and Still bricks are present then you will lose the game
5. If you can able able to break all the bricks within the balls then you will win the game

Enter the size of the game Matrix: 8
Enter the x,y position of bricks & value: 3 3 1
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 3 4 2
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 1 4 2
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 5 4 3
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 7 1 2
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 5 7 3
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 3 1 B
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 4 2 DS
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 4 1 2
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 3 6 DE
Enter Y to continue and N to terminate: y
Enter the x,y position of bricks & value: 1 2 B
Enter Y to continue and N to terminate: n

Enter the ballcount: 3
W       W       W       W       W       W       W       W
W               B               2                       W
W                                                       W
W       B               1       2               DE      W
W       2       DS                                      W
W                               3                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  19
Ballcount Left:  3
Enter the direction of ball or N: rd
W       W       W       W       W       W       W       W
W               B               2                       W
W                                                       W
W                               2               DE      W
W                                                       W
W                               3                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  15
Ballcount Left:  2
Enter the direction of ball or N: rd
W       W       W       W       W       W       W       W
W               B               2                       W
W                                                       W
W                               2               DE      W
W                                                       W
W                               3                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  15
Ballcount Left:  1
Enter the direction of ball or N: st
W       W       W       W       W       W       W       W
W               B               2                       W
W                                                       W
W                               2               DE      W
W                                                       W
W                               2                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  14
Ballcount Left:  1
Enter the direction of ball or N: st
W       W       W       W       W       W       W       W
W               B               2                       W
W                                                       W
W                               2               DE      W
W                                                       W
W                               1                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  13
Ballcount Left:  1
Enter the direction of ball or N: st
W       W       W       W       W       W       W       W
W               B               2                       W
W                                                       W
W                               2               DE      W
W                                                       W
W                                                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  12
Ballcount Left:  1
Enter the direction of ball or N: st
W       W       W       W       W       W       W       W
W               B               2                       W
W                                                       W
W                               1               DE      W
W                                                       W
W                                                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  11
Ballcount Left:  1
Enter the direction of ball or N: st
W       W       W       W       W       W       W       W
W               B               2                       W
W                                                       W
W                                               DE      W
W                                                       W
W                                                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  10
Ballcount Left:  1
Enter the direction of ball or N: st
W       W       W       W       W       W       W       W
W               B               1                       W
W                                                       W
W                                               DE      W
W                                                       W
W                                                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  9
Ballcount Left:  1
Enter the direction of ball or N: st
W       W       W       W       W       W       W       W
W               B                                       W
W                                                       W
W                                               DE      W
W                                                       W
W                                                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  8
Ballcount Left:  1
Enter the direction of ball or N: ld
W       W       W       W       W       W       W       W
W               B                                       W
W                                                       W
W                                                       W
W                                                       W
W                                                       W
W                                                       W
W       G       G       G       O       G       G       W

No.of Brick values left:  7
Ballcount Left:  0
Sorry
!!GameOver!!
You Didn't Won the Game
`
