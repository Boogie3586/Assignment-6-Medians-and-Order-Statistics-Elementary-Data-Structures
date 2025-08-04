# 📘 Assignment 6: Medians and Order Statistics & Elementary Data Structures

This repository contains Python implementations and analyses for two major areas of algorithm design:

- 🧮 **Part 1: Selection Algorithms (Order Statistics)**
- 🧱 **Part 2: Elementary Data Structures**

The goal is to implement these from scratch, analyze their time/space complexity, and discuss real-world applications.

---

## 📂 Repository Structure

assignment6/
├── part1_selection_algorithms/
│ ├── deterministic_selection.py # Median of Medians Algorithm
│ ├── randomized_selection.py # Randomized Quickselect Algorithm
│
├── part2_data_structures/
│ ├── array_matrix.py # Array and Matrix Operations
│ ├── stack_queue.py # Stack and Queue Implementations
│ ├── linked_list.py # Singly Linked List
│
├── report/
│ └── assignment6_report.pdf # Final analysis and discussion report
│
├── README.md # Project documentation

---

## 🧮 Part 1: Selection Algorithms

### 🔍 Overview

This part implements two algorithms for computing the \(k^{th}\) smallest element in an unsorted list:

- **Deterministic Selection (Median of Medians):** Guarantees \(O(n)\) worst-case time  
- **Randomized Quickselect:** Achieves \(O(n)\) expected time but can degrade to \(O(n^2)\) in rare cases  

### 📄 Files

- `part1_selection_algorithms/deterministic_selection.py`  
- `part1_selection_algorithms/randomized_selection.py`  

### 🧪 Example Usage

`from deterministic_selection import median_of_medians
from randomized_selection import quickselect
arr = [7, 2, 9, 1, 5, 6, 8]
k = 3  # Looking for the 4th smallest element (0-based)
print("Deterministic:", median_of_medians(arr[:], k))
print("Randomized:", quickselect(arr[:], k))`

## 🧱 Part 2: Elementary Data Structures

### 🔍 Overview

This part focuses on building common data structures from scratch to understand their internal workings and performance characteristics.

### 📄 Files
-`part2_data_structures/array_matrix.py`

-`part2_data_structures/stack_queue.py`

-`part2_data_structures/linked_list.py`

### 🧪 Example Usage

# Array
`from array_matrix import Array
arr = Array()
arr.insert(0, 42)
print(arr.access(0))  # Output: 42
`
# Stack
`from stack_queue import Stack
s = Stack()
s.push(10)
print(s.pop())  # Output: 10
`
# Queue
`from stack_queue import Queue
q = Queue()
q.enqueue(15)
print(q.dequeue())  # Output: 15
`
# Linked List
`from linked_list import LinkedList
ll = LinkedList()
ll.insert_back(1)
ll.insert_back(2)
ll.traverse()  # Output: 1 -> 2 -> None`
