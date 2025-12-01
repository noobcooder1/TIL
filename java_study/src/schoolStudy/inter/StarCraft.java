package schoolStudy.inter;
/*
- StarCraft를 상속받아 공겨기능을 처리하는 Terran, Zerg, Protos 클래스를 작성하여라.
- 단, StarCraft는 자식의 이름을 파라미터로 받아 처리하는 생성자를 가지고 있다.
- 단, main()에서 자식클래스는 업캐스팅하여 객체 생성하되 배열로 선언하여라.
* */

public class StarCraft {
    protected String name;

    StarCraft(String name) {
        this.name = name;
    }

    public void Start(String s) {
        System.out.println(s + "시작");
    }

    public void attack() {
        System.out.println("스타 공격!!");
    }
}

class Terran extends StarCraft {
    Terran(String name) {
        super(name);
    }

    @Override
    public void attack() {
        System.out.println("스타 공격!!");
    }
}
