import java.util.HashMap;

public class _완주하지못한선수 {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String people : participant) {
            if (!hm.containsKey(people)) hm.put(people, 0);
            hm.put(people, hm.get(people)+1);
        }
        for (String people : completion) {
            hm.put(people, hm.get(people)-1);
        }
        for (String people : hm.keySet()) {
            if (hm.get(people) != 0) {
                answer = people;
                break;
            }
        }
        return answer;
    }
}
