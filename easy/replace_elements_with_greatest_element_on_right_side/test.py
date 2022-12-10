class Solution:
    def replaceElements(self, arr: list):

        largest_number_so_for = 0
        replaced_list = [-1]

        for i in range(len(arr) - 2, -1, -1):

            next_number = arr[i + 1]
            if next_number > largest_number_so_for:
                largest_number_so_for = next_number
                replaced_list.insert(0, largest_number_so_for)
            else:
                replaced_list.insert(0, largest_number_so_for)

        return replaced_list


s = Solution()
print(s.replaceElements([17, 18, 5, 4, 6, 19]))
# Expected output [18, 6, 6, 6, 1, -1]
