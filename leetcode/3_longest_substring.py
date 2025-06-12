from setuptools.windows_support import windows_only


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        char_index: store last seen index
        max_len: longest substring

        start: start of the window
        end: end of the window

        for end in range(len(s)):
            char = s[end]
            if char_index[char] in char_index:
                start = end
            else:
                max_len = max(end - start, max_len)


        :param s:
        :return:
        """
        max_len = 0
        char_index = {}
        start = 0

        for end in range(len(s)):
            char = s[end]
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            else:
                max_len = max(end - start + 1, max_len)

            char_index[char] = end

        print(char_index)
        return max_len



print(Solution().lengthOfLongestSubstring(''))
0
print(Solution().lengthOfLongestSubstring('abcabcbb'))
3
print(Solution().lengthOfLongestSubstring('bbbbb'))
1
print(Solution().lengthOfLongestSubstring('bbc'))
2
print(Solution().lengthOfLongestSubstring('dvdfa'))
# 4

print(Solution().lengthOfLongestSubstring('bbcc'))
# 2

print(Solution().lengthOfLongestSubstring('abbcc'))
# 2

# print(Solution().lengthOfLongestSubstring('pwwkew'))
# 3


