package 연습문제;
import java.util.Scanner;

public class exam4c {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("how many kilograms do you weigh?");
        double weight = s1.nextDouble();
        System.out.println("How tall are you in centimeters?");
        double height = s1.nextDouble();
        System.out.println("You are " + bmi(weight, height) + " your BMI." + result(bmi(weight, height)));
    }

    public static double bmi (double weight, double height) {
        return weight / Math.pow((height/100), 2);     //제곱을 표현함. Math.pow(밑, 지수)
    }

    public static String result (double bmi) {
        if (bmi >= 30) {
            return "당신은 비만입니다. 다이어트하세요";
        }
        else if (bmi >= 25) {
            return "당신은 과체중입니다. 다이어트가 좀 필요해보입니다.";
        }
        else if (bmi >= 18.5) {
            return "당신은 정상입니다. 잘 유지하세요";
        }
        else {
            return "당신은 저체중입니다. 어느정도의 몸무게는 도움이 됩니다.";
        }
    }
}
