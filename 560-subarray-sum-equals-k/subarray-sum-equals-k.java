class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> mapFreq = new HashMap<>();
        mapFreq.put(0,1);
        int count = 0;
        Integer total = 0;
        for(int i = 0; i < nums.length; i++){
            total += nums[i];
            int prefixSum = total - k;
            mapFreq.putIfAbsent(total, 0);
            if (mapFreq.containsKey(prefixSum)){
                count += mapFreq.get(prefixSum);
            }
            mapFreq.put(total, mapFreq.get(total) + 1);   
        }
        return count;
    }
}