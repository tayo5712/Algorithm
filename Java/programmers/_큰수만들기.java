class _큰수만들기 {
    public String solution(String number, int k) {
        char[] arr = number.toCharArray();
        int n = arr.length;
        int r = n - k;
        int s = 0;
        String answer = "";
        int i; // 변수 i를 선언

        while (s < r) {
            char maxV = '0';
            int maxI = 0;
            for (i = s; i < r; i++) { // i를 for문 내에서 선언
                if (arr[i] > maxV) {
                    maxV = arr[i];
                    maxI = i;
                }
            }
            answer += maxV;
            s = maxI + 1;
            r--;
        }
        for (i = s; i < n; i++) {
            answer += arr[i];
        }

        return answer;
    }
}