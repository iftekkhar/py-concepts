"""
Home Work : 6
Topic : Playing Board
"""


def drawBoard(a, b):
    if a == b:
        c = 0
    else:
        c = 1
    for row in range(a):
        if row % 2 == 0:
            for col in range(b):
                if col % 2 == c:
                    if col != b-1:
                        print(' ', end='')
                    else:
                        print(' ')
                else:
                    print('|', end='')
        else:
            print('-'*b)


drawBoard(11, 18)
