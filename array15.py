"""
Remove all characters from an alphanumeric string.

Input:
The first line of the input contains T denoting the number of testcases.
First line of each test case will be an alphanumeric string.

Output:
 For each test case output will be a numeric string after removing all the characters.

Constraints:
1 <= T <= 30
1 <= size of string <= 100

Example:

Input:
1
AA123BB4

Output:
1234
"""


def removeCharacter(alphanumeric):
    alphanumeric = list(alphanumeric)
    for i in range(len(alphanumeric)):
        if alphanumeric[i].isalpha():
            alphanumeric[i] = ""
    return "".join(alphanumeric)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        alphanumeric = input()
        print(removeCharacter(alphanumeric))
