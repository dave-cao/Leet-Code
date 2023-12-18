class Solution:
    def lengthOfLastWord(self, s: str):
        return len(s.split()[-1])

    def length_part2(self, s: str):
        count = 0
        for i in range(len(s) - 1, -1, -1):

            if s[i] != " ":
                count += 1
            elif count:
                return count


s = Solution()
print(s.length_part2("   fly me   to   the moon  "))
