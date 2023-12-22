class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        # super list
        rows = []
        current_row = [1]
        for i in range(numRows):
            rows.append(current_row)
            current_row = get_next_row(current_row)
        return rows


def get_next_row(row):
    next_row = [1]
    for i in range(len(row) - 1):
        result = row[i] + row[i + 1]
        next_row.append(result)
    next_row.append(1)
    return next_row


def main():
    sol = Solution()
    numRows = 1000
    print(sol.generate(numRows))


if __name__ == "__main__":
    main()
