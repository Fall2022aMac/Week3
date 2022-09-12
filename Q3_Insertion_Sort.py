#Write a Program to sort the array of numbers from lowest number to greatest number using Insertion Sort.

print ('Insertion Sort')
print ('Insertion Sort is a sorting algorithm that builds the final sorted array one item at a time')

#this will print list after each insertion sort function
nums = []
print(end="Enter the Size: ") #user input of numbers to be sorted
numsSize = int(input())
print("Enter " +str(numsSize)+ " Numbers: ") #asking user to enter the requested amount of numbers
for i in range(numsSize):
  nums.append(int(input()))

for i in range(1, numsSize):
  elem = nums[i]
  if elem<nums[i-1]:
    for j in range(i+1):
      if elem<nums[j]:
        index = j
        for k in range(i, j, -1):
          nums[k] = nums[k-1]
        break
  else:
    continue
  nums[index] = elem
  print(end="\nStep " +str(i)+ ": ")
  for j in range(numsSize):
    print(end=str(nums[j]) + " ")

print("\n\nThe New (Sorted) List is: ")
for i in range(numsSize):
  print(end=str(nums[i]) + " ")

print()