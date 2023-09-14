class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }else if(x==0){
            return true;
        }else{
            return rev(x)==x;
        }
        
        
    }
    public int rev(int x){
        int rem = 0;
        while(x>0){
            int last_dig = x%10;
            rem = rem*10+last_dig;
            x=x/10;
        }
        return rem;
    }
}