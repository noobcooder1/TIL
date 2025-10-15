package schoolStudy;

public class Car {
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

        public Car(String name, int price) {
            this(name);
            this.price = price;
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
