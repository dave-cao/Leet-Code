class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1, s2 = [*s1], [*s2]
        s1.sort()

        left, right = 0, len(s1) - 1
        while right < len(s2):
            window = (s2[left:right + 1])
            window.sort()

            if s1 == window:
                return True

            left += 1
            right += 1

        return False


def main():
    sol = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    print(sol.checkInclusion(s1, s2))

    pass


if __name__ == "__main__":
    main()
