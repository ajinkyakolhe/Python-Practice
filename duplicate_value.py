# How do you find the duplicate number on a given integer array?

l = [2, 5, 10, 1234, 3, 2, 7, 7]
m,n = [], []
for i in l:
    if i not in m:
        m.append(i)
    else:
        n.append(i)
print("The list of unrepeated elements: ",  m)
print("The list of repeated elements: ",  n)