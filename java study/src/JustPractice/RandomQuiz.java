//이 코드는 아직 완전하지않습니다. 나중에 수정할 에정입니다.

package JustPractice;
import java.util.Random;
import java.util.Scanner;

public class RandomQuiz {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        Random q1 = new Random();
        String[] oppo = {"+", "-", "*", "/"};

        while(true) {
            int num1 = q1.nextInt(100);
            int num2 = q1.nextInt(100);
            int answer;
//            int ranidx = q1.nextInt(oppo.length - 1);
//            String op = oppo[ranidx];
            System.out.println("연습하고 싶으신 연산유형은? +, -, *, /중 입력, 프로그램종료시엔 ! 입력 ");
            String op = s1.nextLine();

            switch(op) {
                case "+":
                    System.out.println(num1 + "+" + num2 + "= 의 정답을 입력하세요.");
                    answer =  s1.nextInt();
                    s1.nextLine();
                    if (answer == (num1 + num2)) {
                        System.out.println("정답입니다!");
                    }
                    else {
                        System.out.println("오답입니다. 다음기회에!");
                    }
                    break;
                case "-":
                    System.out.println(num1 + "-" + num2 + "= 의 정답을 입력하세요.");
                    answer =  s1.nextInt();
                    s1.nextLine();
                    if (answer == (num1 - num2)) {
                        System.out.println("정답입니다!");
                    }
                    else {
                        System.out.println("오답입니다. 다음기회에!");
                    }
                    break;
                case "*":
                    System.out.println(num1 + "*" + num2 + "= 의 정답을 입력하세요.");
                    answer =  s1.nextInt();
                    s1.nextLine();
                    if (answer == (num1 * num2)) {
                        System.out.println("정답입니다!");
                    }
                    else {
                        System.out.println("오답입니다. 다음기회에!");
                    }
                    break;
                case "/":
                    System.out.println(num1 + "/" + num2 + "= 의 정답을 입력하세요.");
                    answer =  s1.nextInt();
                    s1.nextLine();
                    if (answer == (num1 / num2)) {
                        System.out.println("정답입니다!");
                    }
                    else {
                        System.out.println("오답입니다. 다음기회에!");
                    }
                    break;
                case "!":
                    System.exit(0);
                    break;

                default:
                    System.out.println("잘못된 연산자");

            }
        }

    }
//    입력받은 연산자를 직접 사용할 수 없어서 못 쓰는 코드
//    void answer(int num1, int num2, String opoo) {
//        System.out.println(num1 + "oppo" + num2 + "= 의 정답을 입력하세요.");
//        int answer =  s1.nextInt();
//        if (answer == (num1 + num2)) {
//            System.out.println("정답입니다!");
//        }
//        else {
//            System.out.println("오답입니다. 다음기회에!");
//        }
//    }
}
