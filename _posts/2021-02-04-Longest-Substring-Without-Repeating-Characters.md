---
title: "Longest Substring Without Repeating Characters - leetcode"
categories: 
  - Algorithm
last_modified_at: 2021-02-04T23:00:00+09:00
---

- [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q = []
        max = 0
        for i in range(len(s)):
            for j in list(s)[i:]:
                if j not in q:
                    q.append(j)
                else:
                    if max < len(q):
                        max = len(q)
                    q = []
                    break
            else:
                if max < len(q):
                    max = len(q)
                q = []
        return max


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("pwwkew"))
```