
def sort(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if(x[j]>x[j+1]):
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp

x = [5,3,8,6,7,2]

sort(x)

print(x)
