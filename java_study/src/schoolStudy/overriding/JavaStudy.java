package schoolStudy.overriding;
import java.util.Scanner;

/*
문제 )다음의 자바스터디메인클래스를 보고 자바스터디클래스에서 게터와 세터를 이용하여 숫자와 연산자를 입력받은후
해당 연산자의 사칙연산을 수행하는 코드를 완성하시오.
단 자바스터디 클래스는 숫자와 연산자 각을 처리하는 생성자를 포함하고 있어야한다.
*/

public class JavaStudy {
    Scanner sc = new Scanner(System.in);
    private String oper;
    private int num1;
    private int num2;

    public void setNum1(int num1) {
        this.num1 = num1;
    }

    public int getNum1() {
        return num1;
    }

    public void setNum2(int num2) {
        this.num2 = num2;
    }

    public int getNum2() {
        return num2;
    }

    public void setOper(String oper) {
        this.oper = oper;
    }

    public String getOper() {
        return oper;
    }



//시프트 + 위아래 화살표를 하면 한 줄 단위로 선택이 됨.




    public static void main(String[] args) {


    }
}
