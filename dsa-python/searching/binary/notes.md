What is Binary Search?
  Binary Search is a searching algorithm that finds a target in a sorted array by repeatedly dividing the search space into half.
Mandatory condition:
 The array must be sorted

Why Binary Search is Faster than Linear Search
    Linear Search → checks one by one → O(n)
    Binary Search → removes half the array each step → O(log n)
        Example:
            100 elements
            Linear → up to 100 checks
            Binary → ~7 checks

Core Idea (MOST IMPORTANT)
    Binary Search always asks one question:
    “Is the target equal, smaller, or greater than the middle element?”
    Based on the answer:
        discard left half
        or discard right half

Steps of Binary Search (MENTAL TEMPLATE)
    Set start = 0, end = n - 1
    Find middle index
    Compare arr[mid] with target
    Adjust start or end
    Repeat until found or search space is empty



Time & Space Complexity
Time Complexity
Case	Time
Best	O(1)
Worst	O(log n)
Average	O(log n)

Why log n?
    Each step halves the search space

Space Complexity
    Iterative version → O(1)
    Recursive version → O(log n) (call stack)