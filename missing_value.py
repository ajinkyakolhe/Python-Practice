# How do you find the missing number in a given integer array of 1 to 100?
i = input("Enter a number: ")
print("This is input: " + i)
f = list(range(0, 100))
if i not in f:
        print("This is the missing number input:" + i)
