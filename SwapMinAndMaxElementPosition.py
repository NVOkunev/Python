lst = [int(s) for s in input("Enter list of numbers separated by spaces: ").split()]
index_of_min = 0
index_of_max = 0
for i in range(1, len(lst)):
    if lst[i] > lst[index_of_max]:
        index_of_max = i
    if lst[i] < lst[index_of_min]:
        index_of_min = i
lst[index_of_min], lst[index_of_max] = lst[index_of_max], lst[index_of_min]
print("Result list:")
print(' '.join([str(i) for i in lst]))
