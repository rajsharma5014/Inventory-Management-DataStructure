#program to find the sum, average, maximum, and minimum element in an array.
arr=[]
num=int(input("Enter the No. element of Array:"))
for i in range(num):
    element=int(input("Enter the element of array:"))
    arr.append(element)
#sum
total=sum(arr)
print("Sum of Element:",total)

#average
avg= total/num
print("Average of element:",avg)

#Maximum and Minimum
maximum=max(arr)
minimum=min(arr)
print("Maximum of element is:",maximum,"& Minimum of element is:",minimum)
