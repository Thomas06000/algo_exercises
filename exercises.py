from typing import List
# Sum up to K

# Parameters:
#  arr: List[int]
#  k: int
# return type: bool

def sumUpToKOLD(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False

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


def generateMatchingParenthesis(n: int):
    return True