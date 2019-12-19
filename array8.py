"""
Given a string, remove the vowels from the string and print the string without vowels.

Input:
The first line consists of an integer T i.e number of test cases.
The first and only line of each test case consists of a string s.

Output:
Print the required output.

Example:
Input:
2
welcome to geeksforgeeks
what is your name ?

Output:
wlcm t gksfrgks
wht s yr nm ?

"""


def removeVowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str = list(str)
    for i in range(len(str)):
        if str[i].lower() in vowels:
            str[i] = ""
    return "".join(str)


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print(removeVowels(input()))
