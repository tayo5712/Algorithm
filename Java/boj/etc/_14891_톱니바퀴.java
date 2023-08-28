package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class _14891_톱니바퀴 {
    static ArrayList<ArrayList<Character>> wheels = new ArrayList<>();
    static class wheel {
        int num;
        int dir;
        public wheel(int num, int dir) {
            this.num = num;
            this.dir = dir;
        }
    }
    static void Turn(int n, int d) {
        ArrayList<wheel> move = new ArrayList<>();
        move.add(new wheel(n, d));
        int rot = d;
        for (int i = n + 1; i < 4; i++) {
            if (wheels.get(i).get(6) != wheels.get(i-1).get(2)) {
                rot *= - 1;
                move.add((new wheel(i, rot)));
            }
            else break;
        }
        rot = d;
        for (int i = n - 1; i > - 1; i--) {
            if (wheels.get(i).get(2) != wheels.get(i+1).get(6)) {
                rot *= -1;
                move.add(new wheel(i, rot));
            }
            else break;
        }
        for (wheel w : move) {
            if (w.dir == 1) {
                char tmp = wheels.get(w.num).remove(7);
                wheels.get(w.num).add(0, tmp);
            }
            else {
                char tmp = wheels.get(w.num).remove(0);
                wheels.get(w.num).add(tmp);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 4; i++) {
            wheels.add(new ArrayList<>());
            for (char c : br.readLine().toCharArray()) {
                wheels.get(i).add(c);
            }
        }
        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            int direction = Integer.parseInt(st.nextToken());
            Turn(number-1, direction);
        }
        int answer = 0;
        for (int i = 0; i < 4; i++) {
            int n = Character.getNumericValue(wheels.get(i).get(0)) * (int) Math.pow(2, i);
            answer += n;
        }
        System.out.println(answer);
    }
}
