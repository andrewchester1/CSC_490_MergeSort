import timeit
import random

# # Python program for implementation of MergeSort
# def mergeSort(arr):
#     if len(arr) > 1:
#
#         # Finding the mid of the array
#         mid = len(arr) // 2
#
#         # Dividing the array elements
#         L = arr[:mid]
#
#         # into 2 halves
#         R = arr[mid:]
#
#         # Sorting the first half
#         mergeSort(L)
#
#         # Sorting the second half
#         mergeSort(R)
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#
#
# # Code to print the list
#
#
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()
#
#
# # Driver Code
# # if __name__ == '__main__':
# #     arr = [12, 11, 13, 5, 6, 7]
# #     print("Given array is", end="\n")
# #     printList(arr)
# #     mergeSort(arr)
# #     print("Sorted array is: ", end="\n")
# #     printList(arr)
#
# def GenerateArray(size):
#     array = []
#     for i in range(size):
#         array.append(i)
#     random.shuffle(array)
#     return array
#
# def test():
#     arr = GenerateArray(1000)
#     mergeSort(arr)
#
# print(timeit.Timer(test).timeit(number=10))

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