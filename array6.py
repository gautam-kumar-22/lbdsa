"""
Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each testcase contains 3 lines of input. The first line contains an integer N denoting the size of the array.
Then the next line contains N space separated integers forming the array. The third line contains an element X.

Output:
For each testcase, in a new line, print the number of elements which are less than or equal to given element.

Example:
Input:
2
6
1 2 4 5 8 10
9
7
1 2 2 2 5 7 9
2
Output:
5
4

"""


def noOfLessThanEqualElement(arr, n, number):
    total = 0
    for i in range(n):
        total += 1 if arr[i] <= number else 0
    return total


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        number = int(input())
        print(noOfLessThanEqualElement(arr, n, number))











