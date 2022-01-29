package backjoon.class1;

import java.util.Scanner;

public class M2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int result = 1;

        for (int i = 0; i < 3; i++) {
            result *= sc.nextInt();
        }

        String str = String.valueOf(result);

        for (int i = 0; i < 10; i++) {
            int cnt = 0;
            char n = (char) (i + '0');

            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == n) {
                    cnt += 1;
                }
            }
            System.out.println(cnt);
        }
    }
}