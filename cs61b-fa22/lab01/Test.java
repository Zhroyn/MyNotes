import java.util.ArrayList;
import java.util.HashMap;

public class Test {

    public static void main(String[] args) {
        HashMap M = new HashMap();
        M.put(12, "sad");
        M.put("asd", 1);
        HashMap m = new HashMap();
        m.put(new int[]{1,2}, 2);
        M.put(m, 55);
        System.out.println(M.toString());
    }
}

