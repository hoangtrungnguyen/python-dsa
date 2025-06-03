class Solution {

    private int getNextNumber(int number){
        int output = 0;
        while(number > 0){
            int digit = number % 10;
            output += digit * digit;
            number /= 10;
        }
        return output;
    }

    public boolean isHappy(int n) {
        if( n <= 0){
            return false;
        }
        if( n == 1){
            return true;
        }

        int slow = n;
        int fast = n;

        do {
            slow = getNextNumber(slow);
            fast = getNextNumber(getNextNumber(fast));
            if( fast == 1 ){
                return true;
            } 
        } while ( slow != fast);

        return false;
    }
}