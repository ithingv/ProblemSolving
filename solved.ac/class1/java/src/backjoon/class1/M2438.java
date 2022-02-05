package backjoon.class1;
// 별찍기 - 1

import java.util.Scanner;

public class M2438 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();

        String result = "";
        for(int i=0; i<n; i++){
            result += "*";
            System.out.println(result);
        }
    }
}
