class Solution {
    public boolean isPalindrome(String s) {
        String alphas = "";
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if (Character.isLetter(ch)){
                alphas += Character.toString(ch).toLowerCase();
            }else if (this.isDisit(ch)){
                alphas += Character.toString(ch);
            }
        }
        
        for(int i=0;i<(int)(alphas.length()/2);i++){
            if(alphas.charAt(i) != alphas.charAt(alphas.length()-i-1)){
                return false;
            }
        }
        
        return true;
    }
    
    public boolean isDisit(char ch) {
        return '0' <= ch && ch <= '9';
    }
}
