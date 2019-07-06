# How do you find the largest and smallest number in an unsorted integer array?
# Method 1
l = [2, 5, 10, 1234, 3, 2, 7, 7]
print(max(l))

# Method 2
l = [2, 5, 10, 1234, 3, 2, 7, 7]
max = l[0]
for i in range(len(l)):
    if l[i] < max:
        pass
    else:
        max = l[i]
print(max)