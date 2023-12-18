class Solution:
    def replaceElements(self, arr: list):
        # returns another list of integers

        # Think similar to the two sum problem going backgrounds
        # What are we exactly looking for?
        # Looking for a number that is bigger than the current number
        store_number = 0
        replaced_list = [-1]
        for i in range(len(arr) - 2, -1, -1):
            next_number = arr[i + 1]

            # We can't include the current number

            # tracking current largest number
            if next_number > store_number:
                store_number = next_number
                replaced_list.insert(0, store_number)
            else:
                replaced_list.insert(0, store_number)

        return replaced_list


s = Solution()
print(s.replaceElements([19, 18, 5, 4, 6, 1]))
# Expected output [18, 6, 6, 6, -1]
