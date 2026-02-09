### What is Linear Search?

Linear Search is a searching algorithm that checks each element of the array one by one until the target is found or the array ends.

## When do we use Linear Search?

Use Linear Search when:

    The array is unsorted
    The array is small
    Simplicity is more important than speed
    No preprocessing is allowed

## How Linear Search Works (Step-by-Step)
1. Start from index 0
2. Compare current element with target
3. If equal → return index
4. Move to next element
5. If target not found → return -

Time Complexity (Must Know)
Case	Time
Best	O(1)
Average	O(n)
Worst	O(n)

Reason:
    Might need to scan entire array

Space Complexity
O(1)
    (No extra memory used)