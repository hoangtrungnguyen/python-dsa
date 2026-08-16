class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = dict()
        for word in strs:
            key = "".join(sorted(word))   # hashable, and sorted() returns a value
            if key not in dictionary:
                dictionary[key] = [word]  # list of originals, not list(word)
            else:
                dictionary[key].append(word)
        return list(dictionary.values())