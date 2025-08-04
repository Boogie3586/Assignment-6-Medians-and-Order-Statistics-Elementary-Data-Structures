# Assignment 6: Medians and Order Statistics & Elementary Data Structures

This repository contains Python implementations and analyses for two major topics in algorithm design and data structures:

- **Part 1:** Selection Algorithms (Deterministic and Randomized)
- **Part 2:** Elementary Data Structures (Array, Stack, Queue, Linked List)

---

## 🔹 Part 1: Selection Algorithms

### ✅ Files
- `part1_selection_algorithms/deterministic_selection.py`: Median of Medians algorithm (worst-case linear time)
- `part1_selection_algorithms/randomized_selection.py`: Randomized Quickselect algorithm (expected linear time)

### 🚀 Usage
```python
from deterministic_selection import median_of_medians
from randomized_selection import quickselect

arr = [3, 1, 5, 2, 4, 6]
k = 2  # Find 3rd smallest element (0-indexed)

print("Deterministic:", median_of_medians(arr[:], k))
print("Randomized:", quickselect(arr[:], k))
