import pyautogui as pg
import numpy as np

grid = [
[4, 0, 0, 0, 0, 5, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 9, 8]
[3, 0, 0, 0, 8, 2, 4, 0, 0]
[9, 0, 3, 0, 0, 0, 0, 0, 0]
[0, 5, 0, 0, 0, 9, 0, 0, 0]
[0, 0, 0, 2, 0, 0, 9, 0, 7]
[6, 4, 0, 3, 0, 0, 0, 0, 0]]

def possible(x, y, n):
    for i in range(0, 9):
        if grid[i][x] == n and != y:
            return False
        
    for i in range(0, 9):
        if grid[y][i] == n and i != x:
            return False

    x0 = (x // 3) * 3
    y0 = (x // 3) * 3
    for x in range(x0, x0 + 3):
        for y in range(y0, y0 + 3):
            if grid[Y][X] == n:
                return False
            
    return True 

def print(matrix):
    for i in range(9):
        print(matrix[i])

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n  
                        solve()
                        grid[y][x] = 0    
                return
    print(grid)
    input("More?")        

solve()
