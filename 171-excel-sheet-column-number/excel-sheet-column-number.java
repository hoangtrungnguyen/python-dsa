class Solution {
    public int titleToNumber(String columnTitle) {
        int number = 0;
        for(char order : columnTitle.toCharArray()){
            // System.out.println(chr);
            int curr = (int) order - 65 + 1;
            number = number * 26;
            number = number + curr;
        } 

        return number;
    }
}