class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        reversed = ""
        for i in range(len(s)):
            start = s[i].lower()
            end = s[len(s) - 1 - i].lower()

            if start.isalnum():
                forward += start
            if end.isalnum():
                reversed += end

        return forward == reversed


def main():
    sol = Solution()
    s = "0P"
    print(sol.isPalindrome(s))


if __name__ == "__main__":
    main()
