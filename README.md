# Python 3 concepts

## Getting Started with Basic concepts Syntaxs

### Comments

```
# This is a one-line Python comment - code blocks are so useful!
"""This type of comment is used to document the purpose of functions and classes."""
```

### Declaration/ Initialization

``` python
# Remember values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
answer = 42
answer = "The answer is 42."
```

### Data Types

``` python
1. boolean = True

2. number = 1.1

3. string = "Strings can be declared with single or double quotes."

4. list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]

5. tuple = ("Tuples", "can have", "more than", 2, "elements!")

6. dictionary = {'one': 1, 'two': 2, 'three': 3}

7. variable_with_zero_data = None
```

### Simple Logging

``` python
1. print "Printed!"

2. f.write()
```


### Conditionals

``` python
if cake == "delicious":
    return "Yes please!"
elif cake == "okay":
    return "I'll have a small piece."
else:
    return "No, thank you."
```


### Loops

``` python
# For Loops
for item in list:
    print item

# While Loops
while (total < max_val):
    total += values[i]
    i += 2
```


### Functions

``` python
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print q, r
```


### Classes

``` python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
```


### Methods & Operators

#### General
```python
1. range(start, end, step) : # Returns a range of Numbers . Range(10) will return 0-9

2. len(elem) : # returns the length of a list.

3. sorted() :

4. sort() :

5. in :  (x in dict / list) # returns boolean, checks if 'x' exists in a the dict or list.

6. dict.get(): #which returns the value or None if the key is not present (or get(key, not-found) allows you to specify what value to return in the not-found case).
```
[More about Sort & Sorted](https://developers.google.com/edu/python/sorting)

#### String Methods

```python
1. s.lower(), s.upper() -- #returns the lowercase or uppercase version of the string

2. s.strip() -- #returns a string with whitespace removed from the start and end

3. s.isalpha()/s.isdigit()/s.isspace()... -- #tests if all the string chars are in the various character classes

4. s.startswith('other'), s.endswith('other') -- #tests if the string starts or ends with the given other string

5. s.find('other') -- # for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found

6. s.replace('old', 'new') -- #returns a string where all occurrences of 'old' have been replaced by 'new'

7. s.split('delim') -- #returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.

8. s.join(list) -- #opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
```
[More About Strings](https://developers.google.com/edu/python/strings)

#### List Methods

``` python
1. list.append(elem) -- #adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.

2. list.insert(index, elem) -- #inserts the element at the given index, shifting elements to the right.

3. list.extend(list2) #adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().

4. list.index(elem) -- #searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).

5. list.remove(elem) -- #searches for the first instance of the given element and removes it (throws ValueError if not present)

6. list.sort() -- #sorts the list in place (does not return it). (The sorted() function shown later is preferred.)

7. list.reverse() -- #reverses the list in place (does not return it)

8. list.pop(index) -- #removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
```
[More About Lists](https://developers.google.com/edu/python/lists)

#### Dict / Hash Table

```Python
1. keys() #returns keys, values() and items() : return lists of the keys or values explicitly. There's also an items() which returns a list of (key, value) tuples, which is the most efficient way to examine all the key value data in the dictionary

2. iterkeys(), itervalues() and iteritems() #:SAME but which avoid the cost of constructing the whole list -- a performance win if the data is huge.

3. del  #operator

4. dict.get() #which returns the value or None if the key is not present (or get(key, not-found) allows you to specify what value to return in the not-found case).
```

#### Files

```Python
1. open()
2. close()
3. write()
```

### Time & Space Complexities

[BigO](https://www.bigocheatsheet.com/).
