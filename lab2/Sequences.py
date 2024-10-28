#Implement a Recursive Fibonacci Generator
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

#Implement an Iterative Fibonacci Generator
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")

# Compare Performance
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

# Implement a Generator Function for Fibonacci Sequence
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

# Implement Memoization for Recursive Fibonacci
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")
    
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

#Modify the iterative function to return a list of Fibonacci numbers up to n
def fibonacci_up_to_n(n):
    fib_sequence = [0, 1] 
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

#find the index of the first Fibonacci number
def first_fib_exceeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a, b = b, a + b
        index += 1
    return index  

#function that determines Fibonacci number
import math
def is_fibonacci(num):
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s*s == x
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

#function that calculates the ratio between consecutive Fibonacci numbers and observe
def fibonacci_ratios(n):
    a, b = 0, 1
    ratios = []
    for _ in range(n - 1):
        if a == 0:
            ratios.append(None) 
        else:
            ratios.append(b / a)
        a, b =b, a+b
    return ratios

#Testing with n=10
n = 10 

fib_sequence_up_to_n = fibonacci_up_to_n(n)
value_to_exceed = 10
first_fib_exceeding_index = first_fib_exceeding(value_to_exceed)
fib_check_value = 21
is_fib_number = is_fibonacci(fib_check_value)
fib_ratios = fibonacci_ratios(n)

print("Fibonacci sequence up to", n, ":", fib_sequence_up_to_n)
print("Index of the first Fibonacci number exceeding", value_to_exceed, ":", first_fib_exceeding_index)
print("Is", fib_check_value, "a Fibonacci number?", is_fib_number)
print("Fibonacci ratios approaching the golden ratio with", n, "terms:", fib_ratios)