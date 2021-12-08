def mult_table (num1, num2):

    table = [[0]*(abs(num1-num2)+1) for i in range(abs(num1-num2)+1)]
    set_params(table, num1, num2)
    const_table(table)
    print_table(table)

def set_params (table, num1, num2):
    if num1 < num2:
        table[0][0] = num1
        for i in range(1, len(table)):
            table[0][i] = table[0][i-1]+1
            table[i][0] = table[i-1][0]+1
    
    elif num1 > num2:
        table[0][0] = num1
        for i in range(1, len(table)):
            table[0][i] = table[0][i-1]-1
            table[i][0] = table[i-1][0]-1
    
    else:
        print('None')
        exit()

def const_table (table):
    for i in range(1, len(table)):
        for j in range(1, len(table)):
            table[i][j] = table[i][0] * table[0][j]

def print_table (table):
    for i in range(0, len(table)):
        print(table[i])

mult_table(1, 5)
print('...')
mult_table(5, 1)
print('...')
mult_table(1, 1)