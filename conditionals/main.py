'''
Home work : 2
Topic : Create Conditional to See if the given number Matches
'''


def isSame(first, second, third):
    if int(first) == int(second) or int(first) == int(third):
        print(True)
    elif int(second) == int(third):
        print(True)
    else:
        print(False)


isSame(45, 56, '56')
