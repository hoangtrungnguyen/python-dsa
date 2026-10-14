class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> mapFreq = new HashMap<>();
        mapFreq.put(0,1);
        int count = 0;
        Integer prefixSum = 0;
        for(int i = 0; i < nums.length; i++){
            prefixSum += nums[i]; // prefixSum
            int targetKey = prefixSum - k;  
            mapFreq.putIfAbsent(prefixSum, 0);
            if (mapFreq.containsKey(targetKey)){
                count += mapFreq.get(targetKey);
            }
            mapFreq.put(prefixSum, mapFreq.get(prefixSum) + 1);   
        }
        return count;
    }
}