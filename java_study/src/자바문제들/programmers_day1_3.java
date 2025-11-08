package 자바문제들;

import java.util.Scanner;

//문제 설명 : 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
//
//제한사항 : 1 ≤ str의 길이 ≤ 20
//str은 알파벳으로 이루어진 문자열입니다.

public class programmers_day1_3 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        System.out.print(str.repeat(n));
    }

}

//문제를 푸는데 사용된 내가 몰랐던 개념 : String.repeat(int count)는 문자열을 지정한 횟수만큼 이어 붙인 새로운 문자열을 반환합니다.
//원본 문자열은 변경되지 않습니다.
//
//public String repeat(int count)
//
//반환값: 현재 문자열을 count번 반복한 새 문자열
//
//특징 : count = 0: 빈 문자열 "" 반환
//count = 1: 원본 문자열 그대로 반환
//count < 0: IllegalArgumentException 발생
//
//성능: 내부적으로 길이를 미리 계산해 버퍼를 할당하여 효율적으로 이어 붙입니다. 아주 큰 count는 메모리 부족(OOM) 위험이 있으니 주의.