package backjoon.class1;
// 두수 비교하기

import java.util.Scanner;

public class M1330 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        sc.close();

        if (a > b){
            System.out.println(">");
        } else if (a < b){
            System.out.println("<");
        } else {
            System.out.println("==");
        }

    }
}
