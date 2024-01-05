class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # initialize char counter for balloon
        balloon_map = {}
        for char in "balloon":
            balloon_map[char] = balloon_map.get(char, 0) + 1

        # make a character counter for the given word
        map = {}
        for char in text:
            map[char] = map.get(char, 0) + 1

        result = len(text)
        for char in balloon_map:
            # gets the minimum so far
            result = min(result, map[char] // balloon_map[char])
        return result

    def maxNumberOfBalloons_one(self, text: str) -> int:
        # initialize char counter for balloon
        balloon_map = {}
        for char in "balloon":
            balloon_map[char] = balloon_map.get(char, 0) + 1

        # make a character counter for the given word
        map = {}
        for char in text:
            map[char] = map.get(char, 0) + 1

        # continously compare the balloon map with map, subtracting every time
        total = -1
        can_spell_balloon = True
        while can_spell_balloon:
            for char, count in balloon_map.items():
                # if the character exists, then see if we have enought
                if map.get(char):
                    map[char] = map.get(char) - count
                    if map.get(char) < 0:
                        can_spell_balloon = False
                        break
                # if it doesnt' exist, we can't spell balloon anyway
                else:
                    can_spell_balloon = False
                    break
            total += 1
        return total


def main():
    sol = Solution()
    text = "leetcode"
    text = "nlaebolko"
    text = "loonbalxballpoon"
    text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
    print(sol.maxNumberOfBalloons(text))


pass


if __name__ == "__main__":
    main()

# given a string, form as many instances of balloon as possible

# plan
# - we first need to store the characters into map

# 1.
# - we count all characters
# - we continuosly look for balloon characters, and if we dont' get the character
# - then it stops because we can't spell it anymore
