"""
Consider an array with n elements and value of all the elements is zero. We can perform following operations on the array.

 1. Incremental operations: Choose 1 element from the array and increment its value by 1.
 2. Doubling operation: Double the values of all the elements of array.

Given an array of integers of size N. Print the smallest possible number of operations needed to change
the array from all zeros to desired array.


Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is an integer N  where N is the size of array .
The second line of each test case contains N input A[i].

Output:
Print the smallest possible number of the operations needed to change the array from all zeros to desired array.

Example:

Input:
3
3
16 16 16
2
2 3
2
2 1

Output:
7
4
3

Explanation :
In first test case, the output solution looks as follows. First apply an incremental operation to each element.
Then apply the doubling operation four times. Total number of operations is 3+4 = 7

In second test case, to get the target array from {0, 0}, we first increment both elements by 1 (2 operations),
then double the array (1 operation). Finally increment second element (1 more operation)  Total number of operations is 2+1+1 = 4

In third test case , one of the optimal solution is to apply the incremental operation
2 times to first and once on second element.Total number of operations is 1+1+1 = 3
"""


def minimumStepsForArray(arr):
    temp = [0, 0, 0]
    while temp != arr:
        steps = 0
        for i in range(len(arr)):
            while arr[i] != temp[i]:
                if arr[i] % 2 == 0:
                    arr[i] = arr[i]//2
                    steps += 1
                else:
                    arr[i] -= 1
                    steps += 1
            return steps


arr = [16, 16, 16]
print(minimumStepsForArray(arr))
