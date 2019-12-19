"""
Given an array of size N, swap the kth element from beginning with kth element from end.

Input:
The first line of input contains an integer T denoting the number of test cases.
T testcases follow. Each testcase contains 2 lines of input:
The first line contains an integer N, where N is the size of array.
The second line contains N integers(elements of the array) sperated with spaces.

Output:
For each test case, print the modified array.

Example:
Input
1
8 3
1 2 3 4 5 6 7 8
Output
1 2 6 4 5 3 7 8
"""


def swapPositionalElement(n, arr):
    a, b = arr[n-1], arr[-n]
    arr[n-1], arr[-n] = b, a
    return " ".join(list(map(str, arr)))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        _, n = input().split()
        arr = list(map(int, input().split()))
        print(swapPositionalElement(int(n), arr))
