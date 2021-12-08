import string
import os
import time


coords = [[7,1], [5,2], [4,4], [2,5], [4,6], [3,8]]

def set_poles ():
    table = [['0']*9 for i in range(9)]
    table[-1] = [0] + list(string.ascii_lowercase[:8])
    for i in range(8):
        table[i][0] = 8-i
    return table

def print_table(table):
    for i in table:
        print(i)

def main():
    global coords
    table = set_poles()
    table[coords[0][0]][coords[0][1]] = '1'
    print_table(table)

while len(coords) > 0:
    os.system('clear')
    main()
    coords = coords[1::]
    time.sleep(1)