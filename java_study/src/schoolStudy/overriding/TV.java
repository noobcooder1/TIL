package schoolStudy.overriding;

//실습 : 다음 TVMain class의 main() 메소드와 실행결과를 참고하여 TV클래스를 상속받은 ColorTV 클래스를 작성하라.
//출력결과 : 32인치 1024컬러

public class TV {
    private int size;
    public TV(int size) {
        this.size = size;
    }
    protected int getSize() {
        return size;
    }
}

class ColorTV extends TV {
    private int color;
    ColorTV (int size, int color) {
        super(size);                  //super() -> 부모를 가리킴. 그래서 super(size) 사용할경우 부모생성자인 TV를 사용하여 size설정
        this.color = color;
    }
    protected int getColor() {
        return color;
    }
    public void printProperty() {
        System.out.println(getSize() + "인치 " + color + "컬러");
    }
}

class IPTV extends ColorTV {
    private int ip;
    IPTV(int size, int color, int ip) {
        super(size, color);
        this.ip = ip;
    }

    protected int getIp() {
        return ip;
    }

    //오버라이딩을 한 것임. 부모클래스의 메서드를 자식 메서드에 맞게 변경
    public void printProperty() {
        System.out.println(getSize() + "인치 " + getColor() + "컬러 " + ip + "ip");
    //오버라이딩을 하기전의 부모클래스 메서드를 가져오려면 super.을 붙여야한다. 그리고 메서드 안에 써야한다. 그렇지않으면 컴파일에러발생
        super.printProperty();
    }
}