# Sum up to K

# Parameters:
#  arr: List[int]
#  k: int
# return type: bool

def sumUpToK(arr, k):
    if not arr or arr.count == 1 or not k:
        return False
    while len(arr) > 1:
        for i, value in enumerate(arr):
            if i == len(arr) - 1:
                arr.pop(0)
                break
            nextIndex = i + 1
            firstValue = arr[0]
            secondValue = arr[nextIndex]
            if firstValue + secondValue == k:
                return True
    return False

    def firstRepeatingCharacter(str):
        print("hello")
