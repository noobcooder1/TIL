package 연습문제;
import java.util.Scanner;
import java.util.Arrays;

public class exam6b {
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("입력할 숫자를 띄어쓰기로 구분해서 입력하세요.");
        String input = s1.nextLine();

        String[] nums = input.split(" ");
        int[] numbers = Arrays.stream(nums)
                .mapToInt(Integer::parseInt) // 각 문자열 요소를 정수로 변환
                .toArray();                  // 정수들을 모아 배열로 생성

        judge(numbers);
    }

    /**
     * 주어진 숫자가 소수인지 판별하는 메서드
     * @param num 판별할 숫자
     * @return 소수이면 true, 아니면 false
     */
    public static boolean isPrime(int num) {
        // 1 이하의 수는 소수가 아닙니다.
        if (num <= 1) {
            return false;
        }

        // 2부터 자신의 제곱근까지의 수로 나누어 떨어지는지 확인합니다.
        // i * i <= num 과 같이 제곱근 대신 사용할 수도 있습니다.
        for (int i = 2; i <= Math.sqrt(num); i++) {
            // '%' 연산자를 사용하여 나누어 떨어지는지(나머지가 0인지) 확인합니다.
            // 나누어 떨어진다는 것은 1과 자기 자신 외에 다른 약수가 있다는 의미이므로 소수가 아닙니다.
            if (num % i == 0) {
                return false;
            }
        }

        // 반복문을 모두 통과했다면 다른 약수가 없다는 의미이므로 소수입니다.
        return true;
    }

    public static void judge(int[] score) {
        // 향상된 for문(for-each)으로 배열의 각 요소를 순회합니다.
        for (int num : score) {
            // isPrime 메서드를 호출하여 소수인지 판별합니다.
            if (isPrime(num)) {
                System.out.println(num + "은(는) 소수입니다.");
            } else {
                System.out.println(num + "은(는) 소수가 아닙니다.");
            }
        }
    }
}