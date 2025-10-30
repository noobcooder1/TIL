package schoolStudy;

public class Classprac {
    public static void main(String[] args) {
        Car car1 = new Car();
        //Car car1;
        //car1 = new Car(); 이 코드도 가능하긴하지만, 두 번째 줄이 샐행되기 전까지는 값이 null
        //이므로 오류가 발생 할 수 있다. 그래서 조건이 있지 않는 이상은 그냥 한 줄에 쓰는걸 권장함.

        Car car2 = new Car("bugati");
        Car car3 = new Car("jeep");
        Car car4 = new Car("fighter", 10, 1000);

        car1.speedUp(100);
        car1.stop();
        car2.speedUp(100);
        car4.speedUp(3000);
        car1.printCar(car1.name, car1.price, car1.speed);
        car2.printCar(car2.name, car2.price, car2.speed);
        car3.printCar(car3.name, car3.price, car3.speed);
        car4.printCar(car4.name, car4.price, car4.speed);
    }
}
