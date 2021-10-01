import java.util.ArrayList;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if (cacheSize == 0)
            return cities.length * 5;
        int answer = 0;
        ArrayList<String> cache = new ArrayList<String>();
        for (String city : cities) {
            city = city.toLowerCase();
            int index = cache.indexOf(city);
            if (index != -1) {
                answer += 1;
                cache.remove(index);
                cache.add(city);
            } else {
                answer += 5;
                if (cache.size() == cacheSize) {
                    cache.remove(0);
                }
                cache.add(city);
            }
        }

        return answer;
    }
}