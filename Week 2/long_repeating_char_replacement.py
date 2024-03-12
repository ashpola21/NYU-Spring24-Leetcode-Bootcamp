class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_len, larCount = 0, 0
        arr = collections.Counter()
        for i in range(len(s)):
            arr[s[i]] += 1
            larCount = max(larCount, arr[s[i]])
            if max_len - larCount >= k:
                arr[s[i-max_len]] -= 1
            else:
                max_len += 1
        return max_len
