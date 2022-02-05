package backjoon.class1;
// 최댓값

import java.util.Scanner;

public class M2562 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int pos = 0;
        int max_val = 0;
        int curr = 0;

        for(int i=0; i<9; i++){
            curr = sc.nextInt();
            if (curr > max_val) {
                pos = i;
                max_val = curr;
            }
        }
        System.out.println(max_val);
        System.out.println(pos + 1);
    }
}
