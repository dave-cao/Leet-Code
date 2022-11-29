class Solution:
    def fib(self, n: int):
        # returns an int

        # how do we update this total number

        # end condition
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n > 1:
            return self.fib(n - 1) + self.fib(n - 2)

    def fib_2(self, n: int):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
            print(a, b)

        return a


s = Solution()
print(s.fib_2(10))
