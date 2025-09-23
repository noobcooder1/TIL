void main() {
  var num = [1, 2, 3, 4, 5];
  for (var i = 0; i < num.length; i++) {
    print(num[i]);
  }

  for (var n in num) {
    print(n);
  }

  hello();
  
  }

  

  void hello() {
    print('hello');
  }
