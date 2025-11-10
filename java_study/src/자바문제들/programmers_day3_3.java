package 자바문제들;

//문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.
//제한사항 : 1 ≤ my_string의 길이 ≤ 100
//my_string은 영소문자로만 이루어져 있습니다.
//1 ≤ k ≤ 100


public class programmers_day3_3 {
    public String solution(String my_string, int k) {
        String answer = "";
        StringBuilder sb = new StringBuilder(answer);

        for (int i = 0; i < k; i++) {
            sb.append(my_string);
        }
        return sb.toString();
    }
}

//ArrayList <string> str = new ArrayList<>();
//str.add(my_string);
/* 그리고 StringBuilder 구조에 대해서 몰랐음. 좀 더 잘 알아둘 필요가 있음.*/
