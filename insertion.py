A = []
x=5
for v in range(x):
    A.append(int(input('enter a number: ')))
print(A)

#insertion sort

def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i=j-1
        while(i>=0 and A[i]>key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key


insertionSort(A) #function call

print('Sorted array')
print(A)
 
