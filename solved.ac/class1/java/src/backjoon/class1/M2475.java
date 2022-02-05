package backjoon.class1;
//검증수

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class M2475 {
    public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] str = br.readLine().split(" ");

    int result = 0;
    for(String s : str){
        int num = Integer.parseInt(s);
        result += Math.pow(num, 2);
    }
        System.out.println(result % 10);
    }
}
