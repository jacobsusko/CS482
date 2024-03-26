import java.security.MessageDigest;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.NoSuchAlgorithmException;
import java.security.InvalidKeyException;

public class codeBreaker {
    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
        String aGuessedPassword = "password123";
        byte[] embeddedCiphertext = new byte[] { 0x0 };

        MessageDigest mDigest = MessageDigest .getInstance("SHA-256");
        byte[] pwdHashValue = mDigest.digest(aGuessedPassword.getBytes());
        System.out.println(pwdHashValue);

        byte[] key = pwdHashValue;
        SecretKeySpec sks = new SecretKeySpec(key, "AES");

        Mac mac  = Mac.getInstance("HmacSHA256");
        mac.init(sks);
        byte[] macValue = mac.doFinal(embeddedCiphertext);
        
        System.out.println(pwdHashValue);
    }
}