class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # we can get the anagram by sorting
        map = {}
        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string not in map:
                map[sorted_string] = [string]
            else:
                map[sorted_string].append(string)

        return list(map.values())

    def groupAnagrams_brute(self, strs: list[str]) -> list[list[str]]:

        counts = [(self.count_letters(string), string)for string in strs]

        found = [string for string in strs]
        anagrams = []
        for q, (count, key) in enumerate(counts):
            row = []
            if key in found:
                row.append(key)
                found.remove(key)
            else:
                continue

            for i in range(q + 1, len(counts)):
                inner_count, inner_key = counts[i]
                if count == inner_count:
                    if inner_key in found:
                        row.append(inner_key)
                        found.remove(inner_key)
            anagrams.append(row)
        return anagrams

    def count_letters(self, string):
        word_map = {}
        for letter in string:
            word_map[letter] = word_map.get(letter, 0) + 1

        return word_map


def main():

    sol = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    (sol.groupAnagrams(strs))

    pass


if __name__ == "__main__":
    main()
