package Javaweek1;

public class study1 {
    public static void main(String[] args) {
        for(int hang = 1; hang < 10; hang++) {
            for(int dan = 1; dan < 10; dan++) {
                System.out.printf(dan + " * " + hang + " = " + dan * hang + "\t\t");
            }
            System.out.println();
        }
    }
}
