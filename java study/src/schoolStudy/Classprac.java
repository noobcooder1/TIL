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

class Car {
    String name;
    int price;
    String use;
    int speed;

    public Car() {
        name = "tank";
        price = 1;
        speed = 200;
    }

    public Car(String name) {
        this.name = name;
        price = 1;
        speed = 240;
    }

    public Car(String name, int price, int speed) {
        this.name = name;
        this.price = price;
        this.speed = speed;
    }

    //오버로딩 : 동일 클래스내에 같은 이름으로 여러개의 메소드나 생성자가 여러개 정의되어 있는 것을 말함.
    //오버로딩의 구분 : 메소드의 파라미터의 갯수와 데이터 타입으로 구분

    public void speedUp(int booster) {
        speed += booster;
    }

    public void speedDown(int breakk) {
        if (speed <= 0) {
            stop();
        }
        else {
            speed -= breakk;
        }
    }

    public void stop() {
        speed = 0;
    }

    public void printCar(String name, int price, int speed) {
        System.out.println(name + "의 가격은" + price + "원입니다.");
        System.out.println("속도는 " + speed + " 입니다.");
    }
}
