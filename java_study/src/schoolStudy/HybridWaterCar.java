package schoolStudy;

public class HybridWaterCar extends HybridCar {
    private int water;

    HybridWaterCar(int fuel, int electric, int water) {
        super(fuel, electric);
        this.water = water;
    }

    public int getWater() {
        return water;
    }

    public void showGauge() {
        System.out.println("잔여 연료량 : " + getFuel() + " 잔여 전기량 : " + getElectric() + " 잔여 물량 : " + water);
        super.showGauge();
    }
}