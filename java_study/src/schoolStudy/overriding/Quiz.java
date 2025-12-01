package schoolStudy.overriding;
import java.util.Scanner;

public class Quiz {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);

        while (true) {
            System.out.println("안녕하세요. 마법의 계산기입니다. 원하시는 숫자와 연산자를 입력하여"
                    + "결과를 보실 수 있습니다. 만약 종료를 원하신다면 연산자에 ! 를 입력하세요.\n");

            System.out.println("연산할 숫자를 입력하시오.");
            int num1 = s1.nextInt();
            s1.nextLine();                          //개행문자 엔터의 값제거

            System.out.println("연산기호를 입력하시오.");
            String tool = s1.nextLine();

            System.out.println("연산할 숫자를 하나 더 입력하시오.\n");
            int num2 = s1.nextInt();
            calculator(num1, tool, num2);
        }

    }

    static void calculator(int num1, String tool, int num2) {
        switch (tool) {
            case ("+"): {
                System.out.println(num1 + " + " + num2 + " = " + (num1 + num2) + "\n");
                break;
            }
            case ("-"): {
                System.out.println(num1 + " - " + num2 + " = " + (num1 - num2) + "\n");
                break;
            }
            case ("*"): {
                System.out.println(num1 + " * " + num2 + " = " + (num1 * num2) + "\n");
                break;
            }
            case ("/"): {
                System.out.println(num1 + " / " + num2 + " = " + (num1 / num2) + "\n");
                break;
            }
            case ("%"): {
                System.out.println(num1 + " % " + num2 + " = " + (num1 % num2) + "\n");
                break;
            }
            case ("!"): {
                System.out.println("안녕히가세요.");
                System.exit(0);
            }
            default: {
                System.out.println("잘못된 연산자입니다! 다시 입력하세요!!\n");
            }
        }
    }
}
