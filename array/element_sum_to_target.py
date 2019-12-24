"""
Given a list, have to find out the elements whose sum will be equal to target.

Input:
a = [2, 3, 6, 4, 8, 9]
target = 14

Output:
[6, 8]

"""


def find_sum_element(arr, target):
    for i in arr:
        diff = target - i
        if diff in arr:
            return [i, diff] if diff in arr else []


if __name__ == "__main__":
    a = [2, 3, 6, 4, 8, 9]
    target = 20
    print(find_sum_element(a, target))
