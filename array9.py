"""
Given a string S, the task is to change the string according to the condition;
If the first letter in a string is capital letter then change the full string to capital letters,
else change the full string to small letters.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case contains a string S.

Output:
For each test case, print the changed string in a new line.

Example:
Input:
2
geEkS
FoR
Output:
geeks
FOR

"""


def properString(str):
    return str.upper() if len(str) and str[0].isupper() else str


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print(properString(input()))
