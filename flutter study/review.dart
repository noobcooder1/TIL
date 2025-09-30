void main() {

  List<String> names = ['홍길동', '김철수', '이영희'];

  printName(names);
}

void printName(names) {                   //이름이 들어있는 배열을 받아서 출력하는 함수
  for (int i = 0; i < names.length; i++) {
    print(names[i]);
  }
}