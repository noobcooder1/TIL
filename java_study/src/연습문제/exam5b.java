package 연습문제;

public class exam5b {
    public static void main(String[] args) {
        int sum = 1;
        for (int i = 1; i <= 10; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.printf("%d ", sum);
                sum++;
            }
            System.out.println();
        }
    }
}
