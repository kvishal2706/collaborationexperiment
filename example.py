#  author @mourya - Code for Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# --------------------------------------------------------------
#  author @aayushi
def linearSearch(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return f"Element {x} found at index {i}"
	return f"Element {x} not found"

# --------------------------------------------------------------
#  author @devesh
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# --------------------------------------------------------------
# author @Karan
def partition(arr, low, high):
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()

# --------------------------------------------------------------
#  author @Geeta
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Target not found

# --------------------------------------------------------------
#  author @sujith
def selectionSort(arr):
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of the unsorted array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# --------------------------------------------------------------
#  author @sriram
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def merge_sort_print(arr):
    print("Original array:", arr)
    merge_sort(arr)
    print("Merge Sorted array:", arr)
    

# --------------------------------------------------------------

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    printArray(arr)
    
    print(linearSearch(arr, 13))
    print(linearSearch(arr, 23))    
    
    arr1 = [1,2,45,7,9,4]
    selectionSort(arr1)
    printArray(arr1)

    quick_sort(arr, 0, len(arr) - 1)
    print("\nSorted array using quick-sort is")
    print_array(arr)
      
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Bubble Sorted array:", sorted_arr) 

    arr2 = [38, 27, 43, 3, 9, 82, 10]
    merge_sort_print(arr2)#  author @mourya - Code for Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# --------------------------------------------------------------
#  author @aayushi
def linearSearch(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return f"Element {x} found at index {i}"
	return f"Element {x} not found"

# --------------------------------------------------------------
#  author @devesh
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# --------------------------------------------------------------
# author @Karan
def partition(arr, low, high):
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def print_array(arr):
    for i in arr:
        print(i, end=" ")
    print()
    
# --------------------------------------------------------------
#  author @Geeta
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Target not found

# --------------------------------------------------------------
#  author @sujith
def selectionSort(arr):
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of the unsorted array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# --------------------------------------------------------------
#  author @sriram
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def merge_sort_print(arr):
    print("Original array:", arr)
    merge_sort(arr)
    print("Merge Sorted array:", arr)
    

# --------------------------------------------------------------

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    printArray(arr)
    
    print(linearSearch(arr, 13))
    print(linearSearch(arr, 23))    
    
    arr1 = [1,2,45,7,9,4]
    selectionSort(arr1)
    printArray(arr1)
      
    quick_sort(arr, 0, len(arr) - 1)
    print("\nSorted array using quick-sort is")
    print_array(arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Bubble Sorted array:", sorted_arr) 

    arr2 = [38, 27, 43, 3, 9, 82, 10]
    merge_sort_print(arr2)