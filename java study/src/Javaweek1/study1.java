package Javaweek1;
import java.util.Scanner;

public class study1 {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);

        System.out.println("출력하고 싶은 단까지 입력하세요.");
        int num = s1.nextInt();

        for (int hang = 1; hang <= 9; hang++) {
            PrintHang(num, hang);
        }
    }

    static void PrintHang(int num, int hang) {
        for (int dan = 2; dan <= num; dan++) {
            System.out.printf("%d * %d = %d\t\t", dan,  hang, hang * dan);
        }
        System.out.println();
    }
}
