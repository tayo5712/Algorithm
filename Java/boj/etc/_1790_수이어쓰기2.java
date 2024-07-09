
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long k = Long.parseLong(st.nextToken());
        
        long zari = 1;
        long ans = 0;
        long nine = 9;
        while (k > (zari * nine)) {
            k -= zari * nine;
            zari++;
            ans += nine;
            nine *= 10;
        }
        ans += 1 + ((k - 1) / zari);
        if (ans > n) {
            System.out.println(-1);
        } else {
            System.out.println(String.valueOf(ans).charAt((int) ((k-1)%zari)));
        }
    }
}
