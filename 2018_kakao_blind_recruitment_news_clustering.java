import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public int solution(String str1, String str2) {
        int answer = 65536;
        ArrayList<String> array1 = this.getComb(str1);
        ArrayList<String> array2 = this.getComb(str2);
        
        HashMap<String, Integer> map1 = new HashMap<String, Integer>();
        HashMap<String, Integer> map2 = new HashMap<String, Integer>();
        
        for(String ch: array1){
            if(!map1.containsKey(ch)) {
                map1.put(ch, 0);
            }
            map1.put(ch, map1.get(ch)+1);
        }
        
        for(String ch: array2){
            if(!map2.containsKey(ch)) map2.put(ch, 0);
            map2.put(ch, map2.get(ch)+1);
        }
        
        int common = 0;
        int sum = 0;
        
        for(String ch: map1.keySet()){
            if(map2.containsKey(ch)){
                common += Math.min(map1.get(ch), map2.get(ch));
                sum += Math.max(map1.get(ch), map2.get(ch));
                map2.remove(ch);
            }else{
                sum += map1.get(ch);
            }
        }
        
        for(String ch: map2.keySet()){
            sum += map2.get(ch);
        }
        
        
        if(sum!=0) {
            answer = (int)Math.floor(65536*((float)common / sum));
        }
        
        return answer;
    }
    
    public ArrayList<String> getComb(String str){
        ArrayList<String> answer = new ArrayList<String>();
        for(int i=0;i<str.length()-1;i++){
            if (this.isAlpha(str.substring(i,i+2))){
                answer.add(str.substring(i,i+2).toLowerCase());
            }
        }
        return answer;
    }
    
    public boolean isAlpha(String str){
        for(int i=0;i<str.length();i++){
            if(!Character.isLetter(str.charAt(i))) return false;
        }
        return true;
    }
}