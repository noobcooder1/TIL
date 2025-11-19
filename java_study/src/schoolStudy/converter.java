//다음은 단위를 변환하는 추상클래스 Converter이다.

package schoolStudy;

import java.util.Scanner;

abstract class converter {
    abstract protected double convert(double src);
    abstract protected String getSrcString();
    abstract protected String getDestString();
    protected double ratio;
    public void run() {
        Scanner scanner = new Scanner(System.in);
        System.out.println(getSrcString()+ "을(를) " + getDestString() + "로 바꿉니다.");
        System.out.println(getSrcString()+ "을(를) 입력하세요. ");
        double val = scanner.nextDouble();
        double res = convert(val);
        System.out.println("변환 결과 : " + res + getDestString() + " 입니다.");
        scanner.close();
    }
}

class Won2Dollar extends converter {
    private final int won;

    Won2Dollar (int won) {
       this.won = won;
    }

    public String getSrcString() {
        return "Won";
    }
    public String getDestString() {
        return "Dollor";
    }
    public double convert(double src) {
        return  src / won;
    }
}
