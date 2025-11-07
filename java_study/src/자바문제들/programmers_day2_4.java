package 자바문제들;
import java.util.Scanner;

public class programmers_day2_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        /* 1. 정석 if 문
         if (n % 2 == 0) {
            System.out.print(n + " is even");
           }
            else {
                System.out.print(n + " is odd");
            }

        2. 삼항연산자 */
        System.out.print(n % 2 == 0 ? n + " is even" : n + " is odd") ;
    }
}
