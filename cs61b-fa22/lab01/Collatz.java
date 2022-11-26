/**
 * Class that prints the Collatz sequence starting from a given number.
 *
 * @author YOUR NAME HERE
 */
public class Collatz {

    /**
     * Returns the nextNumber in a Collatz sequence.
     */
    public static int nextNumber(int n) {
        return (n % 2 == 0) ? n / 2 : (3 * n + 1);
    }

    public static void main(String[] args) {
        int n = 5;
        System.out.print(n + " ");

        // Some starter code to test
        while (n != 1) {
            n = nextNumber(n);
            System.out.print(n + " ");
        }
        System.out.println();

    }
}

