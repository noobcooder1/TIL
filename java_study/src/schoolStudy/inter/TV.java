package schoolStudy.inter;

public class TV implements Remocon {
    private int vol;

    public void turnOn() {
        System.out.println("TV를 켠다");
    }

    public void turnOff() {
        System.out.println("TV를 끈다");
    }

    public void setVol(int vol) {
        if (vol > Remocon.maxVol) {
            this.vol = Remocon.maxVol;
        }
        else if (vol < Remocon.minVol) {
            this.vol = Remocon.minVol;
        }
        else {
            this.vol = vol;
        }
        System.out.println("현재 TV 불륨 : " + this.vol);
    }
}