#Write a Program to sort the array of numbers from lowest number to greatest number using Selection Sort.

print ('\n''Selection sort finds the smallest number in a list and then subsequently the larger until complete''\n')

print ('------Selection Sort------')

def Selection_Sort(array):
    for i in range(0, len(array) - 1):
        smallest = i #declare the smallest initial value with i
        for j in range(i + 1, len(array)): #inner loop with a loop variable j that counts from i + 1 up to the length of the array – 1
            if array[j] < array[smallest]:
                smallest = j # if elements <j than element at index is smallest thus making smallest = j
        array[i], array[smallest] = array[smallest], array[i] # swap the elements at indexes i and smallest

array = input('Enter the list of numbers (i.e. 5 3 2 9 8): ').split()
array = [int(x) for x in array]
Selection_Sort(array)
print('List after sorting is : ', end='')
print(array)