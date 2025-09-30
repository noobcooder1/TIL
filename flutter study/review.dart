void main() {
 List<String> name = [];

 name.add('kim');
 name.add('park');
 name.add('lee');
 print (name);
}

void printName(name) {

  for (int i = 0; i < name.length; i++) {
    print(name[i]);
  }
}