package 자바문제들;
import java.util.Scanner;

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


