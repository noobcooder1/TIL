package schoolStudy.overriding;

/* 부모 클래스의 생성자 상속
자식 클래스의 인스턴스를 생성하려면 가장 먼저 부모클래스의 생성자 호출 -> 자식클래스의 생성자 호출
 */

public class CellPhone {
    String model;
    String color;

    public void powerOn() {
        System.out.println("전원을 켜다.");
    }

    public void powerOff() {
        System.out.println("전원을 끄다.");
    }

    public void bell() {
        System.out.println("벨이 울리다.");
    }

    public void sendVoice(String voice) {
        System.out.println("me : " + voice);
    }
}
