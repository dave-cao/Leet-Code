class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if empty string, then there is no max count
        if not s:
            return 0

        # pointers
        left_index = 0
        right_index = 1

        # counter variables
        count = 1
        max_count = 1

        # map
        map = {}

        # create two pointers
        while right_index < len(s):
            # if the left and right pointer are not the same
            # then update the right pointer and count by 1
            if s[left_index] != s[right_index] and not map.get(s[right_index]):
                # keep track of letters traversed
                map[s[right_index]] = 1

                count += 1
                right_index += 1

            # otherwise, they are not the same, then update
            # the left pointer and put the right pointer beside the left
            # and reset the count to 0
            else:
                map = {}
                left_index += 1
                right_index = left_index + 1
                count = 1

            # if ever, the count is more then the max count
            # then update the max count
            if count > max_count:
                max_count = count
        return max_count


def main():
    sol = Solution()
    s = "abcabcbb"
    sol.lengthOfLongestSubstring(s)


if __name__ == "__main__":
    main()
