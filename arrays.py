def list_has(my_list, number):
    for i in range(0, len(my_list)):
        if my_list[i] == number:
            return True
    return False


def shift_right(my_list):
    temp = my_list[len(my_list) - 1]
    for i in range(len(my_list)- 1, 0, -1):
        my_list[i] = my_list[i - 1]
    my_list[0] = temp


def print_table(table):
    for i in range(0, len(table)):
        print(*table[i])


# list, array, vectors

# 1: len(my_list)
# 2: my_list.append()
# 3: my_list.pop()

# example 1: (get n numbers)
# my_list = []
# n = int(input())
# for i in range(0, n):
#     number = int(input())
#     my_list.append(number)

# my_list = [2, 3, 1, 4]
#            0, 1, 2, 3, ...
# my_list[2] += 1

# shift list to the right
# [1, 2, 3] --> [2, 3, 1]

# 2D lists
# n rows
# m colmuns
# n * m

table = [[1, 0, 1], [1, 1, 1], [0, 0, 1]]

print_table(table)