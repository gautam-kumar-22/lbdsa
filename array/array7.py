"""
Given an array of size N and you have to tell whether the array is perfect or not.
An array is said to be perfect if it's reverse array matches the original array.
If the array is perfect then print "PERFECT" else print "NOT PERFECT".

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case consists of two lines.
First line of each test case contains an integer N (size of the array)and
the second line contains N elements a0,a1,......aN-1 of an array .

Output:
For each test case, print either "PERFECT" or "NOT PERFECT" in new line as your answer.

Example:
Input:
2
5
1 2 3 2 1
5
1 2 3 4 5
Output:
PERFECT
NOT PERFECT

"""


def checkIsArrayPerfect(arr, n):
    return "PERFECT" if arr == arr[::-1] else "NOT PERFECT"


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(checkIsArrayPerfect(arr, n))

