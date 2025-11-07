package 자바문제들;
import java.util.Scanner;

public class programmers_day2_1 {
   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int a = sc.nextInt();
       int b = sc.nextInt();
       int c = a + b;

       // System.out.printf("%d + %d = %d", a, b, c);
       System.out.print(a + " + " + b + " = " + (a+b) );
   }
}
