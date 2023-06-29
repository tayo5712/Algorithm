import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class _03_문장_속_단어 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sentence = sc.nextLine();
        String[] words = sentence.split(" ");
        String maxWord = "";

        // 1
//        for (String word : words) {
//            if (maxWord.length() < word.length()) {
//                maxWord = word;
//            }
//        }
//        System.out.println(maxWord);

        // 2
        int pos;
        while((pos = sentence.indexOf(" ")) != -1) {
            String tmp = sentence.substring(0, pos);
            maxWord = maxWord.length() < tmp.length() ? tmp : maxWord;
            sentence = sentence.substring(pos + 1);
        }
        maxWord = maxWord.length() < sentence.length() ? sentence : maxWord;
        System.out.println(maxWord);
    }
}
