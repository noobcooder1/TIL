package schoolStudy.overriding;

public class TVMain {
    public static void main(String[] args) {
        ColorTV myTV = new IPTV(32, 1024, 130121324);      //32인치 1024컬러
        myTV.printProperty();
    }
}
