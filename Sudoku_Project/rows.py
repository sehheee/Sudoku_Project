import pyautogui as pg
import numpy as np
import time

grid = []

while True: 
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row: ' + str(len(grid)) + ' Complete')

time.sleep(3)

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
    final = []
    str_fin = [] 
    for i in range(9):
        final.append(matrix[i])

    for lists in finals:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')


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
