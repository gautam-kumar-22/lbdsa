"""
Given an Array, Find the maximum sun sub-array

I/P:
a = [1, 2, 5, -7, 1, 2]

O/P:
[1, 2, 5]

Explanation:
sum of sub array [1, 2, 5] is 8 and it is maximum sum of all sub-array of given array.

"""


def get_max_sum_subarray(arr):
    maxi = 0
    element_sum = 0
    main_max = 0
    temp = []
    for i in arr:
        element_sum += i
        print(maxi, element_sum)
        if maxi < element_sum:
            maxi = element_sum
            main_max = maxi
            temp.append(i)
        elif maxi > element_sum:
            element_sum = 0
            # maxi = 0
            temp = []
        # print(maxi, element_sum)
    return main_max, temp


if __name__ == "__main__":
    a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(get_max_sum_subarray(a))
