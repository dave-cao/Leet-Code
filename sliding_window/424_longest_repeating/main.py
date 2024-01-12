class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # initalize a map that counts letters
        count = {}

        left = 0
        max_count = 0

        # go through every letter
        for r in range(len(s)):
            # add each letter to our map
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            max_count = max(max_count, r - left + 1)

        return max_count


def main():
    sol = Solution()
    s = "AABABBA"
    k = 1
    sol.characterReplacement(s, k)


if __name__ == "__main__":
    main()
