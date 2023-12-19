---
tag: code_problem
time_elapsed: 47
difficulty: medium
created: 2023-12-14T16:14
updated: 2023-12-18T14:58
---

# 695 - Encode and Decode Strings

**Time Elapsed**: 47 minutes
**Difficulty**: medium

Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Only $39.9 for the "Twitter Comment System Project Practice" within a limited time of 7 days!

WeChat Notes Twitter for more information（WeChat ID jiuzhangfeifei）
Example

Example1

Input: ["lint","code","love","you"]

Output: ["lint","code","love","you"]

Explanation:

One possible encode method is: "lint:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]

Output: ["we", "say", ":", "yes"]

Explanation:

One possible encode method is: "we:;say:;:::;yes"

---

Had to watch the video because I didn't want to make a wechat account and its locked under premium on leetcode. The premise is pretty simple but it takes a while to implement. Basically have a number identifer and a symbol to indicate when to start the decoding process.

## Encode and Decode
When encoding, we want to append the length of the word in the beginning to tell us how long the word is in the decoding process. However, there may be other numbers within our string, so right beside our number, we add a "#" symbol to indicate that before the pound is a number and after it is a string. From there, we can get an answer.
