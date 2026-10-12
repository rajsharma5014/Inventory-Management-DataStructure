#program to count the number of positive, negative, even, and odd elements in an array.
arr=[]
num=int(input("Enter the no. of element of array:"))

for i in range(num):
    element=int(input("Enter the Element of array:"))
    arr.append(element)
#initialize
positive=0
negative=0
even=0
odd=0
#count
for i in arr:
    if i>=0:
        positive+=1
    else:
        negative+=1
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Array:",arr)
print("Positive element.:",positive)
print("Negative element.:",negative)
print("Even Element:",even)
print("Odd Element:",odd)

