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


def main():
    solution = TimeMap()
    solution.set("a", "bar", 1)
    solution.set("x", "b", 3)
    print(solution.map)
    print(solution.get("b", 3))
    solution.set("foo", "bar2", 4)
    print(solution.map)
    print(solution.get("foo", 4))
    print(solution.get("love", 15))
    pass


if __name__ == '__main__':
    main()

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
