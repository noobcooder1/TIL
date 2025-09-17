package 연습문제;
import java.util.Scanner;

public class exam3a {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("구하고싶은 직사각형의 가로를 입력하세요.");
        int width = s1.nextInt();

        System.out.println("구하고싶은 직사각형의 세로를 입력하세요.");
        int height = s1.nextInt();

        System.out.println("직사각형의 넓이는 " + square(width, height) + "입니다.");
        s1.close();     //메서드의 자원관리를 위해서 클래스를 닫는다는 의미의 코드를 입력함.
    }

    public static int square(int width, int height) {
        return width * height;
        //바로 리턴하는 것도 방법임!   return width * height;
    }
}
