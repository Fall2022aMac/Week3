#Write a Program to sort the array of numbers from lowest number to greatest number using Bubble Sort.

print ('\n Bubble Sort is a sorting algorithm that repeatedly steps through a list \n of either predefined numbers or a list provided by user.''\n')
print ('Bubble sort is not the most efficient sorting method, it has to exchange items until the final location is known')
print ('\n''Bubble Sort''\n')

#using a nested loop to iterate each element in a given list, the 'if' statement sorts the items in ascending order using Bubble Sort
a = []
number = int(input("Please Enter the Total Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Item : " %i)) #loop for number of elements user asked for
    a.append(value) #appending value to end of unsorted list

def bubble_sort(a):  
    has_swapped = True  
  
    total_iteration = 0  #tracks how many times it goes through the loop
  
    while(has_swapped):  
        has_swapped = False  
        for i in range(len(a) - total_iteration - 1):  
            if a[i] > a[i+1]:  
                # Swap  
                a[i], a[i+1] = a[i+1], a[i]  
                has_swapped = True  
        total_iteration += 1  
    print("The number of iteration: ",total_iteration)  
    return a  
  

print("The unsorted list is: ", a)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(a))  

