from typing import List
# Sum up to K

# Parameters:
#  arr: List[int]
#  k: int
# return type: bool

def sumUpToK(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False


def firstRepeatingCharacter(str):
    print("hello")
