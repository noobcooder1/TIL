void main() {
  print('hello would');
  for(int i = 1; i < 10; i++) {
    print(i);
  }
  print('\n${5 * 8}');


String hello = "hello";
print('\n${hello}');
  
// String? hi;
  
// if(hi != null) {     //null 체크
//   print(hi);
// }

// print(hi?.length);
  
// final String youtuber = 'flutter';
// const String nickname = 'code';
  
// youtuber = 'java';       //final, const 타입의 변수는 값 재할당 불가
// nickname = 'cooder';

int a = 10;
double b = 3.142121;

print(a);
print(a.runtimeType);
print(b);
print(b.runtimeType);

Object c = a;
print(c);

  String name = 'kim';
  int year = 2003;
  
  String TimeManipulation = '$name은 시간을 ${year}년으로 조작했다.';
  
  print(TimeManipulation);

    var numbers = [1, 3, 5, 7, 9];
  numbers.add(2);
  print(numbers);
  
  
  var v2 = List.empty(growable:true);
  v2.add(100);
  v2.add('add String');
  v2.add(false);
  print(v2.runtimeType);
  print(v2);

  var v3 = List.generate(99, (index) => 'number $index');
  print(v3);

  var isString = 312;
  var sampleList = [1, 3, 5, 7, if (isString is! String) isString, 9];
  print(sampleList);

  var List1 = [1, 3, 5];
  print(List1.runtimeType);
  var List2 = ['one', 'two', 'three'];
  print(List2.runtimeType);
  var mergeList = [...List1, ...List2];
  print(mergeList);
  print(mergeList.runtimeType);

  var nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
//   print(nums);
//   var nums2 = List.generate(100, (index) => index + 1);
//   print(nums2);

nums.removeWhere((num) => num % 2 == 0);
  print(nums);

  nums.clear();
  print(nums);

  var nums2 = List.generate(100, (index) => index);
  print(nums2);
  var odds = nums2.where((index) => index % 2 != 0);
  print(odds);

  var mixList = [1, 'two', 3, 'four', 5, 'six', '7', 8, 9, 10];
  print(mixList.runtimeType);
  print(mixList);

  var number = mixList.map<int>((value) => int.parse(value.toString())).toList();
  print(number);
  print(number.runtimeType);
}