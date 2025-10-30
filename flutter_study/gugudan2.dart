void main() {
printGuGuDan(1, 10);

}

void printGuGuDan(int n, int m) {
for (var x = n; x <= m; x++) {
  printDan(x);
  }
}



printDan(int n) {
  for (var i = 1; i <= 9; i++) {
    print('$n * $i = ${n * i}');
 }
}
