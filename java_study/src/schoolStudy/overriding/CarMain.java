package schoolStudy.overriding;

public class CarMain {
    public static void main(String[] args) {

        Car tank = new Car("tank", 1, 2147483647);
        System.out.println(tank.getName() + "의 가격은 " + tank.getPrice() + " 원이고, 속도는 초당 " + tank.getSpeed() + " 광년의 거리를 움직입니다.");
        HybridWaterCar hwc1 = new HybridWaterCar(2147483647, 2147483647, 2147483647);
        hwc1.showGauge();
    }
}
