---
tag: code_problem
difficulty: easy
time_elapsed: 8
created: 2024-01-10T13:00
updated: 2024-01-10T13:00
---

# 705 - Design HashSet

**Notes**: The neetcode explanation for this didn't make any sense...

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Pretty simple solution this one. Just had to design a hashset

# Approach
<!-- Describe your approach to solving the problem. -->
I started off with the self.contains method. From that, I can reuse it for the other methods.

# Complexity
- Time complexity: $O(n)$ ~ only a single loop is used

- Space complexity: $O(n)$ ~ a single list is used

# Code
```python
class MyHashSet:

    def __init__(self):
        """Everytime we make a hashset, we initialize a list"""
        self.hashset = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            index = self.hashset.index(key)
            self.hashset.pop(index)

    def contains(self, key: int) -> bool:
        """Loops through the hashset, and sees if the key matches any elements
        in the array."""
        for element in self.hashset:
            if key == element:
                return True
        return False

    def __str__(self):
        return str(self.hashset)

```

