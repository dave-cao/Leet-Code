class Solution:
    def replaceElements(self, arr: list):
        largest_number_so_far = 0
        replaced_list = [-1]

        for i in range(len(arr) - 2, -1, -1):
            next_number = arr[i + 1]

            if next_number > largest_number_so_far:
                largest_number_so_far = next_number
                replaced_list.insert(0, largest_number_so_far)
            else:
                replaced_list.insert(0, largest_number_so_far)

        return replaced_list


s = Solution()
print(s.replaceElements([17, 18, 5, 4, 6, 1]))
# Expected output [18, 6, 6, 6, 1, -1]
