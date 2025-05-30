class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> currArray = new ArrayList<>();
        currArray.add(1);
        for ( int i = 0; i < rowIndex; i ++){
            List<Integer> newArray = new ArrayList<>();
            newArray.add(1);
            for(int j = 1; j < currArray.size(); j++){
                newArray.add(currArray.get(j) + currArray.get(j - 1));
            }
            newArray.add(1);
            currArray = newArray;
        }
        return currArray;
    }
}