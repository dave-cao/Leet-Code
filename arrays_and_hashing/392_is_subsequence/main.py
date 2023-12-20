class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_index = 0
        t_index = 0

        # stop either when we found a substring, or if we fully explored our string
        while s_index < len(s) and t_index < len(t):

            s_char = s[s_index]
            t_char = t[t_index]

            # if we have a match, look for next character
            if s_char == t_char:
                s_index += 1

            # continuously update t (we want subsequences)
            t_index += 1

        # returns true if all chars have s have been traversed
        return s_index == len(s)


def main():
    sol = Solution()
    s = "axc"
    t = "ahbgdc"
    s = "abc"
    t = "ahbgdc"

    print(sol.isSubsequence(s, t))


if __name__ == "__main__":
    main()

# possible solutions
# first we find if there is any char that matches with the first letter
# of our substring

# from there, we look for the next element in our string
# it doesn't matter if the first element shows up again, because it continues
# as a subsequence still
