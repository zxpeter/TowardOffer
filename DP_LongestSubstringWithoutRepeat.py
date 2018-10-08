class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        used = {}
        max_length = start = 0
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[s[i]] = i
        
        return max_length
