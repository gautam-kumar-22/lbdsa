"""
A list is given and have to count maximum consecutive 1's or 0's.

Input:
1001111100011

Output:
5

Input:
10011111000000011

Output:
7

"""


def count_consecutive(string):
    count = 0
    max = 0
    prev = string[0]
    for i in string:
        if i == prev:
            count += 1
        else:
            prev = i
            if max < count:
                max = count
            count = 1
    return max


if __name__ == "__main__":
    string = "10011111000000011"
    print(count_consecutive(string))
