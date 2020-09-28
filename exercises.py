from typing import List

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


def removeDuplicates(arr):
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



def generateMatchingParenthesis(n: int):
    return True