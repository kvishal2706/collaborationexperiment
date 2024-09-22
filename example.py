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
    return arr

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# --------------------------------------------------------------
# author @Abhishikt
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


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
    return arr

# --------------------------------------------------------------
#  author @Geeta
def binary_search_iterative(arr, target):
    arr.sort()
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
    return arr


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
    return arr
    
# --------------------------------------------------------------
#  author @Nupur - Code for Heap Sort Algorithm
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


#  author @Vishal - # Driver code with menu-based interface
def main():
    while True:
        print("\n--- Menu ---")
        print("Press 1 for Sorting Algorithms")
        print("Press 2 for Searching Algorithms")
        print("Press 0 to Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting...")
            break

        # Taking array input
        n = int(input("Enter the size of the array: "))
        arr = []
        print("Input the array elements one by one (press enter after each):")

        for i in range(n):
            arr.append(int(input()))

        if choice == 1:
            print("\n--- Sorting Algorithms ---")
            print("1. Bubble Sort")
            print("2. Insertion Sort")
            print("3. Selection Sort")
            print("4. Merge Sort")
            print("5. Quick Sort")
            print("6. Radix Sort")
            print("7. Heap Sort")
            algo_choice = int(input("Choose a sorting algorithm: "))

            if algo_choice == 1:
                print("Bubble Sort Result:")
                arr = bubble_sort(arr)
                printArray(arr)
            elif algo_choice == 2:
                print("Insertion Sort Result:")
                arr = insertionSort(arr)
                printArray(arr)
            elif algo_choice == 3:
                print("Selection Sort Result:")
                arr = selectionSort(arr)
                printArray(arr)
            elif algo_choice == 4:
                print("Merge Sort Result:")
                arr = merge_sort(arr)
                printArray(arr)
            elif algo_choice == 5:
                print("Quick Sort Result:")
                arr = quick_sort(arr, 0, len(arr) - 1)
                printArray(arr)
            elif algo_choice == 6:
                print("Radix Sort Result:")
                arr = radix_sort(arr)
                printArray(arr)
            elif algo_choice == 7:
                print("Heap Sort Result:")
                arr = heap_sort(arr)
                printArray(arr)
            else:
                print("Invalid sorting choice")

        elif choice == 2:
            print("\n--- Searching Algorithms ---")
            print("1. Linear Search")
            print("2. Binary Search (Iterative)")
            algo_choice = int(input("Choose a searching algorithm: "))
            target = int(input("Enter the target element to search: "))

            if algo_choice == 1:
                result = linearSearch(arr, target)
                print(result)
            elif algo_choice == 2:
                # Sorting the array first for binary search
                arr.sort()
                result = binary_search_iterative(arr, target)
                if result != -1:
                    print(f"Element {target} found at index {result}")
                else:
                    print(f"Element {target} not found")
            else:
                print("Invalid searching choice")

        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()