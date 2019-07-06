# How do you find all pairs of an integer array whose sum is equal to a given number?
import random
l = [2, 5, 10, 4, 3, 2, 7, 7]
m = []
for i in range(50):
    m.append(random.randint(1, 100))
print(m)
sum = int(input(" Enter the value: "))
nl = []
for i in range(len(m)):
    v = m[i]
    if sum - v in m:
        print(v, (sum - v))
        nl.extend([v, (sum - v)])
    else:
        pass
    i+=1
print(set(nl))