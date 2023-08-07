import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class _12222_문자열나누기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            String str = br.readLine();
            StringBuilder cur = new StringBuilder();
            StringBuilder pre = new StringBuilder();
            ArrayList<String> arr = new ArrayList<>();
            for (int i = 0; i < str.length(); i++) { // 이전 문자열과 같지 않으면 현재 문자열을 넣는다, 같으면 현재 문자열에 계속 더해주기
                cur.append(str.charAt(i));
                if (!pre.toString().equals(cur.toString())) {
                    arr.add(String.valueOf(cur));
                    pre = new StringBuilder(cur);
                    cur.setLength(0);
                }
            }
            System.out.println("#" + tc + " " + arr.size());
        }
    }
}
