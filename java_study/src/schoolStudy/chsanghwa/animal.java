package schoolStudy.chsanghwa;

/* 추상 메서드 : 메서드 선언만 통일하고 실행 내용은 실제 클래스마다 달라야 하는경우
    - abstract 키워드로 선언되고 중괄호가 없는 메소드(선어만하고 구현부가 없는 메소드)
    - 자식클래스는 반드시 재정의해서 실행 내용을 채워야한다.

   추상클래스 : 여러 클래스의 공통된 특성 (필드, 메서드)를 추출해서 선언한 것을 추상클래스라고한다.
    - 실체클래스(객체 생성용 클래스)들의 공통적인 특성을 추출해서 선언
    - 추상 클래스와 실체 클래시는 부모, 자식 클래스로서 상속관계를 가짐
    - 실체 클래스와 인스턴스 생성 불가능하여 추상클래스를 사용하려면 자식클래스에서 추상 클래스를 상속 후 자식클래스의 인스턴스를 생성해야 함
    - 추상 : abstract 키워드를 사용
    - 직접 객체를 생성할 수 없지만 자식 객체가 생성될 때 객체화 된다
    - 단 하나의 추상메소드를 포함   */

abstract public class animal {
    public String kind;

    public void breath() {
        System.out.println("숨을쉰다");
    };

    abstract public void sound();

}

class dog extends animal {
    public void breath() {
        System.out.println("hak hek hak hek");
        super.breath();
    }

    public void sound() {
        System.out.println("wal wal wal wal");
    }

}

class cat extends animal {
    public void breath() {
        System.out.println("fu fu fu fu");
    }

    public void sound() {
        System.out.println("yaong yaong");
    }

}
