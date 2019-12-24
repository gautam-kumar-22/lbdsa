"""
Given a string S , write a program to check if all the characters of the string are same or not.

Input:
The first line of input contains a single integer T which denotes the number of test cases.
Then T test cases follows. First line of each test case contains a string S.

Output:
For each test case print "YES" without quotes if all the characters of the string S are same otherwise print "NO".

Example:
Input:
2
geeks
gggg
Output:
NO
YES

"""


def checkSameString(str):
    return "YES" if str.count(str[0]) == len(str) else "NO"


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print(checkSameString(input()))