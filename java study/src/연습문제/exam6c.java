package 연습문제;

public class exam6c {
    public static void main(String[] args) {
        String[] visiter = {"kim", "lee", "park"};
        int[] money = {980000000, 200000000, 300023000};

        for(int i = 0; i < visiter.length; i++) {
            System.out.println("방문자 " +  visiter[i] + "의 재산은 " + money[i] + "달러입니다." );
        }
    }
}
