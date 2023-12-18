
class Solution:
    # two-pointer solution
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            # this method works because it is already sorted
            elif sum < target:
                # if the sum if less then target, increase the increment (this strictly
                # increases the number since it is sorted)
                left += 1
            else:
                # strictly decreases the number
                right -= 1

    # dictionary solution
    def twoSum_two(self, numbers: list[int], target: int) -> list[int]:

        map = {}
        for i, num in enumerate(numbers):
            if num in map:
                return [map.get(num) + 1, i + 1]
            else:
                map[target - num] = i


def main():
    sol = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    numbers = [2, 3, 4]
    target = 6

    print(sol.twoSum(numbers, target))


if __name__ == "__main__":
    main()

# Notes
# Already sorted
