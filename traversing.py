#program to traverse an array and print each element with its index.

arr=[]
num=int(input("Enter the no. of element of array:"))

for i in range(num):
    element=int(input("Enter the element of Array:"))
    arr.append(element)

print("Element of array with its index are:")
for i in range(num):
    print("Index:",i,"& Element:",arr[i])
    
