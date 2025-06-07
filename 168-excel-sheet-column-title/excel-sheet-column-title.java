class Solution {
    public String convertToTitle(int columnNumber) {
        if(columnNumber <= 0){
            return "";
        }
        final int SIZE = 26;
        StringBuilder resultBuilder = new StringBuilder();

        while(columnNumber > 0){
            int remainder = (columnNumber - 1) % SIZE;
            int quotient = (columnNumber - 1) / SIZE; 
            resultBuilder.append((char) ('A' + remainder));
            columnNumber = quotient;
        }
        
        return resultBuilder.reverse().toString();
    }
}