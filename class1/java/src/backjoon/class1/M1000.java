package backjoon.class1;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class M1000 {

    public static void main(String[] args) throws IOException {

        /* Scanner 클래스를 사용한 입력

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(a+b);
        sc.close();

        */

        // 문자열 분리 방법
            // StringTokenizer 클래스를 이용하여 분리해주는 방법
            // 단순 규칙으로 문자열을 분리해줄 경우
            // StringTokenizer("문자열", "구분자")

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        // StringTokenizer st = new StringTokenizer(br.readline());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        System.out.println(a+b);

        // split() 을 이용하는 방법
        // br.readline()을 통해 읽어온 것을 split(" ")하여 공백 단위로 나눠준 뒤
        // String 배열에 각각 저장하는 방법

        BufferedReader br2 = new BufferedReader(new InputStreamReader(System.in));

        String[] str2 = br2.readLine().split(" ");
        int a2 = Integer.parseInt(str2[0]);
        int b2 = Integer.parseInt(str2[1]);

        System.out.println(a2+b2);

    }
 }

