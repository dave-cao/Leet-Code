class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        print(str)

        number_string = ""
        number = 0
        is_number = True
        word = ""
        word_index = 0
        words = []
        for char in str:

            if char == "#" and is_number:
                is_number = False
                number = int(number_string)
                number_string = ""
                continue
            elif is_number:
                number_string += char
                continue

            # start of word matching
            if not is_number:
                word += char
                word_index += 1

                if word_index == number:
                    words.append(word)
                    is_number = True
                    word_index = 0
                    word = ""

        print(words)


def main():

    input = ["lint:sdfasdf", "###code", "asdfal:::;ove", "you"]
    sol = Solution()
    encoded = sol.encode(input)
    decoded = sol.decode(encoded)
    print(decoded)


if __name__ == "__main__":
    main()
