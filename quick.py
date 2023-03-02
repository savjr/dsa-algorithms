
#partition function

A=[]




for v in range(5):
    A.append(int(input('Enter a number :')))
print(A)

n=len(A)#ending index value
p=0#starting index value
r=n-1#array starts with 0

def partition(A,p,r):
    x = A[r]
    i=p-1

    for j in range(p,r):
        if(A[j] <= x):
            i = i+1
            temp1 = A[i]
            A[i] = A[j]
            A[j] = temp1
    temp2 = A[i+1]
    A[i+1] = A[r]
    A[r] = temp2
    return i+1

#m = partition(A,p,r)
#print(m)

def QuickSort(A,p,r):
    if(p<=r):
        q = partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)


QuickSort(A,p,r)
print('Sorted array')
print(A) 

    
    
