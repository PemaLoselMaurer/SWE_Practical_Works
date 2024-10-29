def linear_search_indices(arr, target):
    indices = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            indices.append(i) 
    return (indices if indices else -1), comparisons # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result, comparisons = linear_search_indices(test_list, 6)
print(f"Linear Search: Indices of 6 is {result} with {comparisons} comparisons")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result, comparisons = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result} with {comparisons} comparisons")

#jump search algorithm with its comparison
def jump_search(arr, target):
    l = len(arr)
    jump = int(l ** 0.5)
    prev = 0
    compare_count = 0

    if arr[0] > target:
        return -1, compare_count

    # Jump search phase
    while prev < l and arr[min(jump, l) - 1] < target:
        compare_count += 1
        prev = jump
        jump += int(l ** 0.5)
        if prev >= l:
            return -1, compare_count

    # Linear search phase
    while prev < l and arr[prev] < target:
        compare_count += 1
        prev += 1
        if prev == min(jump, l):
            return -1, compare_count

    compare_count += 1
    if prev < l and arr[prev] == target:
        return prev, compare_count
    return -1, compare_count

# Test with a sorted list
test_list = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
index, comparisons = jump_search(test_list, 9)
print(f"Index of target (9) using jump search: {index}")
print(f"Number of comparisons: {comparisons}")

def find_insertion_point(arr, target):
    left, right = 0, len(arr)
    comparisons = 0
    
    while left < right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] < target:
            left = mid + 1  # Move the left pointer to the right
        else:
            right = mid  # Move the right pointer to the left
            
    return left, comparisons  # The insertion point is where left ends up

# Test the function
sorted_list = [1, 3, 5, 7, 9]
target = 6
insertion_point, comparisons = find_insertion_point(sorted_list, target)
print(f"Insertion point for {target} in {sorted_list} is {insertion_point} with {comparisons} comparisons")

import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search_indices(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons} Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

def binary_search_recursive(arr, target, left, right, comparisons = 0):
    if left > right:
        return -1, comparisons
    
    mid = (left + right) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)

# Test the recursive function
result, comparisons = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result} with {comparisons} comparisons")


def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result, comparisons = linear_search_indices(test_list, target)
    print(f"Linear Search: Found at indices {result} with {comparisons} comparisons")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result, comparisons = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result} with {comparisons} comparisons")
    
    # Binary Search (recursive)
    result, comparisons = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result} with {comparisons} comparisons")

    #Intersection point
    result, comparisons = find_insertion_point(sorted_list, target)
    print(f"Insertion point for {target} is {result} with {comparisons} comparisons")
     
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()
