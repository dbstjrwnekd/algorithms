import java.util.HashMap;

class Solution {
    public int solution(String dartResult) {
        HashMap<Character, Integer> SDT = this.getDefaultSDT();
        int answer = 0;
        int step = 0;
        boolean fin = false;
        String before = "";
        String current = "";
        while (step < dartResult.length()) {
            char ch = dartResult.charAt(step);
            if (this.isDisit(ch)) {
                if (fin) {
                    answer += Integer.parseInt(current);
                    before = current;
                    current = "";
                    fin = false;
                }
                current += ch;
            } else {
                if (SDT.containsKey(ch)) {
                    current = Integer.toString((int) Math.pow(Integer.parseInt(current), SDT.get(ch)));
                    fin = true;
                } else {
                    int next = 0;
                    if (ch == '*') {
                        next = Integer.parseInt(current) * 2;
                        answer += next;
                        if (before != "")
                            answer += Integer.parseInt(before);
                    } else {
                        next = -1 * Integer.parseInt(current);
                        answer += next;
                    }
                    before = Integer.toString(next);
                    current = "";
                    fin = false;
                }
            }
            step++;
        }

        if (fin)
            answer += Integer.parseInt(current);

        return answer;
    }

    public HashMap<Character, Integer> getDefaultSDT() {
        HashMap<Character, Integer> defaultSDT = new HashMap<Character, Integer>();
        defaultSDT.put('S', 1);
        defaultSDT.put('D', 2);
        defaultSDT.put('T', 3);
        return defaultSDT;
    }

    public boolean isDisit(char ch) {
        if ('0' <= ch && ch <= '9')
            return true;
        return false;
    }
}
