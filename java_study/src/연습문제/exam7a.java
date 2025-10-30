package 연습문제;
import java.util.Scanner;

public class exam7a {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("만들고 싶은 숫자 피라미드의 높이를 입력해주세요.");
        int low = s1.nextInt();
        int num = 1;

        for (int i = 1; i <= low; i++) {
            for (int j = 0; j < i; j++) {
                System.out.printf("%d ", num);
                num++;
            }
            System.out.println();
        }
    }
}
