#0 for blocked cell
#1 for free cell
#order N*N
#source at 0,0 and the destinations is N-1, N-1
#movements are up, down, left, right

import random

directions = ((1,0,'D'),(-1,0,'U'),(0,1,'R'),(0,-1,'L'))

def isValid(i,j,m): #si esta dentro de los limites de la matriz
    return 0<=i < len(m) and 0<=j<len(m[0]) 

def dfs(i,j,m,visited,ans,path): 
    if i == len(m)-1 and j == len(m[0])-1: #if we reach th destination
        ans.append(path)
        return 
    visited.add((i,j))  #if not 

    for k in directions:
        newi, newj = i+k[0], j+k[1]
        if isValid(newi, newj, m) and (newi, newj) not in visited and m[newi][newj] == 1:
            dfs(newi,newj,m,visited,ans,path+k[2])
    visited.remove((i,j))


def find_Path(m,n): #(m is matrix, n for the size) initial call
    ans = []
    if m[0][0] == 0 or m[n-1][n-1] == 0:
        return ans
    path = ""
    visited = set() 
    dfs(0,0,m,visited,ans,path)
    return ans

def generate_maze(n):
    


m = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
n = 4
paths = find_Path(m, n)
print(paths) 