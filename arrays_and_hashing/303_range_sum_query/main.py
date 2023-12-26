class NumArray:

    def __init__(self, nums: list[int]):
        self.range = nums

    def sumRange(self, left: int, right: int) -> int:

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(left,right)
        total = 0
        for i in range(left, right + 1):
            total += self.range[i]
        return total


def main():
    nums = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    sol = NumArray(nums)
    pass


if __name__ == "__main__":
    main()
