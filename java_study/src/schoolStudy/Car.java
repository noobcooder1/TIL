package schoolStudy;
/* 인스턴스 멤버 : 객체마다 가지고 있는 멤버, 객체를 생성한 후 사용 할 수 있는 필드와 메소드
    - 인스턴스 필드 : 영역의 객체마다 가지고 있는 멤버, 객체마다 다른 데이터를 저장
    - 인스턴스 메소드 : 객체가 있어야 호출 가능한 메소드, 클래스코드에 위치하지만 객체마다 가지고있는 메소드

  클래스 멤버(정적멤버) : 객체와 상관 없는 멤버, 클래스코드에 위치, static을 사용, this 사용불가
    - 정적필드 및 상수 : 객체없이 클래스만으로도 사용 가능, 객체들끼리 공유
    - 정적 메소드 : 객체 없이 클래스만으로도 호출 가능
 */

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
