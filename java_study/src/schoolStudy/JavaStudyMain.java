package schoolStudy;
import java.util.Scanner;

public class JavaStudyMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        JavaStudy cs = new JavaStudy();

        System.out.println("첫번째 수 : ");
        cs.setNum1(sc.nextInt());
        System.out.println("연산자선택 : +, -, *, /: ");
        cs.setOper(sc.next());
        System.out.println("두번째 수 : ");
        cs.setNum2(sc.nextInt());

        switch (cs.getOper()) {
            case "+":
                System.out.println("결과는 : " + (cs.getNum1() + cs.getNum2()));
                break;

            case "-":
                System.out.println("결과는 : " + (cs.getNum1() - cs.getNum2()));
                break;

            case "*":
                System.out.println("결과는 : " + (cs.getNum1() * cs.getNum2()));
                break;

            case "/":
                System.out.println("결과는 : " + (cs.getNum1() / cs.getNum2()));
                break;
        }
        //println에서 +가 문자열을 더하는 연산자취급되어 먼저 실행되니 문자열 + 숫자는 문자열 취급이라
        // - 로 문자열 - 숫자 연산을 실행할수없어서 오류가남. 마찬가지로 + 연산도 똑같이 원하는 결괏값을 못 얻음
    }
}