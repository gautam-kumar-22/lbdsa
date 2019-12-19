"""
Given n size unsorted array, find its mean and median.
Mean of an array = (sum of all elements) /(number of elements)
Median of a sorted array of size n is defined as below :
It is middle element when n is odd and average of middle two elements when n is even.
"""


def getMeanMedian(arr):
    mean = sum(arr)/len(arr)
    print("Mean of {arr} = {mean}".format(arr=arr, mean=mean))
    arr.sort()
    median = 0
    length = len(arr)
    if len(arr) % 2 == 0:
        median = (arr[length//2-1]+arr[length//2])/2
    else:
        median = arr[length//2]
    print("Median of {arr} = {median}".format(arr=arr, median=median))

arr = [2, 5, 3, 7, 8, 1, 10, 11]
getMeanMedian(arr)