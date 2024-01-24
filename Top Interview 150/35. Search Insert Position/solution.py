class Solution {
    public int searchInsert(int[] nums, int target) {
        int res = 0; 
        for (int i = 0; i < nums.length; i++) {
            if (target == nums[i]) {
                res = i; 
                break;  
            } else if (target < nums[i]) {
                res = i; 
                break; 
            } else if (i == nums.length - 1) {
                res = nums.length;  
                break; 
            }
        } 

        return res; 

    }
}
