"""
Given a number N. Your task is to check whether it is fascinating or not.
Fascinating Number : When a number( 3 digit or more) is multiplied by 2 and 3 ,
and when both these products are concatenated with the original number,
then it results in all digits from 1 to 9 present exactly once.

Input:
First line contains number of test cases T. Then following T lines contains a positive integer N.

Output:
Print "1" (without quotes) if given number is fascinating else "0" (without quotes) .

Constraints:
1 <= T <= 200
100 <= N <= 107

Example:
Input:
3
192
853

Output:
1
0
Explanation:
Testcase 1: After multiplication with 2 and 3, and concatenating with original number,
number will become 192384576 which contains all digits from 1 to 9.
"""


def isFascinatingNumber(number):
    if len(str(number)) < 3:
        return "Number should be atleast three digits"
    number = "".join([str(number), str(number*2), str(number*3)])
    return "Fascinating" if "123456789" in "".join(sorted(list(number))) else "Not Fascinating"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        number = int(input())
        print(isFascinatingNumber(number))
