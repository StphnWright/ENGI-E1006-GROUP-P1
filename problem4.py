"""
A program to produce a list of the k-smallest
numbers in a given list of numbers.
"""

# Driver program
li = [30, 45, 82, 39, 81, 64, 98, 79, 100, 84]
lowest_k = []
k = 5


# Determines the lowest value in a list and appends it to a new list
def minimum(li):
    min = li[0]
    for i in li:
        if i < min:
            min = i
    li.remove(min)
    lowest_k.append(min)


# We run minimum() k times to fill the new list with k lowest values
for i in range(k):
    minimum(li)

print(lowest_k)
