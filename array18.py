"""
Given an array A[ ], find maximum and minimum elements from the array.

Input:
The first line of input contains an integer T, denoting the number of testcases.
The description of T testcases follows.
The first line of each testcase contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
For each testcase in a new line, print the maximum and minimum element in a single line with space in between.

Example:
Input:
2
4
5 4 2 1
1
8

Output:
5 1
8 8

Explanation:
Testcase 1:
Maximum element is: 5
Minimum element is: 1

"""


def getMinimumMaximumElement(n, arr):
    return " ".join([str(max(arr)), str(min(arr))])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(getMinimumMaximumElement(n, arr))

