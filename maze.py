#0 for blocked cell
#1 for free cell
#order N*N
#source at 0,0 and the destinations is N-1, N-1
#movements are up, down, left, right

import random

directions = ((1,0,'D'),(-1,0,'U'),(0,1,'R'),(0,-1,'L'))

def isValid(i,j,maze): #si esta dentro de los limites de la matriz
    return 0<=i < len(maze) and 0<=j<len(maze[0]) 

def dfs(i,j,maze,visited,ans,path): 
    if i == len(maze)-1 and j == len(maze[0])-1: #if we reach th destination
        ans.append(path)
        return 
    visited.add((i,j))  #if not 

    for k in directions:
        newi, newj = i+k[0], j+k[1]
        if isValid(newi, newj, maze) and (newi, newj) not in visited and maze[newi][newj] == 1:
            dfs(newi,newj,maze,visited,ans,path+k[2])
    visited.remove((i,j))


def find_Path(maze,n): #(m is matrix, n for the size) initial call
    ans = []
    if maze[0][0] == 0 or maze[n-1][n-1] == 0:
        return ans
    path = ""
    visited = set() 
    dfs(0,0,maze,visited,ans,path)
    return ans

def generate_maze(n):
    maze = [[1 for _ in range(n)] for _ in range(n)] 
    
    for i in range(n):
        for j in range(n):
            if(i,j) != (0,0) and (i,j) != (n-1,n-1):
                if random.choice([0,1]) == 0:
                    maze[i][j] = 0
    return maze

n = 10
maze = generate_maze(n)
for row in maze:
    print(row)

# Encontrar todos los caminos posibles en el laberinto generado
paths = find_Path(maze, n)

# Imprimir los caminos encontrados
print("\nPaths Found:")
for path in paths:
    print(path)
