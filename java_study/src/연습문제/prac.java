package 연습문제;

public class prac {
    public static void main(String[] args) {
        int a = 100;
        int b = 200;
        int c = 300;
        final int d = a + b + c;        //final선언시에는 변숫값변경불가
        String dd = "hello";

        System.out.println("a와 b와 c와 d의 합계는 " + d + "입니다.");
        System.out.println("문자열 dd의 값은 " + dd);
    }

}
