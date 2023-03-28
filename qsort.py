def quicksort(nums, fst, lst):
   
   i, j = fst, lst
   pivot = nums[random.randint(fst, lst)]
   #print(nums) 
   #print(pivot)
   while i <= j:
       while nums[i] < pivot: i += 1
       while nums[j] > pivot: j -= 1
       if i <= j:
           nums[i], nums[j] = nums[j], nums[i]
           i, j = i + 1, j - 1
   if  fst < j   :
        quicksort(nums, fst, j)
   if  i < lst   :
        quicksort(nums, i, lst)
   
   return nums

 
import random
A = [0]*10
for i in range(len(A)):
    A[i] =random.randint(1,10)
print(A)
print()

B = quicksort(A,0, len(A) - 1)
print(B)



