import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1245_균형점 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] pos = new int[N];
            int[] mass = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N * 2; i++) {
                if (i < N) pos[i] = Integer.parseInt(st.nextToken());
                else mass[i-N] = Integer.parseInt(st.nextToken());
            }
            double[] answer = new double[N-1];
            for (int i = 0; i < N-1; i++) {
                double left = pos[i];
                double right = pos[i+1];
                double mid = 0;
                while (right - left > 1 / Math.pow(10, 12)) {
                    mid = (left + right) / 2;
                    double leftPower = 0;
                    double rightPower = 0;
                    for (int j = 0; j < N; j++) {
                        if (pos[j] < mid) leftPower += mass[j] / Math.pow(mid-pos[j], 2);
                        else rightPower += mass[j] / Math.pow(pos[j]-mid, 2);
                    }
                    if (leftPower > rightPower) left = mid;
                    else right = mid;
                }
                answer[i] = mid;
            }
            System.out.print("#" + tc + " ");
            for (double balance : answer) {
                System.out.printf("%.10f ", balance);
            }
            System.out.println();
        }
    }
}
