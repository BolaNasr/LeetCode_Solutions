class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_most_valid = 0
        longest = 0
        last_seen = {}

        for i, letter in enumerate(s):
            if letter in last_seen:
                left_most_valid = max(left_most_valid, last_seen[letter] + 1)
            last_seen[letter] = i

            longest = max(longest, i - left_most_valid + 1)

        return longest
                
            
        
        
