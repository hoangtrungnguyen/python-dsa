class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // count frequency of each number
        Map<Integer, Integer> mapFreq = new HashMap<>();
        for (int num : nums) {
            mapFreq.merge(num, 1, Integer::sum);
        }

        // bucket sort: index = frequency, value = list of nums with that frequency
        // max possible frequency of any num is nums.length (if all elements are identical)
        // so buckets needs indices 0..nums.length inclusive -> size nums.length + 1
        List<List<Integer>> buckets = new ArrayList<>();
        for (int i = 0; i < nums.length + 1; i++) {
            buckets.add(new ArrayList<>());
        }

        // place each num into its frequency bucket
        for (Map.Entry<Integer, Integer> entry : mapFreq.entrySet()) {
            int freq = entry.getValue();
            buckets.get(freq).add(entry.getKey()); // mutate in place, no need to re-set
        }

        // walk buckets from highest frequency to lowest, collect top k nums
        int[] result = new int[k];
        int idx = 0;
        for (int i = buckets.size() - 1; i >= 0 && idx < k; i--) {
            for (int num : buckets.get(i)) {
                if (idx == k) break;
                result[idx++] = num;
            }
        }

        return result;
    }
}