import java.security.MessageDigest;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.NoSuchAlgorithmException;
import java.security.InvalidKeyException;

public class codeBreaker_task1 {

    private static byte[] givenMac = {(byte) 0xBC, (byte) 0xB0, (byte) 0x78, (byte) 0x41, (byte) 0xAA, (byte) 0xD0, 
        (byte) 0x06, (byte) 0x68, (byte) 0xDD, (byte) 0xA4, (byte) 0x74, (byte) 0x06, (byte) 0xD7, (byte) 0x1A, 
        (byte) 0x2B, (byte) 0xD2, (byte) 0x9B, (byte) 0x0E, (byte) 0xDB, (byte) 0x0D, (byte) 0xF9, (byte) 0xCE, 
        (byte) 0xF4, (byte) 0xA7, (byte) 0xF9, (byte) 0x51, (byte) 0x6C, (byte) 0x99, (byte) 0xFC, (byte) 0xB6, 
        (byte) 0x95, (byte) 0xF8};

    private static byte[] givenC = {(byte) 0x34, (byte) 0x3B, (byte) 0x71, (byte) 0x62, (byte) 0xBA, (byte) 0x9F, 
        (byte) 0x55, (byte) 0xB8, (byte) 0xD9, (byte) 0x88, (byte) 0x71, (byte) 0x98, (byte) 0x24, (byte) 0x41,
        (byte) 0x3E, (byte) 0x4D, (byte) 0xA4, (byte) 0xBD, (byte) 0x1A, (byte) 0xE1, (byte) 0x2C, (byte) 0xAE, 
        (byte) 0x2C, (byte) 0xFF, (byte) 0x1D, (byte) 0x4E, (byte) 0x1A, (byte) 0x9E, (byte) 0x94, (byte) 0x8A, 
        (byte) 0x4D, (byte) 0x07, (byte) 0x71, (byte) 0x5D, (byte) 0xC6, (byte) 0x1F, (byte) 0xEF, (byte) 0x91, 
        (byte) 0x09, (byte) 0x67, (byte) 0xDA, (byte) 0xFA, (byte) 0x37, (byte) 0x96, (byte) 0x11, (byte) 0xE1, 
        (byte) 0x67, (byte) 0xD6, (byte) 0x3E, (byte) 0xA1, (byte) 0x5E, (byte) 0x58, (byte) 0x0B, (byte) 0x81, 
        (byte) 0xDD, (byte) 0xB2, (byte) 0xAF, (byte) 0x5D, (byte) 0xDE, (byte) 0xDE, (byte) 0x9D, (byte) 0x82, 
        (byte) 0xB3, (byte) 0x72, (byte) 0x36, (byte) 0x86, (byte) 0xA6, (byte) 0x72, (byte) 0xEA, (byte) 0x3E, 
        (byte) 0x5A, (byte) 0xA0, (byte) 0x21, (byte) 0x4E, (byte) 0x94, (byte) 0xBF, (byte) 0x51, (byte) 0x12, 
        (byte) 0xBE, (byte) 0xFC, (byte) 0xB6, (byte) 0x07, (byte) 0x3D, (byte) 0x51, (byte) 0x36, (byte) 0xCF, 
        (byte) 0x76, (byte) 0x93, (byte) 0xAB, (byte) 0xC6, (byte) 0x6C, (byte) 0x7B, (byte) 0x5F, (byte) 0xC8, 
        (byte) 0x16, (byte) 0xA2, (byte) 0x11, (byte) 0xC0, (byte) 0xE6, (byte) 0x87, (byte) 0x9E, (byte) 0xAB, 
        (byte) 0x40, (byte) 0x56, (byte) 0xA4, (byte) 0xB7, (byte) 0xA5, (byte) 0x20, (byte) 0x44, (byte) 0xBF, 
        (byte) 0xB0, (byte) 0xB7, (byte) 0x5B, (byte) 0x43, (byte) 0x4A, (byte) 0x02, (byte) 0x19, (byte) 0x09, 
        (byte) 0x1D, (byte) 0xB2, (byte) 0x30, (byte) 0xBB, (byte) 0x15, (byte) 0xCE, (byte) 0x1C, (byte) 0x97, 
        (byte) 0xD8, (byte) 0x77, (byte) 0xBC, (byte) 0x42, (byte) 0x87, (byte) 0x14, (byte) 0x93, (byte) 0x85, 
        (byte) 0xD2, (byte) 0x0A, (byte) 0x7D, (byte) 0xC4, (byte) 0x44, (byte) 0x0E, (byte) 0x82, (byte) 0x35, 
        (byte) 0x3B, (byte) 0xC4, (byte) 0x40, (byte) 0x78, (byte) 0x7A, (byte) 0x59, (byte) 0xA1, (byte) 0x59, 
        (byte) 0x18, (byte) 0x09, (byte) 0x22, (byte) 0x17, (byte) 0x68, (byte) 0xC0, (byte) 0xFC, (byte) 0x7A, 
        (byte) 0x5F, (byte) 0x67, (byte) 0x5B, (byte) 0x2A, (byte) 0xB3, (byte) 0xFC, (byte) 0x53, (byte) 0xBC, 
        (byte) 0xE0, (byte) 0x92, (byte) 0xFF, (byte) 0x0D, (byte) 0x84, (byte) 0x74, (byte) 0x31, (byte) 0x1F, 
        (byte) 0xF5, (byte) 0x16, (byte) 0x4F, (byte) 0x17, (byte) 0x50, (byte) 0x8D, (byte) 0x95, (byte) 0x51, 
        (byte) 0x06, (byte) 0xF7, (byte) 0xBC, (byte) 0xDA, (byte) 0x15, (byte) 0x05, (byte) 0x76, (byte) 0xB5, 
        (byte) 0x10, (byte) 0x78, (byte) 0xA4, (byte) 0xA1, (byte) 0xF1, (byte) 0x45, (byte) 0xF1, (byte) 0x6E, 
        (byte) 0x78, (byte) 0x2C, (byte) 0x3A, (byte) 0x01, (byte) 0x4E, (byte) 0x82, (byte) 0x68, (byte) 0x4F, 
        (byte) 0xE8, (byte) 0x12, (byte) 0x69, (byte) 0xDD, (byte) 0x00, (byte) 0x77, (byte) 0x17, (byte) 0xEC, 
        (byte) 0x95, (byte) 0x76, (byte) 0xBC, (byte) 0x8C, (byte) 0x43, (byte) 0xC5, (byte) 0x99, (byte) 0x53, 
        (byte) 0xBA, (byte) 0x86, (byte) 0x4C, (byte) 0x6B, (byte) 0x46, (byte) 0x4A, (byte) 0x35, (byte) 0x82, 
        (byte) 0xE1, (byte) 0x10, (byte) 0xEE, (byte) 0x2A, (byte) 0x73, (byte) 0x4D, (byte) 0x80, (byte) 0x55, 
        (byte) 0xDC, (byte) 0xBC};

    private static byte[] working = {0x2, 0x12};


    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {

        String template = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
        int size = template.length();

        for (int i = 0; i < size; i++) {// We are interested in alphanumeric characters only
            for (int j = 0; j < size; j++) {// We are interested in alphanumeric characters only
                for (int k = 0; k < size; k++) { // We are interested in alphanumeric characters only
                    String aGuessedPassword = "" + template.charAt(i) + template.charAt(j) + template.charAt(k);

                    MessageDigest mDigest = MessageDigest.getInstance("SHA-256");
                    byte[] pwdHashValue = mDigest.digest(aGuessedPassword.getBytes());
                    
                    if (pwdHashValue[0] == 0x12 && pwdHashValue[1] == 0x2) {
                        System.out.println(aGuessedPassword);
                    }
                }
            }
        }


        byte[] key = new byte[16];
        for (int i = 0; i < 0xFF; i++) {
            for (int j = 0; j < 0xFF; j++) {
                byte first = (byte) i;
                byte second = (byte) j;
                key[0] = (byte) (first ^ 0x23);
                key[1] = (byte) (second ^ 0x8E);
                key[2] = (byte) (key[1] ^ 0x60);
                key[3] = (byte) (key[0] ^ 0xE1);
                key[4] = (byte) (key[3] ^ 0xD2);
                key[5] = (byte) (key[2] ^ 0x96);
                key[6] = (byte) (key[5] ^ 0x38);
                key[7] = (byte) (key[4] ^ 0xC7);
                key[8] = (byte) (key[7] ^ 0xA5);
                key[9] = (byte) (key[6] ^ 0xC0);
                key[10] = (byte) (key[9] ^ 0x22);
                key[11] = (byte) (key[8] ^ 0x74);
                key[12] = (byte) (key[11] ^ 0x4F);
                key[13] = (byte) (key[10] ^ 0x31);
                key[14] = (byte) (key[13] ^ 0x5B);
                key[15] = (byte) (key[12] ^ 0xCD);

                SecretKeySpec sks = new SecretKeySpec(key, "AES");
                Mac mac  = Mac.getInstance("HmacSHA256");
                mac.init(sks);
                byte[] macValue = mac.doFinal(givenC);
                        
                for (int k = 0; k < macValue.length; k++) {
                    if ((k == macValue.length - 1) && (macValue[k] == givenMac[k])) {
                        System.out.printf("%X  %X", first, second);
                    } else if (macValue[k] != givenMac[k]) {
                        break;
                    }
                }
            }
        }
    }
}
