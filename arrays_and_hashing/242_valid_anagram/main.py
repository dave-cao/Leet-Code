class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # use a hashmap to store input

        s_map = self.get_char_count(s)
        t_map = self.get_char_count(t)

        return s_map == t_map

    def get_char_count(self, string: str) -> dict:

        word_map = {}
        for char in string:
            word_map[char] = word_map.get(char, 0) + 1
        return word_map


def main():
    sol = Solution()

    s = "anagram"
    t = "nagaram"

    print(sol.isAnagram(s, t))


if __name__ == "__main__":
    main()
