def isSafe(board,x,y,n):
    for row in range(x):
        if(board[row][y] == 1):
            return False
    
    row = x
    col = y
    while(row>=0 and col>=0):
        if(board[row][col] == 1):
            return False
        row -= 1
        col -= 1
    
    row = x
    col = y
    while(row>=0 and col<n):
        if(board[row][col] == 1):
            return False
        
        row -= 1
        col += 1

    return True


def nQueen(board,x,n):
    if(x==n):
        return True
    for col in range(n):
        if(isSafe(board,x,col,n)):
            board[x][col] = 1

            if(nQueen(board,x+1,n)):
                return True
            
            board[x][col] = 0
    return False



n = int(input())
board = []

for i in range(n):
    temp = [0]*n
    board.append(temp)

nQueen(board,0,n)
print("\n")
for i in range(n):
    print(board[i])
print("\n")