class Solution {
    public boolean isPalindrome(String word) {
        int i = 0, j = word.length() - 1;
        while (i < j) {
            char a = Character.toLowerCase(word.charAt(i));
            char b = Character.toLowerCase(word.charAt(j));
            if (!isAlnum(a)) {
                i++;
            } else if (!isAlnum(b)) {
                j--;
            } else if (a != b) {
                return false;
            } else {
                i++;
                j--;
            }
        }
        return true;
    }

    private boolean isAlnum(char c) {
        return (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
}