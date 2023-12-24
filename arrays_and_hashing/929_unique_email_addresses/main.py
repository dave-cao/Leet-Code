class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:

        map = {}
        for mail in emails:
            local, domain = mail.split("@")
            valid_local = local.split("+")[0]

            # get rid of "." in the string
            valid_local = valid_local.replace(".", "")

            filtered_mail = valid_local + "@" + domain
            if not map.get(filtered_mail):
                map[filtered_mail] = None
        return len(map)


def main():
    sol = Solution()
    emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    emails = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
    print(sol.numUniqueEmails(emails))

    pass


if __name__ == "__main__":
    main()

# 1. everything after the @ sign stays the same
# 2. we are focusing on before the @ sign
#   - split the string by @ sign first
# 3. split the string by + and only get preceding
# 4. remove all "." in the string
# remove duplicates
