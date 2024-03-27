import java.security.MessageDigest;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.NoSuchAlgorithmException;
import java.security.InvalidKeyException;

public class codeBreakerTask2 {
    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {

        byte[] embeddedCiphertext = new byte[] { (byte) 0xA0, (byte) 0xE2, (byte) 0x57, (byte) 0x8B, (byte) 0x13, (byte) 0x2D, (byte) 0x3C, 
            (byte) 0x3B, (byte) 0x92, (byte) 0x1C, (byte) 0xBF, (byte) 0xBF, (byte) 0x57, (byte) 0x42, (byte) 0x43, (byte) 0x19, (byte) 0xE9, 
            (byte) 0x34, (byte) 0x6C, (byte) 0xBF, (byte) 0x99, (byte) 0x15, (byte) 0x81, (byte) 0x5F, (byte) 0x71, (byte) 0x18, (byte) 0x12, 
            (byte) 0x97, (byte) 0xA0, (byte) 0x8F, (byte) 0x8A, (byte) 0xF9, (byte) 0xCE, (byte) 0x07, (byte) 0x73, (byte) 0xB6, (byte) 0xC7, 
            (byte) 0xFE, (byte) 0xD8, (byte) 0xA2, (byte) 0x2B, (byte) 0x3E, (byte) 0xFC, (byte) 0xD0, (byte) 0xD3, (byte) 0x37, (byte) 0xBF, 
            (byte) 0x3B, (byte) 0xC4, (byte) 0x1E, (byte) 0x5E, (byte) 0x42, (byte) 0x4A, (byte) 0x21, (byte) 0x00, (byte) 0x83, (byte) 0x9F, 
            (byte) 0xF7, (byte) 0xED, (byte) 0xCC, (byte) 0x8A, (byte) 0x8E, (byte) 0x60, (byte) 0x06, (byte) 0x7D, (byte) 0x57, (byte) 0xA3, 
            (byte) 0x8D, (byte) 0x6E, (byte) 0xD5, (byte) 0x69, (byte) 0x1F, (byte) 0x98, (byte) 0x98, (byte) 0xE0, (byte) 0xAE, (byte) 0xC2, 
            (byte) 0x65, (byte) 0xD5, (byte) 0x1D, (byte) 0x30, (byte) 0x25, (byte) 0x00, (byte) 0xE8, (byte) 0x99, (byte) 0x69, (byte) 0x9F, 
            (byte) 0x04, (byte) 0x01, (byte) 0xC4, (byte) 0x81, (byte) 0x34, (byte) 0xC1, (byte) 0x2D, (byte) 0x13, (byte) 0xA7, (byte) 0xCC, 
            (byte) 0x5A, (byte) 0xB7, (byte) 0xC8, (byte) 0x5C, (byte) 0x8E, (byte) 0xA4, (byte) 0x29, (byte) 0x23, (byte) 0x98, (byte) 0xE6, 
            (byte) 0x2B, (byte) 0x6A, (byte) 0x44, (byte) 0x59, (byte) 0x2E, (byte) 0x31, (byte) 0xF4, (byte) 0xBE, (byte) 0x7E, (byte) 0x43, 
            (byte) 0x45, (byte) 0xA5, (byte) 0x05, (byte) 0x4E, (byte) 0xAE, (byte) 0x8C, (byte) 0x4A, (byte) 0x8F, (byte) 0xBA, (byte) 0x6B, 
            (byte) 0x6D, (byte) 0x2A, (byte) 0x07, (byte) 0xEB, (byte) 0x82, (byte) 0x8E, (byte) 0xFB, (byte) 0xCD, (byte) 0xE9, (byte) 0x7B, 
            (byte) 0xB1, (byte) 0x5A, (byte) 0xAD, (byte) 0x3F, (byte) 0x5E, (byte) 0x4F, (byte) 0x7C, (byte) 0x3F, (byte) 0xCE, (byte) 0x79, 
            (byte) 0x7E, (byte) 0x84, (byte) 0x72, (byte) 0xAD, (byte) 0x34, (byte) 0x8A, (byte) 0xBA, (byte) 0x4A, (byte) 0xAA, (byte) 0xCE, 
            (byte) 0xE0, (byte) 0xFE, (byte) 0x32, (byte) 0xA2, (byte) 0x7F, (byte) 0xF8, (byte) 0xD7, (byte) 0xFD, (byte) 0x04, (byte) 0xF1, 
            (byte) 0xEF, (byte) 0x02, (byte) 0x4A, (byte) 0xB3, (byte) 0x2C, (byte) 0x73, (byte) 0x33, (byte) 0xD3, (byte) 0x96, (byte) 0xD6, 
            (byte) 0x93, (byte) 0x7D, (byte) 0xD9, (byte) 0xA6, (byte) 0xCA, (byte) 0xAF, (byte) 0xB3, (byte) 0xF3, (byte) 0xD6, (byte) 0xFA, 
            (byte) 0xAA, (byte) 0x8E, (byte) 0x77, (byte) 0x38, (byte) 0xD0, (byte) 0xA7, (byte) 0x78, (byte) 0xB2, (byte) 0x38, (byte) 0xFE, 
            (byte) 0x50, (byte) 0xD9, (byte) 0x4F, (byte) 0x5E, (byte) 0x04, (byte) 0x50, (byte) 0x7C, (byte) 0xC7, (byte) 0xB8, (byte) 0x29, 
            (byte) 0xED, (byte) 0xF7, (byte) 0x8D, (byte) 0x76, (byte) 0xCA, (byte) 0x89, (byte) 0x71, (byte) 0xF8, (byte) 0x06, (byte) 0x2D, 
            (byte) 0x72, (byte) 0x67, (byte) 0xF1, (byte) 0xFA, (byte) 0xD4, (byte) 0xB1, (byte) 0xAA, (byte) 0x08, (byte) 0x34, (byte) 0xC3, 
            (byte) 0x21, (byte) 0xE7, (byte) 0x97, (byte) 0x21, (byte) 0x6C, (byte) 0x79, (byte) 0xB8, (byte) 0x29, (byte) 0xAE, (byte) 0xD2, 
            (byte) 0x7D, (byte) 0x68, (byte) 0xCD };
        byte[] givenMac = new byte[] { (byte) 0x74, (byte) 0x0E, (byte) 0x55, (byte) 0x80, (byte) 0x37, (byte) 0x11, (byte) 0xCD, (byte) 0x1A,
            (byte) 0x65, (byte) 0x1A, (byte) 0x34, (byte) 0x71, (byte) 0xB5, (byte) 0xA8, (byte) 0xED, (byte) 0xE8, (byte) 0x4F, (byte) 0x44,
            (byte) 0xAB, (byte) 0x67, (byte) 0xDF, (byte) 0x2E, (byte) 0x5B, (byte) 0x8A, (byte) 0x38, (byte) 0xED, (byte) 0xF1, (byte) 0x2C,
            (byte) 0x89, (byte) 0x50, (byte) 0x98, (byte) 0x24 };

        for(char c = 'A'; c <= 'z'; ++c) {
            for(char b = 'A'; b <= 'z'; ++b) {
                for(char d = 'A'; d <= 'z'; ++d) {
                    String aGuessedPassword = "" + c + b + d;
                    MessageDigest mDigest = MessageDigest.getInstance("SHA-256");
                    byte[] pwdHashValue = mDigest.digest(aGuessedPassword.getBytes());
                }
            }
        }


        // String aGuessedPassword = "xx"; // Loop to try all passwords of size 2/3 or something, brute force
            // is it only alphabetic or also numeric/etc



        // MessageDigest mDigest = MessageDigest.getInstance("SHA-256");
        // byte[] pwdHashValue = mDigest.digest(aGuessedPassword.getBytes());
        // for (byte x : pwdHashValue) {
        //     System.out.printf("%X ", x);
        // }



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
                    byte[] macValue = mac.doFinal(embeddedCiphertext);
                            
                    for (int k = 0; k < macValue.length; k++) {
                        if ((k == macValue.length - 1) && (macValue[k] == givenMac[k])) {
                            System.out.printf("%X  %X", first, second);
                        } else if (macValue[k] != givenMac[k]) {
                            break;
                        }
                    }
                            

                            // if (pwdHashValue[0] == givenMac[0] && pwdHashValue[1] == givenMac[1]) {
                            //     System.out.println(aGuessedPassword);
                            //     return;
                            // }
                }
            }
        
        

        // Do the key generation algorithm shown in proj with v0 and v1, then k1 through k14 or whatever.
        // Use that entire key as the byte[] key and put it in SecretKeySpec
        // Then generate mac value from that sks and then compare the result (macValue) with the given 32 bytes in program
        // SecretKeySpec sks = new SecretKeySpec(key, "AES");

        // Mac mac  = Mac.getInstance("HmacSHA256");
        // mac.init(sks);
        // byte[] macValue = mac.doFinal(embeddedCiphertext);
        // // compate the found value with the 32 bytes given in the program

        // System.out.println(pwdHashValue);
    }
}

// ciphertext = the 240 byte value
// HMAC value is the 32 bytes value

// Process:
// brute force 16 bits for the first 2 bytes for key
// try all passwords and get first 2 bytes of 32 bytes and only check if the 2 first bytes of password match the 32
// Just need to try 2 letter combonations -- case sensitive
// 