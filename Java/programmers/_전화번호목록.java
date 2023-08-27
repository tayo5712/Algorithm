import java.util.HashMap;

public class _전화번호목록 {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        HashMap<String, Integer> hm = new HashMap<>();
        for (int i = 0; i < phone_book.length; i++) {
            hm.put(phone_book[i], i);
        }
        for(String s : phone_book) {
            for (int i = 1; i < s.length(); i++) {
                if (hm.containsKey(s.substring(0, i))) return false;
            }
        }
        return answer;
    }
}
