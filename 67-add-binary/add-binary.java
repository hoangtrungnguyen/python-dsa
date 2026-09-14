class Solution {
    public String addBinary(String input1, String input2) {
        String a, b;
        if (input1.length() > input2.length()) { a = input1; b = input2; }
        else { a = input2; b = input1; }

        int[] bitsA = a.chars().map(c -> c - '0').toArray();
        int[] bitsB = b.chars().map(c -> c - '0').toArray();

        int length = bitsA.length;
        int diff = bitsA.length - bitsB.length;

        int[] result = new int[length + 1];
        int carry = 0;

        for (int i = 0; i < length; i++) {
            int aIndex = length - i - 1;
            int bIndex = aIndex - diff;
            int cur = bitsA[aIndex] + (bIndex >= 0 ? bitsB[bIndex] : 0) + carry;
            result[aIndex + 1] = cur % 2;
            carry = cur / 2;
        }
        result[0] = carry;

        StringBuilder sb = new StringBuilder();
        for (int bit : result) sb.append(bit);
        int start = 0;
        while (start < sb.length() - 1 && sb.charAt(start) == '0') start++;
        return sb.substring(start);
    }
}