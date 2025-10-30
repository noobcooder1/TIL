package 연습문제;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class finalExam5a {
    public static void main(String[] args) {
        // 1. 데이터 구조 개선: Map을 사용하여 상품명과 가격을 함께 관리합니다.
        // 이제 상품과 가격이 짝이 안 맞을 걱정이 없습니다.
        Map<String, Integer> productMap = new HashMap<>();
        productMap.put("소모품", 1600);
        productMap.put("아이템", 9100);
        productMap.put("능력", 19000);
        productMap.put("책", 8700);
        productMap.put("재화", 7600);
        productMap.put("영혼", 25400);
        productMap.put("정보", 1500);
        productMap.put("기타", 900);

        Scanner s1 = new Scanner(System.in);

        // Map의 keySet()을 이용해 상품 목록을 보여줍니다.
        System.out.println("--- 판매 목록 ---");
        for (String productName : productMap.keySet()) {
            System.out.printf("%s ", productName);
        }
        System.out.println("\n-----------------");

        System.out.println("구매하실 항목을 입력하세요.");
        String choice = s1.nextLine();

        // 2. 로직 개선: containsKey로 상품 존재 여부를 확인합니다.
        if (productMap.containsKey(choice)) {
            // 3. 효율성 개선: get()으로 가격을 한 번만 조회하여 변수에 저장합니다.
            int productPrice = productMap.get(choice);

            System.out.println(choice + "의 가격은 " + productPrice + "원 입니다. 내실 금액을 입력하세요.");
            int pay = s1.nextInt();

            // 4. 역할 분리: 계산 로직은 change 메소드에 맡깁니다.
            purchaseResult(choice, pay, productPrice);
        }
        else {
            System.out.println("그 품목은 없습니다!");
        }
    }

    /**
     * 지불 금액과 상품 가격을 비교하여 구매 결과와 거스름돈을 출력합니다.
     * @param choice 구매한 상품 이름
     * @param pay 지불한 금액
     * @param productPrice 상품의 실제 가격
     */
    public static void purchaseResult(String choice, int pay, int productPrice) {
        if (pay < productPrice) {
            System.out.println("구매 실패! 금액이 " + (productPrice - pay) + "원 부족합니다.");
        }
        else {
            System.out.print(choice + " 구매 성공! ");
            int change = pay - productPrice;
            if (change == 0) {
                System.out.println("거스름돈은 없습니다.");
            } else {
                System.out.println("거스름돈은 " + change + "원입니다.");
            }
        }
    }
}