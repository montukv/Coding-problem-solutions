def isSafe(maze,x,y):
    if(x<len(maze) and y<len(maze) and maze[x][y] == 1):
        return True
    return False 

def findPath(maze,x,y,path):
    
    if(x==len(maze)-1 and y == len(maze)-1):
        path[x][y] = 1
        return True

    if(isSafe(maze,x,y)):
        path[x][y] = 1 
        if(findPath(maze,x+1,y,path)):
            return True
        if(findPath(maze,x,y+1,path)):
            return True
        path[x][y] = 0
        return False
n = int(input())
maze = []
temp = []
for i in range(n):
    temp = list(map(int,input().split()))
    maze.append(temp)

path = []
for i in range(n):
    temp = [0]*n
    path.append(temp)

if(findPath(maze,0,0,path)):
    print("\n\n")
    for i in range(n):
        print(path[i])
else:
    print("No sol")


# 5
# 1 0 1 0 1
# 1 1 1 1 1
# 0 1 0 1 0
# 1 0 0 1 1
# 1 1 1 0 1