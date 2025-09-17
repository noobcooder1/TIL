package 연습문제;

public class exam6d {
    public static void main(String[] args) {
        String[] student = {"kim", "lee", "park", "seo", "yoon", "na", "choi", "jung", "ju"};
        int[] score = {100, 99, 96, 93, 98, 95, 94, 97, 92};

        printScore(student, score);
    }

    public static void printScore(String[] student, int[] score) {
        int top = 0;
        for (int i = 0; i < student.length; i++) {
            if (score[top] < score[i]) {
                top = i;
            }
        }
        System.out.println("최고점을 받은 학생은 " + student[top] + "입니다. 점수는 " + score[top] + "점 입니다.");
    }
}
