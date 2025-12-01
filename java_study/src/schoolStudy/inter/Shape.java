package schoolStudy.inter;
//인터페이스는 상속과 조금 다르다. 상속은 클래스당 한 번 받지만 인터페이스는 클래스안에 여러개가 구현가능
//그리고

public interface Shape {
    final double PI = 3.14;

    void draw();

    double getArea();

    default public void redraw() {
        System.out.print("--- 다시 그립니다.");
        draw();
    }
}
