package Durango;
import java.util.ArrayList;

public class durangoProductRegistration {

    String name;
    double price;
    int amount;

    public durangoProductRegistration(String name) {
        this.name = name;
    }

    public durangoProductRegistration(String name, double price, int amount) {
        this(name);            //this()를 사용해서 위에있는 생성자를 가져 올 수 있다.
        this.price = price;
        this.amount = amount;
    }

    public void printProduct() {
        System.out.println("상품명 : " + name + " 가격 : " + price + " 수량 : " + amount);
    }

    public void decreaseAmount(int wantAmount) {
        amount -= wantAmount;
    }
}
