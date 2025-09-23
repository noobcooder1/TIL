enum ColorType {
  red(1),
  green(2),
  blue(3);

  final int code;
  const ColorType(this.code);
  }

void main() {
  var userInfo = {
  'name' : '개발하는남자',
  'age' : '30',
  'address' : '서울시 강남구',
  };
  Map<String, Map<String, String>> User = {};

  User['123'] = userInfo;
  print(User['123']);

  var selectedColor = ColorType.red;
  print(selectedColor.code);
  if (selectedColor.code == 1) {
    print('빨간색');
  }
}