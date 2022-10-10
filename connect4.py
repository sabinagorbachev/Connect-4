# board 0-41
board = ['_' for x in range(42)]

def print_board():
    print('  1   2   3   4   5   6   7')
    for i in range(42):
       # if(i % 7 ==0):
          #  print('     '),
        print('|' + ' ' + board[i]),
        if ((i+1)%7 == 0):
            print('|' + '\n')

# check for full board
def check_full():
    for i in range(42):
        if (board[i] == '_'):
            return False
    return True

# check move
def check_move(move):
    #checking for invalid column numbers entered
    if (move < 1 or move > 7):
        return False

    # checking for where piece lands and if column is full
    position = move+34
    while(position >= 0):
        if (board[position] == '_'):
            return position
        if(position<7 and board[position] != '_'):
            return False
        position -= 7

# check board for win
def check_win(move, start):
    # figure out where they landed
    position = move+34
    counter1 = 0
    counter2 = 0

    #vertical
    i = position
    while(i>=((move-1)%7)):
        if(board[i] == 'X'):
            counter1 += 1
        else:
            counter1 = 0
        if(board[i] == 'O'):
            counter2 += 1
        else:
            counter2 = 0
        if (counter1 == 4):
            return True
        if (counter2 == 4):
            return True
        """ print('vertical counter1: ' + str(counter1))
        print('vertical counter2: ' + str(counter2)) """
        i -=7
   
    # horizontal
    counter1 = 0
    counter2 = 0
    # going all the way left of the row
    j = start - (start % 7) 
    while (j <= ((start - (start % 7)) + 6)):
        if(board[j] == 'X'):
            counter1 += 1
        else:
            counter1 = 0
        if(board[j] == 'O'):
            counter2 += 1
        else:
            counter2 = 0
        if (counter1 == 4):
            return True
            break
        if (counter2 == 4):
            return True
            break
        #print('horizontal counter1: ' + str(counter1))
        #print('horizontal counter2: ' + str(counter2))
        j += 1
    
    # diagonal (index +- 8)
    k = start
    counter1 = 0
    counter2 = 0
    while (k <= start+18 and k <= 41):
        if(board[k] == 'X'):
            counter1 += 1
        else:
            counter1 = 0
        if(board[k] == 'O'):
            counter2 += 1
        else:
            counter2 = 0
        if (counter1 == 4):
            return True
            break
        if (counter2 == 4):
            return True
            break
        """ print('diagonal left counter1: ' + str(counter1))
        print('diagonal left counter2: ' + str(counter2)) """
        k += 6
    k = start
    counter1 = 0
    counter2 = 0
    while (k <= start+24 and k <= 41):
        if(board[k] == 'X'):
            counter1 += 1
        else:
            counter1 = 0
        if(board[k] == 'O'):
            counter2 += 1
        else:
            counter2 = 0
        if (counter1 == 4):
            return True
            break
        if (counter2 == 4):
            return True
            break
        """ print('diagonal right counter1: ' + str(counter1))
        print('diagonal right counter2: ' + str(counter2)) """
        k +=8


def play():
    print_board()
    while not check_full():
        #Player 1 (Red)
        while(True):
            move = int (input('Player 1: Please input a row (1-7) to place your piece: '))
            start = check_move(move)
            if (start == False):
                print('Invalid Entry, Please Try Again')
            elif (isinstance(start, int)):
                
                board[start] = 'X'
                print_board()
                
                if (check_full()):
                    print("Tie Game!")
                    break
                if (check_win(move, start)):
                    print("Player 1 Wins!")
                    break
                break

        if(check_win(move, start) or (check_full())):
            break

        #Player 2 (Yellow)
        while(True):
            move = int (input('Player 2: Please input a row (1-7) to place your piece: '))
            start = check_move(move)
            if (isinstance(start, int)):

                board[start] = 'O'
                print_board()
                
                if (check_full()):
                    print("Tie Game!")
                    break
                if (check_win(move, start)):
                    print("Player 2 Wins!")
                    break
                break
            elif (start == False):
                print('Invalid Entry, Please Try Again')

        if(check_win(move, start) or (check_full())):
            break


play()
