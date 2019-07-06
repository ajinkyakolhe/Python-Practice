# How do you find the missing number in a given integer array of 1 to 100?
f = list(range(0, 100))
f.remove(32)
for k in range(100):
    if k not in f:
        print("This is the missing number:", k)
