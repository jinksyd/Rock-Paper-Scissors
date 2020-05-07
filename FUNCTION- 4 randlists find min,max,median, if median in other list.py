import random
import statistics

def randlist(n,m):
    ## This function generates a list of size n made of random numbs
    templist = []
    for i in range(n):
        x = random.randrange(0,m)
        templist.append(x)
    return templist

def statlist(templist2):
    ## This function calculates the min, max, and median value in a list
    ## templlist2 could be called templist bc it's completely different than the other templist since it's local
    return min(templist2), max(templist2), statistics.median(templist2)

def inlist(templist, element):
    ##This function checks if an element exists in a list
    if element in templist:
        return templist.index(element)
    else:
        return("Element not found")

A = randlist(500, 500)
B = randlist(200, 600)
C = randlist(300, 250)
D = randlist(100, 350)
print(A)
print(B)
print(C)
print(D)

minA,maxA,medianA = statlist(A)
minB,maxB,medianB = statlist(B)
minC,maxC,medianC = statlist(C)
minD,maxD,medianD = statlist(D)

print("The min of listA is",minA,"max is",maxA,"and median of list A is", medianA)
print("The min of listB is",minB,"max is",maxB,"and median is:",medianB)
print("The min of list C is",minC,"max is",maxC,"and median is",medianC)
print("The min of list D is",minD,"max is",maxD,"and median is",medianD)

print(inlist(A, medianB))
print(inlist(A,medianC))
print(inlist(A,medianD))
