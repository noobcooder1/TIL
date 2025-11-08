package 자바문제들;
import java.util.Scanner;

//문자열 str이 주어집니다.
//문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.
//제한사항
//
//1 ≤ str의 길이 ≤ 10

public class programmers_day2_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        for (char i : a.toCharArray()) {
            System.out.println(i);
        }
   /*    for (int i = 0; i < a.length(); i++) {
              String[] printString = new String[a.length()];
              printString[i] = a.substring(i, i + 1);
              System.out.println(printString[i]);

              2.간단한 버전
              System.out.println(a.substring(i, i + 1));
          }
    */

    }
}


