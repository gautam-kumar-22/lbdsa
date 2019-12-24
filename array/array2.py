"""
Given a Integer array A[] of n elements. Your task is to complete the function PalinArray.
Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

The first line of input contains an integer denoting the no of test cases.
Then T test cases follow. Each test case contains two lines. The first
line of input contains an integer n denoting the size of the arrays.
In the second line are N space separated values of the array A[].
"""

''' This is a function problem.You only need to complete the function given below '''
# Your task is to complete this function
# Function should return True/False or 1/0


def PalinArray(arr ,n):
    _isPalin = True
    for i in range(n):
        i = str(arr[i])
        rev = i[::-1]
        if i != rev:
            _isPalin = False
            break
    return _isPalin

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
