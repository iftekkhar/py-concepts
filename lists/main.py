"""
Home Work : 4
Topic : Push element to an empty and check if the element already exists or not
"""

myUniqueList = []
myLeftovers = []


# function for appending unique elements to list
def addToList(element):
    if element in myUniqueList:
        myLeftovers.append(element)
        return False
    else:
        myUniqueList.append(element)
        return True


addToList(20)
addToList(20)
addToList(70)
addToList(50)
addToList(90)
addToList(20)
addToList(40)
addToList(70)
addToList(90)
addToList(10)
addToList(60)
print(myUniqueList)
print(myLeftovers)
