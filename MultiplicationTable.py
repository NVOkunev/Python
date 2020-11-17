#!/usr/bin/env python
dimension = 9 # The number of rows or columns in multiplication table

for row in range(1, dimension + 1):
    for column in range(1, dimension + 1):
        print(row * column, end='\t')
    print()
