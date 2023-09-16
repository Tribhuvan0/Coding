class Solution {
    public boolean checkString(String s) {
        int idx = 0;
        int cnt = 0;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i)=='b'){
                idx = i;
                cnt++;
                break;
            }
        }
        if(cnt==0){//if no 'b' exists in the string then return true
            return true;
        }
        for(int i = idx; i<s.length();i++){
            if(s.charAt(i)=='a'){
                return false;
            }
        }
        return true;
        
    }
}