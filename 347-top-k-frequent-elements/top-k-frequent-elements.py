class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_freqs = [0] * k          # k largest frequencies, descending
        top_values = [0] * k         # values paired 1:1 with top_freqs
        nums_sorted = sorted(nums)   # groups equal values into runs
        n = len(nums_sorted)

        scan = 0                     # scan position over nums_sorted
        run_length = 0               # length of the current equal-value run

        while scan < n:
            if scan < n - 1 and nums_sorted[scan] == nums_sorted[scan + 1]:
                run_length += 1
            else:
                run_length += 1                       # count the run's last element
                if run_length > top_freqs[-1]:        # beats weakest of current top-k
                    slot = k - 1
                    while slot > 0 and run_length > top_freqs[slot - 1]:
                        top_freqs[slot] = top_freqs[slot - 1]
                        top_values[slot] = top_values[slot - 1]   # key travels with its count
                        slot -= 1
                    top_freqs[slot] = run_length
                    top_values[slot] = nums_sorted[scan]
                run_length = 0
            scan += 1

        return top_values