"""
Given an array C[], write a program that prints 1 if array is sorted in non-decreasing order, else prints 0.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case there will be two lines. First line contains the size of the array N. Second line contains N space seperated integers of the array C[i].

Output:
Print 1 if array is sorted, else print 0.

Example:
Input
2
5
10 20 30 40 50
6
90 80 100 70 40 30

Output
1
0
"""


def isArraySorted(arr, n):
    return 1 if arr == sorted(a) else 0

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(isArraySorted(arr, n))
