package 연습문제;
import java.util.Scanner;
import java.util.Arrays;

public class exam5a {
    public static void main(String[] args) {
        String[] product = {"소모품", "아이템", "능력", "책", "재화", "영혼", "정보", "기타"};
//        product p1 = new product();
//        p1.name = "소모품";
//        p1.price = 1000;
        Scanner s1 = new Scanner(System.in);
//        for (int i = 0; i < product.length; i++) {
//            System.out.printf("%s ", product[i]);
//        }
        for (String item : product) {
            System.out.printf("%s ", item);
        }
        System.out.println("\n구매하실 항목을 입력하세요.");
        String choice = s1.nextLine();
//        for (int i = 0; i < product.length; i++) {
//            if(choice.equals(product[i])) {
//                change(choice);
//            }
//        }
        if (Arrays.asList(product).contains(choice)) {
            int productPrice = result(choice, product);
            System.out.println(choice + "의 가격은 " + productPrice + "코인입니다. 내실 금액을 입력하세요.");
            int pay = s1.nextInt();
            System.out.printf("%s ", choice);
            change(pay, productPrice);
        }
        else {
            System.out.println("그 품목은 없습니다!");
        }
    }

    public static void change (int pay, int productPrice) {
        int change = pay - productPrice;
        if (pay < productPrice) {
            System.out.println(" 구매 실패!!!  물건 가격보다 내신 돈이 더 적습니다. 돈을 더 내시거나 하십쇼.");
        }
        else if (pay == productPrice) {
            System.out.println("구매 성공!!!  거스름돈은 없습니다.");
        }
        else {
            System.out.println("구매 성공!!!  거스름돈은 " + change + "코인입니다.");
        }
    }

    public static int result(String choice, String[] product) {
        int[] price = {1600, 9100, 19000, 8700, 7600, 25400, 1500, 900};
//        int productprice = 0;
//        for (int i = 0; i < product.length; i++) {
//            if (Arrays.asList(product).contains(choice)) {
//                productprice = price[i];
//            }
//        }
        int index = Arrays.asList(product).indexOf(choice);

        if (index != -1) {
            return price[index];
        }
        else {
            return 0;
        }
    }

}

