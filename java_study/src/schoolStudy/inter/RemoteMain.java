package schoolStudy.inter;

public class RemoteMain {
    public static void main(String[] args) {
        Remocon[] rc = new Remocon[2];
        rc[0] = new Audio();
        rc[1] = new TV();

        rc[0].turnOn();
        rc[0].setVol(5);
        rc[0].turnOff();

        rc[1].turnOn();
        rc[1].setVol(12);
        rc[1].turnOff();
    }
}
