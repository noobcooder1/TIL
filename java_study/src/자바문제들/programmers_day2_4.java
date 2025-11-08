package 자바문제들;
import java.util.Scanner;

//문제 설명 : 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을,
//홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.
//
//제한사항 : 1 ≤ n ≤ 1,000


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
