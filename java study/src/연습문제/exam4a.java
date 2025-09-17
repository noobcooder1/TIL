package 연습문제;
import java.util.Scanner;

public class exam4a {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("삼겹살 몇 인분 주문하시나요????");
        int num = s1.nextInt();
        System.out.println("총 칼로리는 " + calculate(num) + "칼로리 입니다.");
    }

    public static double calculate (int num) {        //웬만하면 float 보다 double을 사용하는게 낫다!
        double oneserving = 180 * 5.179;
        return oneserving * num;
    }
}
