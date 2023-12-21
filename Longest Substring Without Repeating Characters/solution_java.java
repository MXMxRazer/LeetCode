class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int i = 0;
        int j = 0;
        int result = 0;

        while (i < s.length()) {
            if (set.contains(s.charAt(i))) {
                set.remove(s.charAt(j));
                j++;
            } else {
                set.add(s.charAt(i));
                i++;
                
                int size = set.size();
                result = Math.max(result, size);
            }
        }

        return result;
	}
}
