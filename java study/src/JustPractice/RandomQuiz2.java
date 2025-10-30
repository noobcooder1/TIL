package JustPractice;

import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;
import java.util.Scanner;

public class RandomQuiz2 {
    //이 코드는 아직 완전하지않습니다. 나중에 수정할 에정입니다.
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        Random q1 = new Random();
        String re;

        String[] oppo = {"+", "-", "*", "/"};

        do  {
            ThreadLocalRandom.current().nextInt(oppo.length);
            String pick = oppo[ThreadLocalRandom.current().nextInt(oppo.length)];
            int num1 = q1.nextInt(100);
            int num2 = q1.nextInt(100);
            int answer;

            switch (pick) {
                case "+":
                    System.out.printf("%d %s %d 의 정답은?", num1, pick, num2);
                    answer = s1.nextInt();
                    if (answer == num1 + num2) {
                        System.out.println("정답입니다.");
                    } else {
                        System.out.printf("오답입니다.  정답은 : %d 입니다.", num1 + num2);
                    }
                    break;

                case "-":
                    System.out.printf("%d %s %d 의 정답은?", num1, pick, num2);
                    answer = s1.nextInt();
                    if (answer == num1 - num2) {
                        System.out.println("정답입니다.");
                    } else {
                        System.out.printf("오답입니다.  정답은 : %d 입니다.", num1 - num2);
                    }
                    break;

                case "*":
                    System.out.printf("%d %s %d 의 정답은?", num1, pick, num2);
                    answer = s1.nextInt();
                    if (answer == num1 * num2) {
                        System.out.println("정답입니다.");
                    } else {
                        System.out.printf("오답입니다.  정답은 : %d 입니다.", num1 * num2);
                    }
                    break;

                case "/":
                    System.out.printf("%d %s %d 의 정답은?", num1, pick, num2);
                    answer = s1.nextInt();
                    if (answer == num1 / num2) {
                        System.out.println("정답입니다.");
                    } else {
                        System.out.printf("오답입니다.  정답은 : %d 입니다.", num1 / num2);
                    }
                    break;
            }

            System.out.println("문제를 계속 푸시려면 y 또는 Y을 입력하시고, 그만 푸시려면 아무키나 입력하세요.");
            s1.nextLine();
            re = s1.nextLine();

        }   while(re.equals("y") || re.equals("Y"));
    }

}
