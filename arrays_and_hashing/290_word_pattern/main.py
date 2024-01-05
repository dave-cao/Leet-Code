class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # match each letter to a different word
        s = s.split(" ")

        # pattern and s have to be same length for anything to be true
        if len(pattern) != len(s):
            return False

        map = {}
        for i, letter in enumerate(pattern):
            if s[i] not in map.values() and letter not in map:
                map[letter] = s[i]

            # go through pattern, check if corresponding index in s matches
            # if not, then return false
            else:
                if map.get(letter) != s[i]:
                    return False
        return True


def main():
    sol = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(sol.wordPattern(pattern, s))


if __name__ == "__main__":
    main()

# What structures are involved in this problem?
# - map
# - each letter corresponds to a different word
# - with that correspondence, we figure out a pattern

# Approach
# - map each word to a letter
# - see if they follow the same pattern

# I think not in values could be better...
