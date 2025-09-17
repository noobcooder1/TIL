package Durango;

import java.util.Scanner;
import java.util.ArrayList;


public class durangoMarketHome {
    static ArrayList<durangoProductRegistration> productList = new ArrayList<>();
    static Scanner s1 = new Scanner(System.in);

    public static void main(String[] args) {

        while(true) {
            System.out.println("어서오세요 듀랑고 마켓입니다! 원하시는 업무를 번호로 입력해주세요!!\n" +
                    "1.물건판매등록 2.물건 검색 3.나가기");
            int work = s1.nextInt();
            s1.nextLine();

            if (work == 1) {
                productRegistration();
            }

            if (work == 2) {
                productSearch();
            }

            if (work == 3) {
                System.out.println("안녕히가세요.");
                break;
            }
        }
    }

    public static void productRegistration() {
        System.out.println("등록할 상품의 이름을 입력하세요.");
        Scanner s1 = new Scanner(System.in);
        String name = s1.nextLine();

        System.out.println("상품의 가격을 입력하세요.");
        double price = s1.nextDouble();
        s1.nextLine();

        if (price < 1) {
            System.out.println("그 가격으로는 등록할 수 없습니다.");
            System.exit(0);
        }

        System.out.println("상품의 수량을 입력하세요.");
        int amount = s1.nextInt();
        durangoProductRegistration product = new durangoProductRegistration(name, price, amount);
        System.out.println("성공적으로 등록되었습니다!\n");
        productList.add(product);
    }

    public static void productSearch() {
            System.out.println("검색할 품목을 입력하세요.");
            String productName = s1.nextLine();
            boolean productFound = false;
            for (durangoProductRegistration product : productList) {
                if(product.name.equals(productName)) {
                    productFound = true;
                    System.out.println("원하시는 물건을 찾았습니다.");
                    System.out.println("이름 : " + product.name + " 가격 : " + product.price + " 수량 : " + product.amount);
                    System.out.println("구매하시겠습니까? 구매하시려면 1을 아니라면 2를 입력하세요.");
                    int buy = s1.nextInt();
                    if (buy != 1) {
                        break;
                    }
                    else {
                        System.out.println("구매하실 수량을 입력하세요.");
                        int wantAmount = s1.nextInt();
                        if(wantAmount > product.amount) {
                            System.out.println("재고가 부족합니다!");
                        }
                        else {
                            System.out.println("가격은 " + product.price * wantAmount + "티스톤 입니다.");
                            product.decreaseAmount(wantAmount);
                        }
                    }

                }
            }
            if (!productFound) {
                System.out.println("찾으시는 물품이 없습니다!");
            }
        }
    }

