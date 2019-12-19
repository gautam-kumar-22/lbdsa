"""
1. You are given an array A of size N. You need to print elements of A in alternate order.
https://practice.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1
The first line of input contains T denoting the number of testcases. T testcases follow.
Each test case contains two lines of input. The first line contains N and the second line contains the elements of the array.
"""
def printAL(arr, n):
    for i in range(0, n, 2):
        print(arr[i])

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        printAL(arr, n)
