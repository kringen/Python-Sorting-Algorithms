# Python-Sorting-Algorithms
Displays the concept and code behind some of the most famous array sorting algorithms.

##  Bubble Sort
### Iteration 1
Starts at the first element of an array and compares to its neighbor.  If it is bigger, it switches places.  This process is repeated until the next-to-last in the array.
Since the last element in the array is for sure the largest (after iterating through), no point in checking it again, so the "Max" is decremented by 1.
### Iteration 1 ++
This process continues checking the beginning of the array to the "Max" until no more swaps occur.  Once all swaps are done, the list is sorted and we break from the loop.
### Bubble Sort In Action
Here is an example of how an array that has mostly small numbers on the left and mostly large numbers on the right:

```python
arr1 = [3, 2, 6, 4, 9, 4, 3, 7, 8, 5, 3, 5, 78, 54, 102]
```

The number of iterations to sort this is:
```python
passNumber: 1
[2, 3, 4, 6, 4, 3, 7, 8, 5, 3, 5, 9, 54, 78, 102]
passNumber: 2
[2, 3, 4, 4, 3, 6, 7, 5, 3, 5, 8, 9, 54, 78, 102]
passNumber: 3
[2, 3, 4, 3, 4, 6, 5, 3, 5, 7, 8, 9, 54, 78, 102]
passNumber: 4
[2, 3, 3, 4, 4, 5, 3, 5, 6, 7, 8, 9, 54, 78, 102]
passNumber: 5
[2, 3, 3, 4, 4, 3, 5, 5, 6, 7, 8, 9, 54, 78, 102]
passNumber: 6
[2, 3, 3, 4, 3, 4, 5, 5, 6, 7, 8, 9, 54, 78, 102]
passNumber: 7
[2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 54, 78, 102]
passNumber: 8
[2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 54, 78, 102]
```
And here is an example array that is almost reverse sorted:
```python
arr2 = [100, 54, 78, 5, 3, 8, 7, 3, 4, 9, 4, 6, 2, 3]
```
Note that it takes more iterations to sort!
```python
passNumber: 1
[54, 78, 5, 3, 8, 7, 3, 4, 9, 4, 6, 2, 3, 100]
passNumber: 2
[54, 5, 3, 8, 7, 3, 4, 9, 4, 6, 2, 3, 78, 100]
passNumber: 3
[5, 3, 8, 7, 3, 4, 9, 4, 6, 2, 3, 54, 78, 100]
passNumber: 4
[3, 5, 7, 3, 4, 8, 4, 6, 2, 3, 9, 54, 78, 100]
passNumber: 5
[3, 5, 3, 4, 7, 4, 6, 2, 3, 8, 9, 54, 78, 100]
passNumber: 6
[3, 3, 4, 5, 4, 6, 2, 3, 7, 8, 9, 54, 78, 100]
passNumber: 7
[3, 3, 4, 4, 5, 2, 3, 6, 7, 8, 9, 54, 78, 100]
passNumber: 8
[3, 3, 4, 4, 2, 3, 5, 6, 7, 8, 9, 54, 78, 100]
passNumber: 9
[3, 3, 4, 2, 3, 4, 5, 6, 7, 8, 9, 54, 78, 100]
passNumber: 10
[3, 3, 2, 3, 4, 4, 5, 6, 7, 8, 9, 54, 78, 100]
passNumber: 11
[3, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 54, 78, 100]
passNumber: 12
[2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 54, 78, 100]
passNumber: 13
[2, 3, 3, 3, 4, 4, 5, 6, 7, 8, 9, 54, 78, 100]
```
