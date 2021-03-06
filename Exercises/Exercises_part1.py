from typing import List

# ----------------------------------------------------------------
# brute force
def sumUpToKOLD(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False


# with hash map (fastest index system)
def sumUpToK(arr, k):
    visitedElements = {} # hash map
    for index, item in enumerate(arr):
        if visitedElements.get(k-item):
            return True
        else:
            visitedElements[item] = True
    return False


# ----------------------------------------------------------------
# brute force
def firstRepeatingCharacter(str: str):
    for i in range(len(str)):
        for j in range(i):
            if str[i] == str[j]:
                return str[i]
    return "\0"


# with hash map (fastest index system)
def firstRepeatingCharacter_hashMap(str):
    visitedElements = {}
    for char in str:
        if visitedElements.get(char):
            return char
        else:
            visitedElements[char] = True
    return "\0"


def firstUniqueCharacter(str: str):
    for index, char in enumerate(str):
        tempStr = str
        tempStr = tempStr.replace(char, '', 1)
        if not tempStr.__contains__(char):
            return index
    return -1

# ----------------------------------------------------------------
def _removeDuplicates(arr):
    visitedElements = {}
    indexToRemove = []
    for index, value in enumerate(arr):
        if visitedElements.get(value):
            indexToRemove.append(index)
        else:
            visitedElements[value] = True
    
    # We reverse array to be able to properly pop an item from index
    for index in sorted(indexToRemove, reverse=True):
        del arr[index]
    return arr

def removeDuplicates_simpler(arr):
    noDuplicates = []
    for value in arr:
        if value not in noDuplicates:
            noDuplicates.append(value)
    return noDuplicates


# Best solutions
def removeDuplicates(arr):
    visitedElements = {}
    for value in arr:
        visitedElements[value] = True
    return list(visitedElements.keys())

# ----------------------------------------------------------------
def findDuplicate(arr):
    visitedElements = {}
    for value in arr:
        if visitedElements.get(value):
            return value
        else:
            visitedElements[value] = True
    return 0


# Floyd's cycle detection algorithm (tortoise and hare)
def findDuplicateFloyd(arr):
    tortoise = arr[0]
    hare = arr[arr[0]]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
    tortoise = 0
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    return tortoise


def generateMatchingParenthesis(n: int):
    return True
