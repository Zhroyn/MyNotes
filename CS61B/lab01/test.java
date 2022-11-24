public class test {
    public int n;

    /** Constructer */
    public test (int n) {
        n = n;
    }

    public static void main(String[] args) {
        Dog[] d = new Dog[1];
        d[0].makeBark();
    }
}

class Dog {
    public int weightInPounds;

    public Dog(int w) {
        weightInPounds = w;
    }

    public void makeBark() {
        System.out.println("bark!");
    }
    public void makeNoise() {
        if (weightInPounds < 10) {
            System.out.println("yipyipyip!");
        } else if (weightInPounds < 30) {
            System.out.println("bark. bark.");
        } else {
            System.out.println("woof!");
        }
    }
    public Dog maxDog(Dog d1, Dog d2) {
        if (weightInPounds > d2.weightInPounds) {
            return d1;
        }
        return d2;
    }
}