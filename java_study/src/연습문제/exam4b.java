package 연습문제;
import java.util.Scanner;

//① 월급은 (총 근무시간) x (기본 시급)으로 책정된다.
//        ② 총 근무시간이 160시간을 넘으면 초과 근무 시간이 시급이 1.5배를 적용한다.
//        ③ 최저 시급은 1만원이며 이보다 작은 경우 경고문을 출력한다.
//        ④ 총 근무시간이 180시간을 넘으면 경고문을 출력한다.
//        ⑤ 출력 예와 같은 결과가 나오도록 하단 코드의 printSalary() 메소드를 완성하시오

public class exam4b {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("시급은 얼마인가요????");
        int money = s1.nextInt();
        if (money < 10000) {
            System.err.println("최저시급은 10000원보다 작을 수 없습니다!");
            System.exit(404);

        }

        System.out.println("몇 시간 일하셨나요????");
        int time = s1.nextInt();
        if (time > 180) {
            System.err.println("일한 시간은 180시간을 넘을 수 없습니다!");
            System.exit(404);

        }
        System.out.println("당신의 월급은 " + printSalary(time, money) + "원 입니다.");
    }

    public static long printSalary(int time, int money) {
        double salary;
        if (time > 160) {
            salary = ((long)money * 160) + ((money * 1.5) * (time - 160));
        }
        else {
            salary = (long)money * time;
        }
        return (long)salary;
    }
}
