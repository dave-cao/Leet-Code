class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                length += 1
            elif length:
                return length

        return length


def main():
    sol = Solution()
    s = "Hello World  "
    print(sol.lengthOfLastWord(s))
    pass


if __name__ == "__main__":
    main()

# Notes

# Start at the last index, work your way backwards
# if you encounter a space, then done.

# edge cases
# 1. if the string has trailing whitespace
