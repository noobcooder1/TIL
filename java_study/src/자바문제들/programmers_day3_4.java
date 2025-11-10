package 자바문제들;
//연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
//  12 ⊕ 3 = 123
//  3 ⊕ 12 = 312
//양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
//단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.
//제한사항 : 1 ≤ a, b < 10,000


public class programmers_day3_4 {
    public int solution(int a, int b) {
        int answer = 0;
        String sum1 = a + "" + b;
        String sum2 = b + "" + a;

        if (Integer.parseInt(sum1) > Integer.parseInt(sum2)) {
            answer = Integer.parseInt(sum1);
            return answer;
        }
        else if (Integer.parseInt(sum1) == Integer.parseInt(sum2)) {
            answer = Integer.parseInt(sum1);
            return answer;
        }

        else {
            answer = Integer.parseInt(sum2);
            return answer;
        }
    }
}

/*char -> int, double -> int 형 변환이 아닐경우에도 강제형변환을 시도하려고했음. String형은 (int)로 의해
강제 형변환이 안 됨. 그리고 그러려면 Integer.parseInt()등의 함수를 썼어야함. */
