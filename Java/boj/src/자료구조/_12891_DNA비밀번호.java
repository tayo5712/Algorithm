package 자료구조;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _12891_DNA비밀번호 {
    static int checkArr[]; // 필요한 {'A','C', 'G', 'T'} 각 개수
    static int myArr[]; // 현재 {'A','C', 'G', 'T'} 각 개수
    static int checkCount = 0; // 각각 A, C, G, T 개수가 필요 개수랑 맞으면 1씩 증가 ( 총 4면 비밀번호수 1증가)
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        int result = 0;
        checkArr = new int[4];
        myArr = new int[4];
        char A[] = br.readLine().toCharArray();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {   // 필요한 {'A','C', 'G', 'T'} 각 개수 입력 받기
            checkArr[i] = Integer.parseInt(st.nextToken());
            if (checkArr[i] == 0) { // 0 이면 체크할 문자가 없으므로 체크카운터를 1 늘려준다.
                checkCount++;
            }
        }
        for (int i = 0; i < P; i++) {   // 초기 P부분 문자열 처리
            Add(A[i]);
        }
        if (checkCount == 4) {  // 각 요구하는 개수를 충족한다면 결과 1추가
            result++;
        }

        for (int i = 0; i < S-P; i++) { // P 범위를 잡고 옆으로 이동하면서 문자열 체크
            int j = i+P;
            Add(A[j]);
            Remove(A[i]);
            if (checkCount == 4) {
                result++;
            }
        }
        System.out.println(result);


    }

    private static void Add(char c) {
        switch (c) {
            case 'A':
                myArr[0]++;
                if (myArr[0] == checkArr[0]) {
                    checkCount++;
                }
                break;
            case 'C':
                myArr[1]++;
                if (myArr[1] == checkArr[1]) {
                    checkCount++;
                }
                break;
            case 'G':
                myArr[2]++;
                if (myArr[2] == checkArr[2]) {
                    checkCount++;
                }
                break;
            case 'T':
                myArr[3]++;
                if (myArr[3] == checkArr[3]) {
                    checkCount++;
                }
                break;
        }
    }

    private static void Remove(char c) {
        switch (c) {
            case 'A':
                if (myArr[0] == checkArr[0]) {
                    checkCount--;
                }
                myArr[0]--;
                break;
            case 'C':
                if (myArr[1] == checkArr[1]) {
                    checkCount--;
                }
                myArr[1]--;
                break;
            case 'G':
                if (myArr[2] == checkArr[2]) {
                    checkCount--;
                }
                myArr[2]--;
                break;
            case 'T':
                if (myArr[3] == checkArr[3]) {
                    checkCount--;
                }
                myArr[3]--;
                break;
        }
    }
}
