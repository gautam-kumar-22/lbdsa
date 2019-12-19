"""
Given a array of length N, at each step it is reduced by 1 element.
In the first step the maximum element would be removed,
while in the second step minimum element of the remaining array would be removed,
in the third step again the maximum and so on.
Continue this till the array contains only 1 element. And print that final element remaining in the array.

Input:
The first line contains a single integer T i.e. the number of test cases.
The first line of each test case consists of a single integer N.
The second and last line of each test case contains the N spaced integers .

Output:
Fore each test case in new line print the final remaining element in the array.

Example:
Input:
2
7
7 8 3 4 2 9 5
8
8 1 2 9 4 3 7 5

Ouput:
5
4

Explanation:
Test Case 1:
In first step '9' would be removed, in 2nd step '2' will be removed,
in third step '8' will be removed and so on. So the last remaining element would be '5'.

"""


def removeMaxandMinElement(arr, n):
    arr.sort()
    index = n//2
    return arr[index] if n%2 != 0 else arr[index-1]


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(removeMaxandMinElement(arr, n))