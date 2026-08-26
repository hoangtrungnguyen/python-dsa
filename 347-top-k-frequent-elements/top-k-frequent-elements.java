class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> mapFreq = new HashMap<>(); // map value -> frequencies 
        
        for(int i = 0; i < nums.length; i ++){
            mapFreq.putIfAbsent(nums[i],  0);
            mapFreq.put(nums[i], mapFreq.get(nums[i]) + 1);
        }

        // System.out.println(mapFreq);
        // initialize buckets
        // index of buckets is the frequencies, element of buckets is list of num that have frequencies = index. Buckets length == nums.length because nums can contain only distinct num. 
        List<ArrayList<Integer>> buckets = new ArrayList<>();
        for (int i = 0; i < nums.length + 1; i++) {
            buckets.add(new ArrayList<>());
        }

        // System.out.println(buckets);


        for(Map.Entry<Integer, Integer> entry: mapFreq.entrySet()){
            int freq = entry.getValue();
            ArrayList<Integer> freqNums = buckets.get(freq);
            freqNums.add(entry.getKey());
            buckets.set(freq, freqNums);
        }

        // System.out.println(buckets);

        List<Integer> result = new ArrayList<>();
        for(int i = buckets.size() - 1; i >= 0 ; i --){
       
                for(Integer e : buckets.get(i)){
                    if(result.size() < k){
                        result.add(e);
                    } else {
                        break;
                    }
                }
            
        }

        return result.stream().mapToInt(Integer::intValue).toArray();

    }
}