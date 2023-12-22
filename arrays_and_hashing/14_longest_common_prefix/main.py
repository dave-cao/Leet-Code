class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # we begin by comparing the first word
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            current_string = strs[i]
            common = get_common(common_prefix, current_string)
            common_prefix = common

            # reduces runtime
            if common_prefix == "":
                return common_prefix

        return common_prefix


def get_common(word1, word2):

    # get the smaller word
    if len(word2) < len(word1):
        word1, word2 = word2, word1

    prefix = ""
    for i in range(len(word1)):
        word1_char = word1[i]
        word2_char = word2[i]

        if word1_char != word2_char:
            break
        else:
            prefix += word1_char

    return prefix


def main():
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    sol.longestCommonPrefix(strs)


if __name__ == "__main__":
    main()

# Idea 1
# Brute Force
# - for every word
# - for every char in the word
# - have a variable keep track of the common words

# The longest prefix we can have is the smallest word

# Idea 2
# O(n)
# - we compare the first word with the second word and get an output (prefix)
# - compare that output with the third word and update the output
# - compare that output with the fourth word and update the output
# - compare that output with the fifth word and update the output

# - if the prefix is empty, then return the empty prefix
