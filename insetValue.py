#program to insert an element at a specified position in an array
arr=[]
num=int(input("Enter the no. of element of Array:"))

for i in range(num):
    element=int(input("Enter the element of array:"))
    arr.append(element)

index=int(input("Enter the postion of element"))
element=int(input("Enter the element to insert:"))
arr.insert(index,element)

print("Array after insertion:",arr)
