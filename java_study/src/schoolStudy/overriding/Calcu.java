package schoolStudy.overriding;

abstract public class Calcu {
    protected int a;
    protected int b;


    public void setValue(int a, int b) {
        this.a = a;
        this.b = b;
    }

    abstract protected int calculate();
}


class Add extends Calcu {
    public int calculate() {
        return a + b;
    }
}

class Sub extends Calcu {
    public int calculate() {
        return a - b;
    }
}

class Mul extends Calcu {
    public int calculate() {
        return a * b;
    }
}

class Div extends Calcu {
    public int calculate() {
        return a / b;
    }
}
