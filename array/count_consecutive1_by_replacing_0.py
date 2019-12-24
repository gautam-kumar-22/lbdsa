"""
A binary string is given and have to count maximum consecutive 1's. You can replace n zeros.

Input:
101111001
n = 1

Output:
6

Explanation:
After replacing n zero, we get 111111001 and here maximum consecutive 1 is 6

"""


def count_consecutive_after_replacing1(string, n):
    temp = []
    for i in range(len(string)):
        if string[i] == '0':
            temp.append(i)
    print(temp)
    print(type(temp))
    arr = [temp[i+1]-temp[i] for i in range(len(temp)-1)] if len(temp) > 1 else [temp[0]]
    return max(arr)-1


if __name__ == "__main__":
    string = "101111001"
    string = "111111101"
    n = 2
    print(count_consecutive_after_replacing1(string, n))

