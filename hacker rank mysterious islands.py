n = int(input())

element_1 = 1
element_2 = 1
element_sum = 1
index = 1

while element_sum < n:
    element_2 += element_1
    element_1 = element_2 - element_1
    element_sum += element_1
    index += 1
print(index)