def sort(x):
    for i in range(len(x)-1):
        minpos = i
        for j in range(i,len(x)):
            if x[j] < x[minpos]:
                minpos = j

        temp = x[i]
        x[i] = x[minpos]
        x[minpos] = temp

        print(x)

x= [5,3,8,6,7,2]
sort(x)

print(x)
