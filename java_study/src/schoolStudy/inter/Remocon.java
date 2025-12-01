package schoolStudy.inter;

public interface Remocon {
    static int maxVol = 10;
    static int minVol = 0;

    public void turnOn();
    public void turnOff();
    public void setVol(int vol);
}
