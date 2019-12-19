"""
A and B are good friend and programmers. They are always in a healthy competition with each other.
They decide to judge the best among them by competing.
They do so by comparing their three skills as per their values. Please help them doing so as they are busy.

Set for A are like [a1, a2, a3]
Set for B are like [b1, b2, b3]

Compare ith skill of A with ith skill of B
if a[i] > b[i] , A's score increases by 1
if a[i] < b[i] , B's score increases by 1

Input :
The first line of input contains an integer T denoting the test cases.
For each test case there will be two lines.
The first line contains the skills of A and the second line contains the skills of B

Output :
For each test case in a new line print the score of A and B separated by space.

Example:
Input :
2
4 2 7
5 6 3
4 2 7
5 2 8

Output :
1 2
0 2

"""


def checkBetterFriend(A, B):
    a_total = 0
    b_total = 0
    for i in range(len(A)):
        if A[i] > B[i]:
            a_total += 1
        if A[i] < B[i]:
            b_total += 1
    return "{a_total} {b_total}".format(a_total=a_total, b_total=b_total)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(checkBetterFriend(A, B))
