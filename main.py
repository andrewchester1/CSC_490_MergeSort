import timeit
import random

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        leftIndex = 0
        rightIndex = 0

        mainIndex = 0

        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] <= right[rightIndex]:
                myList[mainIndex] = left[leftIndex]
                leftIndex += 1
            else:
                myList[mainIndex] = right[rightIndex]
                rightIndex += 1
            mainIndex += 1

        while leftIndex < len(left):
            myList[mainIndex] = left[leftIndex]
            leftIndex += 1
            mainIndex += 1

        while rightIndex < len(right):
            myList[mainIndex] = right[rightIndex]
            rightIndex += 1
            mainIndex += 1

def GenerateArray(size):
    array = []
    for i in range(size):
        array.append(i)
    random.shuffle(array)
    return array

def test():
    randmonArray = GenerateArray(1000)
    mergeSort(randmonArray)

print(timeit.Timer(test).timeit(number=10))