import numpy as np
x=input('write the values such as (6738759):')

s=np.array([x[i:i+1] for i in range(0, len(x), 1)])

maxArea=0
area1=0

for c in range(len(x)):
    for j in range(len(x)):

        if int(s[c])>=int(s[j]):

            area1=int(s[j])*abs(c-j)

            if area1>maxArea:
                maxArea=area1

        elif int(s[j])>int(s[c]):

            area1=int(s[c])*abs(c-j)
            if area1>maxArea:
                maxArearea=area1
print(maxArea)