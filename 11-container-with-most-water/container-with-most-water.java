class Solution {
    public int maxArea(int[] heights) {
        int left  = 0; 
        int right = heights.length - 1;
        int maxArea = 0;
        int highestLeft = heights[left];

        while(left < right){
            int wide = right - left;
            int height = Math.min(heights[left], heights[right]);
            int area = wide * height;

            // System.out.printf("left=%d; right=%d, %d\n",left, right, wide * height);
            if( area > maxArea){
                maxArea = height * wide;
            } 

            if (heights[left] < heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }


        return maxArea;
    }
}