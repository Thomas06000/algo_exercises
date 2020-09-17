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


def firstRepeatingCharacter(str: str):
    for i in range(len(str)):
        for j in range(i):
            if str[i] == str[j]:
                return str[i]
    return "\0"

def firstUniqueCharacter(str: str):
    for index, char in enumerate(str):
        tempStr = str
        tempStr = tempStr.replace(char, '', 1)
        if not tempStr.__contains__(char):
            return index
    return -1


def generateMatchingParenthesis(n: int):
    return True