class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # both strings need to be of same length
        if len(s) != len(t):
            return False

        map = {}
        for i, char in enumerate(s):

            # if the char hasn't been mapped yet, map it
            if not map.get(char):

                # so long as the value to be mapped is not already used
                if t[i] not in map.values():
                    map[char] = t[i]

            # return false if the mapped char isn't correct
            if map.get(char, "") != t[i]:
                return False
        return True

    def alternate_solution(self, s: str, t: str) -> bool:
        map_1 = []
        map_2 = []

        for i in s:
            map_1.append(s.index(i))
        for i in t:
            map_2.append(t.index(i))

        # this works because 'index' takes the very first value
        # everytime. Therefore, if there is a discrepency, that means
        # the two strings are not isomorphic

        return map_1 == map_2


def main():
    sol = Solution()
    s = "bbbaaaba"
    t = "aaabbbba"
    s = "egg"
    t = "add"
    print(sol.alternate_solution(s, t))
    pass


if __name__ == "__main__":
    main()

# what is isomorphic?
# a character can map to itself
# we need to preserve the order of the characters
