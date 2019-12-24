"""
Given an array of distinct elements. Your task is to find the third largest element in it.
You have to complete the function thirdLargest which takes two argument.
The first argument is the array a[] and the second argument is the size of the array (n). T
he function returns an integer denoting the third largest element in the array a[].
The function should return -1 if there are less than 3 elements in input.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. The first line of each test case is N, size of array.
The second line of each test case contains N space separated values of the array a[].

Output:
Output for each test case will be  the third largest element of the array .

Example(To be used for only expected output):
Input:
1
5
2 4 1 3 5

Output:
3

"""

''' This is a function problem.You only need to complete the function given below '''
# You are required to complete this method
# Just Return 3rd Largets integer from the list
# arr Integer List, n Size of the List
# You may use module's


def thirdLargest(arr, n):
    arr.sort()
    return -1 if n < 3 else arr[-3]

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(thirdLargest(arr, n))