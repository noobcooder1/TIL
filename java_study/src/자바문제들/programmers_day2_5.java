package 자바문제들;

//문자열 my_string, overwrite_string과 정수 s가 주어집니다. 문자열 my_string의 인덱스 s부터 overwrite_string의
//길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

//제한사항
//      my_string와 overwrite_string은 숫자와 알파벳으로 이루어져 있습니다.
//        1 ≤ overwrite_string의 길이 ≤ my_string의 길이 ≤ 1,000
//        0 ≤ s ≤ my_string의 길이 - overwrite_string의 길이


public class programmers_day2_5 {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        String main_string1 = my_string.substring(0, s);
        String main_string3 = my_string.substring(s + overwrite_string.length());

        answer = answer + main_string1 + overwrite_string + main_string3;
        return answer;
    }
}
