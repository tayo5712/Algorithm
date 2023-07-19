package Greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Friend implements Comparable<Friend> {
    int t;
    int state;

    public Friend(int t, char state) {
        this.t = t;
        this.state = state;
    }

    @Override
    public int compareTo(Friend o) {
        if (this.t == o.t) return this.state - o.state;
        return this.t-o.t;
    }
}

public class _09_03_결혼식 {
    public static void main(String[] args) throws IOException {
        ArrayList<Friend> myFriends = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            myFriends.add(new Friend(start, 's'));
            myFriends.add(new Friend(end, 'e'));
        }
        Collections.sort(myFriends);

        int answer = 0;
        int cnt = 0;
        for (int i = 0; i < myFriends.size(); i++) {
            if (myFriends.get(i).state == 's') cnt++;
            else cnt--;
            answer = Math.max(answer, cnt);
        }
        System.out.println(answer);
    }
}
