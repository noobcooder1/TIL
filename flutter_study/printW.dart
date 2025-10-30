// 문제분석 n의 수에 따라서 v자 모양의 도형을 여러개 반복하는 코드

// 문제분해 1단계 - #으로 이루어진 사각형을 출력하기위해 크기를 정해야함
// -> 간과한 사실 1개 v자는 가로와 세로가 같지가 않기에 가로와 세로축의 크기를 따로 정해야함
// 문제분해 2단계 - #으로 이루어진 정사각형을 v자로 만들기 위해서 어느 위치에 공백을 넣을지 생각해야함
// 2-1단계 v자는 대각선 두 개로 나누어진다. 반대편 대각선을 만들기 위해선 9, 8, 7, 6, 5가 x축이다. 9는 1과 8은 2와
// 같은 식으로 조건식을 짜야한다. 반복횟수를 변수로 두고 뺄까?
// 문제분해 3단계 -v자를 만들었으면 이제 그 v자를 몇 번 반복해서 이어 붙여 출력할지 정해야함

void main() {
  String line = '';
  String tool1 = '#';
  String tool2 = ' ';
  int size = 5;
  int n = 5;

  for (int y = 1; y <= size; y++) {
    for (int x = 1; x <= size * 2 - 1; x++) {
      if (x == y || x == size * 2 - y) {
        line += tool1;
      }
      else {
        line += tool2;
      }
    }
    print(line * n);  //print line의 문자열을 5번 곱해서 만들음.  //
    line = '';
  }
}

// 순정 dart에서는 이렇게 하면 됨
// List.filled + join
// print(List.filled(5, line).join());
// StringBuffer로 누적
// final sb = StringBuffer(); for (var i = 0; i < 5; i++) sb.write(line); print(sb.toString());