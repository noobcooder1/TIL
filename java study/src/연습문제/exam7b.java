package 연습문제;

public class exam7b {
    public static void main(String[] args) {
        int[] score = {100, 99, 96, 93, 98, 95, 94, 97, 92};
        String[] student = {"kim", "lee", "park", "seo", "yoon", "na", "choi", "jung", "ju"};

        System.out.println("1등은 " + score[printTopScore(score, student)] + "점을 받은 " + student[printTopScore(score, student)] + "입니다.");
        printSecondScore(score, student);
    }

    public static int printTopScore(int[] score, String[] student) {
        int topIndex = 0;
        for (int i = 0; i < score.length; i++) {
            if(score[i] > score[topIndex]) {
                topIndex = i;
            }
        }
        return topIndex;
    }

    public static void printSecondScore(int[] score, String[] student) {
        int SecondIndex = -1;
        int topIndex = printTopScore(score, student);
        for (int i = 0; i < score.length; i++) {
            if(i == topIndex) {
                continue;
            }
            if(SecondIndex == -1 || score[i] > score[SecondIndex]) {
                SecondIndex = i;
            }
        }
        if(SecondIndex == -1) {
            System.out.println("2등은 없습니다.");
        }
        else {
            System.out.println("2등은 " + score[SecondIndex] + "점을 받은 " + student[SecondIndex] + "입니다.");
        }
    }
}
