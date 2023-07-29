package Stack_Queue;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class _05_08_응급실 {
    static class Person {
        int id;
        int danger;
        public Person(int id, int danger) {
            this.id = id;
            this.danger = danger;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Queue<Person> Q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            Q.offer(new Person(i, a));
        }

        int answer = 1;

        while (!Q.isEmpty()) {
            Person tmp = Q.poll();
            for (Person p : Q) {
                if (tmp.danger < p.danger) {
                    Q.offer(tmp);
                    tmp = null;
                    break;
                }
            }
            if (tmp != null) {
                if (tmp.id == m) System.out.println(answer);
                else answer++;
            }
        }
    }
}
