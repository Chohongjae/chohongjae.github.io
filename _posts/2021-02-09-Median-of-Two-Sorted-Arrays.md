---
title: "Median of Two Sorted Arrays"
categories: 
  - Algorithm
last_modified_at: 2021-02-09T23:00:00+09:00
---

- [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)

```python
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        data = sorted(nums1 + nums2)
        n = len(data)
        if n == 0:
            raise Exception("no median for empty data")
        if n % 2 == 1:
            return data[n // 2]
        else:
            i = n // 2
            return (data[i - 1] + data[i]) / 2


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 1]))  # 0
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
    print(Solution().findMedianSortedArrays([1, 3], [2, 7]))  # 2.5
```