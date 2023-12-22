class Solution {
    public int maxScore(String s) {
        int max = 0; 
        int countLeft = 0; 
        int countRight = (int) s.chars().filter(c -> c == '1').count(); 

        for (int i = 0; i < s.length() - 1; i++) {
            countLeft += (s.charAt(i) == '0') ? 1 : 0;
            countRight -= (s.charAt(i) == '1') ? 1 : 0;
            max = Math.max(max, countLeft + countRight); 
        }

        return max; 
    }
}
