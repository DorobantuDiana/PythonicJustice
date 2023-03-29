from bigO import BigO
import numpy as np
def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break

data = np.random.randint(-100, 100, size=50)

bubbleSort(data)

print('Sorted Array in Ascending Order:', data)

lib = BigO()
complexity = lib.test(bubbleSort, "sorted")
complexity = lib.test(bubbleSort, "random")
complexity = lib.test(bubbleSort, "reversed")
complexity = lib.test(bubbleSort, "partial")
complexity = lib.test(bubbleSort, "Ksorted")

'''
Output:
    Sorted Array in Ascending Order: [-96 -94 -88 -80 -73 -65 -60 -56 -56 -55 -53 -51 -50 -48 -46 -39 -38 -36
                                      -34 -31 -27 -26 -17 -16 -10  -4   1   4   8   9   9  17  26  45  49  60
                                       62  63  64  66  70  82  82  91  92  92  96  96  96  98]
    Running bubbleSort(sorted array)...
    Completed bubbleSort(sorted array): O(n)
    Running bubbleSort(random array)...
    Completed bubbleSort(random array): O(n^2)
    Running bubbleSort(reversed array)...
    Completed bubbleSort(reversed array): O(n^2)
    Running bubbleSort(partial array)...
    Completed bubbleSort(partial array): O(n^2)
    Running bubbleSort(Ksorted array)...
    Completed bubbleSort(ksorted array): O(nlog(n))
'''