# You are tasked with searching about three sorting algorithms , understand them and how they work . Then , write a program that has the three algorithms implemented with the user entering the list and choosing which sorting algorithm they want to use
#The program stops when the user wants it to stop .
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Main program
while True:
    print("Enter a list of numbers: ")
    user_input = input()
    try:
        numbers = [int(num) for num in user_input.split()]
        print("Choose a sorting algorithm:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Selection Sort")
        choice = int(input())

        if choice == 1:
            sorted_numbers = bubble_sort(numbers)
        elif choice == 2:
            sorted_numbers = insertion_sort(numbers)
        elif choice == 3:
            sorted_numbers = selection_sort(numbers)
        else:
            print("Invalid choice!")
            continue

        print("Sorted list:", sorted_numbers)
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers.")
