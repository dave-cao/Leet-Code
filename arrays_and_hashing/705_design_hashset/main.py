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


def main():
    hash_set = MyHashSet()
    print(hash_set)
    hash_set.add(1)
    print(hash_set)
    hash_set.add(2)
    print(hash_set)
    print(hash_set.contains(1))
    print(hash_set.contains(3))
    hash_set.add(2)
    print(hash_set)
    print(hash_set.contains(2))
    hash_set.remove(2)
    print(hash_set)
    print(hash_set.contains(2))


if __name__ == "__main__":
    main()

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
