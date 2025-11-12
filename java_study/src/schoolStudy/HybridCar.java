package schoolStudy;

public class HybridCar {
    private int fuel;
    private int electric;

    HybridCar(int fuel, int electric) {
        this.fuel = fuel;
        this.electric = electric;
    }

    public int getFuel() {
        return fuel;
    }

    public int getElectric() {
        return electric;
    }

    protected void showGauge() {
        System.out.println(" 잔여 연료량 : " + fuel + " 잔여 전기량 : " + electric);
    }
}
