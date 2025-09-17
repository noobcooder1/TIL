package 연습문제;
import java.math.BigInteger;
import java.util.Scanner;

public class exam2a {
    public static void main(String[] args) {

        Scanner s1 = new Scanner(System.in);
        System.out.print("자릿수의 합계를 구할 숫자를 구하시오.\n");
        BigInteger a = s1.nextBigInteger();

        System.out.printf("각 자릿수의 합은 %d 입니다.", sumint(a));
    }

    public static int sumint(BigInteger a) {
        String num = a.toString();      //입력된 숫자 a를 문자열로 변환해서 num에 대입함. biginteger는 직접적인연산이 까다로워서
        int sum = 0;

        for (int i = 0; i < num.length(); i++) {
            sum += Character.getNumericValue(num.charAt(i));
        }
        return sum;
    }
}


