class Solution {
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10; 
//In this solution we check rev at every step, after performing every iteration we check if rev overflows or not

// if temp = rev*10+pop  then it must be rev>= INTMAX/10, that's why we divide it by 10

// if rev> INTMAX/10, then temp = rev*10+pop is guaranteed to overflow

//if rev==INTMAX/10 then temp = rev*10+pop will overflow if and only if pop value>7
            if (rev > Integer.MAX_VALUE/10 || 
                (rev == Integer.MAX_VALUE / 10 && pop > 7)) 
                    return 0;
            if (rev < Integer.MIN_VALUE/10 || 
                (rev == Integer.MIN_VALUE / 10 && pop < -8)) 
                    return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};