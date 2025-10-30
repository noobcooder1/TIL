void main() {
  print(5 + 19);

  int a = 5;
  int b = 10;
  print(a + b);

  var c = 20;   // 대입연산자와 논리연산자등을 사용함.
  var d = 30;

  print(c > d);

  var e = true; var f = false;

  var andResult = e && f; // and
  var notResult = !e;    // not

  print(andResult);
  print(notResult);

  var year = 2004;
  var bornYear = 2003;
  var age = year - bornYear + 1;
  var num = 10;

  for (var i = 0; i < num; i++) {
    for (var j = 0; j < num; j++) {
      print(i);
      print(' ');
    }
  }
  print(age);
}