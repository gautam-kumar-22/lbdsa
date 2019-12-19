"""
Given an array of elements. Your task is to find the second maximum element in the array.

Input:
The first line of input contains an integer T which denotes the number of test cases.
Then T test cases follows. First line of each test case contains a
single integer N which denotes the number of elements in the array.
Second line of each test case contains N space separated integers which denotes the elements of the array.
Output:
For each test case in a new line print the second maximum element in the array.
If there does not exist any second largest element, then print -1.


Constraints:
1<=T<=100
2<=n<=1000
1<=a[i]<=106


Example:
Input:
2
5
2 4 5 6 7
6
7 8 2 1 4 3
Output:
6
7
"""


def getSecondMaimumElement(n, arr):
    arr = list(set(arr))
    return sorted(arr)[-2] if len(arr) > 1 else -1


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(getSecondMaimumElement(n, arr))
