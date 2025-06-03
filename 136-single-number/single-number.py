class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for e in nums:
            if counter.get(e) is None:
                counter[e] = 0
            else:
                counter[e] = 1
        
        key_found = None # To store the first key found
        for key, value in counter.items():
            if value == 0:
                key_found = key
                break # Stop searching once the first match is found
        return key_found

        