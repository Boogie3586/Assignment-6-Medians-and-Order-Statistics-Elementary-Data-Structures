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

##🔹 Part 2: Elementary Data Structures
✅ Files
part2_data_structures/array_matrix.py: Array operations (insert, delete, access)

part2_data_structures/stack_queue.py: Stack and Queue using arrays

part2_data_structures/linked_list.py: Singly linked list (insert, delete, traverse)

### 🚀 Usage
```python
# Array
from array_matrix import Array
arr = Array()
arr.insert(0, 10)
print(arr.access(0))  # 10

# Stack
from stack_queue import Stack
s = Stack()
s.push(5)
print(s.peek())  # 5

# Queue
from stack_queue import Queue
q = Queue()
q.enqueue(10)
print(q.dequeue())  # 10

# Linked List
from linked_list import LinkedList
ll = LinkedList()
ll.insert_back(1)
ll.insert_back(2)
ll.traverse()  # 1 -> 2 -> None
📊 Performance & Analysis
See the report/assignment6_report.pdf for:

Theoretical time & space complexity

Empirical comparisons between deterministic and randomized selection

Real-world applications of data structures

## 📁 Directory Structure

assignment6/
├── part1_selection_algorithms/
│   ├── deterministic_selection.py
│   ├── randomized_selection.py
│
├── part2_data_structures/
│   ├── array_matrix.py
│   ├── stack_queue.py
│   ├── linked_list.py
│
├── report/
│   ├── assignment6_report.pdf
│
├── README.md

##✅ How to Run
Clone the repository:

git clone https://github.com/yourusername/assignment6.git
cd assignment6
Run any of the Python files:


python part1_selection_algorithms/deterministic_selection.py
Install any needed packages (e.g., for graphing):

pip install matplotlib
