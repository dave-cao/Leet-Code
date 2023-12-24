---
tag: code_problem
time_elapsed: 19
difficulty: easy
process: completed
created: 2023-12-24T11:55
updated: 2023-12-24T12:27
---

# 929 - Unique Email Addresses


Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

    For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

    For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

    For example, "m.y+name@email.com" will be forwarded to "my@email.com".

It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

 

Constraints:

    1 <= emails.length <= 100
    1 <= emails[i].length <= 100
    emails[i] consist of lowercase English letters, '+', '.' and '@'.
    Each emails[i] contains exactly one '@' character.
    All local and domain names are non-empty.
    Local names do not start with a '+' character.
    Domain names end with the ".com" suffix.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We just needed to split the email into multiple different parts and then make sure we don't have any duplicates. At the end, we return how many unique identifiers we got.

# Approach
<!-- Describe your approach to solving the problem. -->
I started off with looping through the emails. Then, splitting until we filtered the email into what we wanted. Next, I put the email into a map, and if there was a duplicate, didn't add it in. Finally, we can just return the number of keys in the map. Done.

# Complexity
- Time complexity: $O(n \cdot m)$ ~ $n$ is the number of emails and $m$ is the size of the email itself

- Space complexity: $O(n \cdot m)$ ~ the map stores (worst case) $n$ amount of emails with where each email has an average size of $m$

# Code
```python
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

```


