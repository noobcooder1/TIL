package schoolStudy.inter;

public class Audio implements Remocon {
    private int vol;

    public void turnOn() {
        System.out.println("오디오를 켠다");
    }

    public void turnOff() {
        System.out.println("오디오를 끈다");
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
        System.out.println("현재 오디오 불륨 : " + this.vol);
    }
}
