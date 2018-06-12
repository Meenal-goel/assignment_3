#1.Create a list with user defined inputs

ip1=input("enter the first element:" )
ip2=input("enter the second element:")
ip3=input("enter the third element:")
ip4=input("enter the fourth element:")
ip5=input("enter the fifth element:")

check_list1=[ip1, ip2, ip3, ip4, ip5]
print(check_list1)
print("\n")

#2.add the list['google', 'apple', 'facebook', 'microsoft', 'tesla'] to the list created above

check_list2=['google', 'apple', 'facebook', 'microsoft', 'tesla']
print("The new list is:" ,check_list1+check_list2)
print("\n")

#3.count the number of times an object occurs in a list

check_list3=['m','e','e','n','a','l','g','o','e','l']
print("the count of m is : " ,check_list3.count('m'))
print("the count of e is : " ,check_list3.count('e'))
print("\n")

#4.create a list with numbers and sort it in ascending order

num_list=[5,10,2,1,10,3]
num_list.sort()
print(num_list)
print("\n")

#5.Given are two one-dimensional arrays A and B which are sorted in ascending order.Write a program to merge them into a single sorted array C that contain every item from arrays A and B,in ascending order.


ar_A=[1,5,10,25]
ar_B=[12,52,77,85]
ar_C=(ar_A+ar_B)
ar_C.sort()
print("the sorted array C is:",ar_C)
print("\n")


#6.Implement stack and queue using lists

#stack implementation
stack=[]
#started pushing elements in stack
print("Stack with elements look like:")
stack.append("maruti suzuki")
stack.append("nano")
stack.append("wagonR")
stack.append("honda city")
print(stack)
#popping elements from stack
print("As per stack LIFO property-")
print("first element popped from stack is:",stack.pop())
print("updated stack:" ,stack)
print("second element popped from stack is :",stack.pop())
print("updated stack:",stack)
print("\n")

#queue implementation
queue=[]
#started pushing elements in queue
print("queue with elements looks like:")
queue.append("laptop")
queue.append("mobile")
queue.append("notebooks")
queue.append("tabs")
print(queue)
#popping elements from queue
print("As per queue FIFO property-")
print("first element popped from queue is:",queue.pop(0))
print("updated queue",queue)
print("second element popped from queue is:",queue.pop(0))
print("updated queue:",queue)
print("\n")

#7.optional question:count even and odd numbers in that list
numb = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
odd = 0
even = 0
for i in numb:
     if not i % 2:
        even+=1
     else:
        odd+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)


