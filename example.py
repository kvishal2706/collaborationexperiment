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
