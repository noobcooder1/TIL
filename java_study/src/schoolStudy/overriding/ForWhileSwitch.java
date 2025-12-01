package schoolStudy.overriding;

import java.util.Scanner;

public class ForWhileSwitch {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);

        System.out.println("반복횟수를 설정해주세요.");
        int n = s1.nextInt();
        int count = 0;

        forloop(n);

        while(count < n) {
            System.out.println("반복합니다.");
            count++;
        }

    }

    static void forloop(int num) {
        for (int i = 1; i <= num; i++) {
            System.out.println(i + "번");
        }
        System.out.println();
    }
}
