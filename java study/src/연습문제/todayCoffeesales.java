package 연습문제;

public class todayCoffeesales {
    public static void main(String[] args) {
        coffee c1 = new coffee("아메리카노", 32, 1);
        c1.printCoffee();
    }
}

class coffee {
    String name;
    int amount;
    int price;

    public coffee(String name, int amount, int price) {
        this.name = name;
        this.amount = amount;
        this.price = price;
    }

    public void printCoffee() {
        System.out.println("커피이름 : " + name);
        System.out.println("판매량 : " + amount);
        System.out.println("가격 : " + price);
    }
}
