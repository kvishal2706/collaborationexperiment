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

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    printArray(arr)
    
    print(linearSearch(arr, 13))
    print(linearSearch(arr, 23))   
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Bubble Sorted array:", sorted_arr) 
