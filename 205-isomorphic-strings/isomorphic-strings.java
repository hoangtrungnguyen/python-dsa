class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        // char at index in s -> char at index in t
        HashMap<Character,Character> dict = new HashMap<>();
        // char index in t -> chart at index in s
        HashMap<Character,Character> reversedDict = new HashMap<>();

        for(int i = 0; i < s.length(); i ++){
            if(!dict.containsKey(s.charAt(i))){
                if(reversedDict.containsKey(t.charAt(i))){
                    return false;
                }
                dict.put(s.charAt(i),t.charAt(i));
                reversedDict.put(t.charAt(i), s.charAt(i));
            } else {
                if(dict.get(s.charAt(i)) != t.charAt(i)){
                    return false;
                } 
            }
        }

        return true;
    }
}