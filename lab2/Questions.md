1. What are the advantages and disadvantages of the recursive approach compared to the iterative approach?
=Recursion follows the divide and conquers approach. The time complexity of recursion is higher than Iteration due to the overhead of maintaining the function call stack. Iteration is faster than recursion due to less memory usage. while Iteration follows the sequential execution approach to solve the problem.

Advantages and Disadvantages of Recursive vs. Iterative Approaches

Advantages of Recursive Approach:

Simplicity and Readability: Recursive solutions can be more straightforward and easier to read, especially for problems that naturally fit a recursive structure (e.g., tree traversals, factorial calculations).
Cleaner Code: Recursion often results in less code compared to iteration, as it avoids the need for loops and manual state management.
Divide and Conquer: Many algorithms, such as quicksort and mergesort, benefit from the recursive approach, making it easier to implement divide-and-conquer strategies.
Disadvantages of Recursive Approach:

Performance: Recursive solutions can be less efficient due to overhead from function calls and potential stack overflow issues for deep recursions.
Space Complexity: Each recursive call adds a new layer to the call stack, which can lead to higher memory usage compared to an iterative approach that may only use a fixed amount of space.
Debugging Difficulty: Debugging recursive functions can be more challenging, especially when trying to trace the flow of execution.
Advantages of Iterative Approach:

Efficiency: Iterative solutions can be more efficient in terms of time and space complexity, especially for large datasets.
Control: Iteration allows more control over the loop's state and can be easier to manage for certain problems.
Disadvantages of Iterative Approach:

Complexity: Some problems are less intuitive when implemented iteratively, leading to more complicated code that may be harder to understand.
More Boilerplate Code: Iterative solutions may require more lines of code to handle state management (e.g., using counters, stacks, or queues).

2. How does memoization improve the performance of the recursive function? Are there any drawbacks?
=Memoization is a powerful technique used to improve the efficiency of recursive functions. By storing the results of function calls and reusing when the same inputs occur again, memoization avoids redundant calculations amd speeds up the execution of recursive algorithms.
It reduces redundant computations, improves time complexity, and improves time complexity.

Backdraws....
The back draws are: increased space complexity, overhead of storing results, potential for cache invalidation, and not suitable for all problems.

3. In what scenarios might you prefer to use a generator function over other implementations?
= I would perfer to use when handling large datasets, infinite sequences, simplified code for iteration, state retention and when I don't need random access.

4. How does the space complexity differ between these implementations?
= They differ as :
-Generators handle large datasets or streams of data efficiently, without consuming significant memory.
-Lists require random access to elements and can afford the memory usage.
-Recursive Functions gives clear, concise solution to problems that fit the recursive paradigm, but there is high space usage due to recursion depth and memoization.
They all trade their memory with time for better efficieny or trade time with more momery