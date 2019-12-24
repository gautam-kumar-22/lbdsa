"""
A list is given and have to count maximum consecutive 1's.

Input:
1001111100011

Output:
5

Input:
1110011111111100011

Output:
9

"""


def count_consecutive(string):
    count = 0
    maxi = 0
    for i in string:
        if i == '1':
            count += 1
        else:
            count = 0
        if maxi < count:
            maxi = count
    return maxi


if __name__ == "__main__":
    string = "0101010101010101010101010"
    print(count_consecutive(string))

