"""
Given a number N. The task is to complete the function convertFive()
which replace all zeros in the number with 5 and returns the number.
Input:
The first line of input contains an integer T, denoting the number of testcases.
Then T testcases follow. Each testcase contains a single integer N denoting the number.

Output:
The function will return integer where all zero's are converted to 5.
"""


''' This is a function problem.You only need to complete the function given below '''
# function should return an integer
# 3your task is to compplete this function


def convertFive(n):
    return str(n).replace('0', '5')


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(convertFive(n))