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
            final char a = s.charAt(i);
            final char b = t.charAt(i);
            if(!dict.containsKey(a)){
                if(reversedDict.containsKey(b)){
                    return false;
                }
                dict.put(a,b);
                reversedDict.put(b, a);
            } else {
                if(dict.get(a) != b){
                    return false;
                } 
            }
        }

        return true;
    }
}