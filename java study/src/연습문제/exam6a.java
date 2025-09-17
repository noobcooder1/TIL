package 연습문제;

public class exam6a {
    public static void main(String[] args) {
        int[] score = {100, 100, 100, 100};
        double[] score1 = {99.99, 100.1, 100.0, 1000.0};

        for (int i = 0; i < score1.length; i++) {
            System.out.printf("%.1f ", score1[i]);
        }
    }
}
