package schoolStudy;

public class CarMain {
    public static void main(String[] args) {

        Car tank = new Car("tank", 1, 500);
        System.out.println(tank.name + "의 가격은" + tank.price + "원이고, 속도는 초당" + tank.speed + "광년의 거리를 움직입니다.");
    }
}
