import java.math.BigInteger;

/**
 * @author Jacob Susko
 * @author Justin Lacombe
 * @date 2/16/2024
 */

public class CS482_project3_justin_jacob_encrypt {




    public static void main(String[] args) {
        String k = "DC37471D600000000000000000000003";
        BigInteger k2 =  new BigInteger(k, 16);
        byte[] kTemp =  k2.toByteArray();
        byte[] key = new byte[80];
        for (int p = 1; p < kTemp.length; p++) {
            key[p-1] = kTemp[p];
        }
    }

}
