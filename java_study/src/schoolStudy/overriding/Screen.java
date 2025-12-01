package schoolStudy.overriding;

import java.util.Objects;
import java.util.Scanner;


class Screen {
    Scanner s1 = new Scanner(System.in);
    public void monitor() {
        System.out.print("정수와 연산자, 정수를 입력하시오 >>");
        int a = s1.nextInt();
        String op = s1.next();
        int b = s1.nextInt();
        Calcu aa = null;

        if (Objects.equals(op, "+")) {
            aa = new Add();
        }
        else if (Objects.equals(op, "-")) {
            aa = new Sub();
        }
        else if (Objects.equals(op, "*")) {
            aa = new Mul();
        }
        else if (Objects.equals(op, "/")) {
            aa = new Div();
        }

        if (aa != null) {
            aa.setValue(a, b);
            System.out.println("결과는 " + aa.calculate());
        }
    }
}