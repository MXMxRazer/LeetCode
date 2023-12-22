// Dynamic Programming Approach. 

class Solution {
    public int climbStairs(int n) {
        int[] steps = new int[n+1];

        steps[0] = 1; 
        steps[1] = 1;

        for (int i = 2; i <= n; i++) {
            steps[i] = steps[i - 1] + steps[i - 2];
        }

        return steps[n]; 
    }
}

// Optimized 

class Solution {
    public int climbStairs(int n) {
        int x = 1; 
        int y = 1;
        int z = 1;
         
        for (int i = 2; i <= n; i++) {
            z = x + y;
            x = y; 
            y = z; 
        }

        return z; 
    }
}
