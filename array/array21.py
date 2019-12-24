"""
1. Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that prod[i] is
equal to the product of all the elements of arr[] except arr[i]. Solve it without division operator and in
O(n).
Example :
arr[] = {10, 3, 5, 6, 2}
prod[] = {180, 600, 360, 300, 900}
"""


def arrayProductConstruction(arr):
    temp = []
    for i in range(len(arr)):
        number = 1
        data = arr[i+1:] + arr[:i]
        for j in data:
            number *= j
        temp.append(number)
    return temp


arr = [10, 3, 5, 6, 2]
print(arrayProductConstruction(arr))
