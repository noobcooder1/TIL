package 자바문제들;

//문제 설명

//영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
//        제한사항

//    1 ≤ str의 길이 ≤ 20
//str은 알파벳으로 이루어진 문자열입니다.

//입출력 예

//입력 #1

//aBcDeFg

//출력 #1

//AbCdEfG

import java.util.Scanner;

public class programmers_day1_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("변환하고싶은 문장을 입력하세요.");
        String a = sc.next();
        char[] aa = new char[20];
        String[] answer = new String[20];


        for (int i = 0; i < a.length(); i++) {
            aa[i] = a.charAt(i);
            if ((int)aa[i] >= 65 && (int)aa[i] <= 90) {
                answer[i] = Character.toString(Character.toLowerCase(aa[i]));
            }
            else if ((int)aa[i] >= 97 && (int)aa[i] <= 122) {
                answer[i] = Character.toString(Character.toUpperCase(aa[i]));
            }
            else {
                System.out.print("알파벳만 입력하세요!");
                System.exit(0);
            }
        }
        for (int i = 0; i < a.length(); i++) {
            System.out.print(answer[i]);
        }
    }
}

//문제를 푸는데 헷갈렸던 개념들과 몰랐던 개념들이 양이 너무 많은 관계로 코파일럿 대화 링크를 올립니다.
//https://copilot.microsoft.com/shares/oJ9sPLtvMYjUr4Zk8HjXy