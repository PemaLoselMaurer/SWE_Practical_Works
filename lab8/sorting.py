import random
import time
from statistics import mean
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)

def quick_sort1(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort1(arr, low, pi - 1)
        quick_sort1(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Test function
test_arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort1(test_arr, 0, len(test_arr) - 1)
print("In Place Quick Sort Results:", test_arr)

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
def hybrid_merge_sort(arr, left, right, threshold=10):
    if left < right:
        if right - left + 1 <= threshold:
            insertion_sort(arr, left, right)
        else:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid, threshold)
            hybrid_merge_sort(arr, mid + 1, right, threshold)
            merge(arr[left:mid + 1], arr[mid + 1:right + 1])  
# Test function
test_arr = [64, 34, 25, 12, 22, 11, 90]
hybrid_merge_sort(test_arr, 0, len(test_arr) - 1)
print("Hybrid Merge Sort Results:", test_arr)

# Compare sorting algorithms
def compare_sorting_algorithms(arr, trials=5):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("In-Place Quick Sort", quick_sort1)
    ]

    performance = {name: [] for name, _ in algorithms}

    for trial in range(trials):
        print(f"Trial {trial + 1}/{trials}")
        for name, func in algorithms:
            arr_copy = arr.copy()
            start_time = time.time()
            if func == insertion_sort:
                insertion_sort(arr_copy, 0, len(arr_copy) - 1) 
            elif func in (quick_sort1, hybrid_merge_sort):
                func(arr_copy, 0, len(arr_copy) - 1)  
            else:
                func(arr_copy) 
            end_time = time.time()
            elapsed_time = end_time - start_time
            performance[name].append(elapsed_time)
            print(f"  {name} took {elapsed_time:.6f} seconds")
    
    # Calculate average times
    average_performance = {name: mean(times) for name, times in performance.items()}
    print("\nAverage Performance over", trials, "trials:")
    for name, avg_time in average_performance.items():
        print(f"{name}: {avg_time:.6f} seconds")
    
    return average_performance

# Visualize the performance using matplotlib
def visualize_performance(performance):
    algorithms = list(performance.keys())
    times = list(performance.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, times, color=['blue', 'orange', 'green', 'red', 'purple'])
    plt.xlabel('Sorting Algorithms')
    plt.ylabel('Average Time (seconds)')
    plt.title('Performance Comparison of Sorting Algorithms')
    plt.ylim(0, max(times) * 1.1)

    # Add the exact time on top of each bar
    for bar, time_val in zip(bars, times):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + max(times)*0.01, f'{time_val:.6f}', 
                 ha='center', va='bottom')
    plt.show()

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]
average_performance = compare_sorting_algorithms(large_arr, trials=5)
visualize_performance(average_performance)
