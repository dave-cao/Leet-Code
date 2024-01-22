---
tag: code_problem
difficulty: medium
time_elapsed: 50
---

# 981 - Time Based Key-Value Store

<https://leetcode.com/problems/time-based-key-value-store/>

## Quick Notes

- Binary search
- Hashmap with list of tuples as values
- use binary search on the get method
- if the timestamp is not in the list, then return the value associated with the largest lesser timestamp. The right index of the binary search will always end with the lesser value!

---

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 

Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Intuitively I understood the assignment. BUT, I didn't read all the constraints. I didn't read that the timestamps were strictly in increasing order. Thus, I SORTED THEM and it always timed out for me.

# Approach
<!-- Describe your approach to solving the problem. -->
Create a hashmap with the value being a list storing (value, timestamp). Then to get the value from the timestamp, use binary search. Also, one of the requirements was that if the timestamp wasn't in the list, then return a smaller timestamp value. The right index of our binary search will always go to the smaller value!

# Complexity
- Time complexity: $O(log(n))$

- Space complexity: $O(n)$

# Code
```python
class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if not self.map.get(key):
            self.map[key] = [(value, timestamp)]
        else:
            self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if self.map.get(key):
            pairs = self.map.get(key)

            # if the timestamp exists, then return the value
            left, right = 0, len(pairs) - 1
            while left <= right:
                mid = (right + left) // 2
                value, mid_time = pairs[mid]

                if mid_time < timestamp:
                    left = mid + 1
                elif mid_time > timestamp:
                    right = mid - 1
                else:
                    # time is equal to our value
                    return value
            # if it does not exist within the list
            # but it larger, then return the value associated with
            # the largest lesser timestamp
            return pairs[right][0] if (pairs[right][1] < timestamp) else ""
        else:
            return ""


```
