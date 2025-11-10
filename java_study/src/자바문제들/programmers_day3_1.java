package 자바문제들;

//길이가 같은 두 문자열 str1과 str2가 주어집니다.
//두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는
//solution 함수를 완성해 주세요.
//제한사항 : 1 ≤ str1의 길이 = str2의 길이 ≤ 10
//str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.

public class programmers_day3_1 {
  public String solution(String str1, String str2) {
      String answer = "";
      int count1 = 0;
      int count2 = 0;

      for (int i = 0; i < str1.length() * 2; i++) {
          if (i == 0 || i % 2 == 0) {
              answer = answer + str1.substring(count1, count1 + 1);
              count1++;
          }
          else {
              answer = answer + str2.substring(count2, count2 + 1);
              count2++;
          }
      }

      return answer;
  }
}

//StringBuilder등을 사용햇으면 더 간단했을것
