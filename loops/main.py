"""
Home Work : 5
Topic : fizzBuzz
"""


for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        print(i, 'FizzBuzz')
    elif i % 2 == 0:
        print(i, 'Fizz')
    elif i % 5 == 0:
        print(i, 'Buzz')
