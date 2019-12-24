"""
Given a non-empty sequence of characters, return true if sequence is Binary, else return false

Input:

The task is to complete the method that takes a string as argument.
We should not read any input from stdin/console. There are multiple test cases.
For each test case, this method will be called individually.

Output:
Your function should return true str is binary, else false

Example:

Input:
2
101
75

Output:
1
0
"""

# Return true if str is binary, else false


def isBinary(str):
    #code here
    isBinary = True
    for i in str:
        if int(i) > 1:
            isBinary = False
            break
    return isBinary


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print(1)
        else:
            print(0)