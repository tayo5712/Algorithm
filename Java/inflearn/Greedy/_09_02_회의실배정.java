package Greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Meet implements Comparable<Meet> {
    int st;
    int ed;
    public Meet(int st, int ed) {
        this.st = st;
        this.ed = ed;
    }

    @Override
    public int compareTo(Meet o) {
        if (this.ed == o.ed) return this.st-o.st;
        return this.ed-o.ed;
    }
}

public class _09_02_회의실배정 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Meet> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.add(new Meet(a, b));
        }
        Collections.sort(arr);
        int answer = 0;
        int edTime = 0;
        for (int i = 0; i < n; i++) {
            Meet meet = arr.get(i);
            if (meet.st >= edTime) {
                answer++;
                edTime = meet.ed;
            }
        }
        System.out.println(answer);
    }
}
