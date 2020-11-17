#!/usr/bin/env python

# Create empty lists for user data and resulting list
lst = []
uniq = []

# User define the number of elements in list
n = int(input("Enter number of elements : "))

# User define the n values of list's elements
for i in range(0, n):
	ele = input()
	lst.append(ele)
print('Initial list is:              {0}'.format(lst))
# Fill addiional list with unique elements of initial list.
for j in lst:
	if j not in uniq:
		uniq.append(j)
print('List with unique elements is: {0}'.format(uniq))
