package etc;

import java.util.*;
import java.io.*;


public class Main {
    static int n;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        if (n == 1){
            System.out.println(2);
        }
        else {
            for (int i = n; ; i++){
                if (isPalind(i) && isPrime(i)){
                    System.out.println(i);
                    break;
                }
            }
        }
    }
    public static boolean isPrime(int num){
        for (int i = 2; i <= Math.sqrt(num); i++){
            if (num % i == 0){
                return false;
            }
        }
        return true;
    }
    public static boolean isPalind(int num) {
        if (num == Integer.parseInt(String.valueOf(new StringBuilder(String.valueOf(num)).reverse()))) {
            return true;
        }
        return false;
    }
}
