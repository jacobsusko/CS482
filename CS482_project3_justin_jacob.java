import java.math.BigInteger;
import java.security.InvalidKeyException;
/**
 * @author Jacob Susko
 * @author Justin Lacombe
 * @date 2/13/2024
 */

public class CS482_project3_justin_jacob {

    // Not full key is known only partial key is known (3.4 Background story)
    // possibiliy iterate through all possible symmertric keys given what we know 16^33 for number of possibilities
    // Need to figure out how to find the key



    private static byte[] inkey = {(byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, 
        (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, 
        (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, 
        (byte) 0x00, (byte) 0x03}; // 5th byte is either 6 or f

    private static byte[] iv = {(byte) 0xC1, (byte) 0x77, (byte) 0x28, (byte) 0xA9, 
        (byte) 0x47, (byte) 0xCC, (byte) 0xC9, (byte) 0xEE, (byte) 0x21, 
        (byte) 0xB4, (byte) 0xEA, (byte) 0xED, (byte) 0x9C, (byte) 0x62, 
        (byte) 0xC8, (byte) 0x88};

    private static byte[] c1 = {(byte) 0x62, (byte) 0xFD, (byte) 0x8D, (byte) 0x38, (byte) 0x8D,
        (byte) 0x65, (byte) 0x83, (byte) 0x9F, (byte) 0x79, (byte) 0xE8, (byte) 0xA9,
        (byte) 0x38, (byte) 0x2B, (byte) 0x0B, (byte) 0x14, (byte) 0xF3};

    private static byte[] c2 = {(byte) 0xE8, (byte) 0xC9, (byte) 0x55, (byte) 0xF4, (byte) 0x86,
        (byte) 0x4C, (byte) 0xAE, (byte) 0x8A, (byte) 0x09, (byte) 0x30, (byte) 0xFF,
        (byte) 0x3B, (byte) 0x73, (byte) 0xF3, (byte) 0x88, (byte) 0x52};

    private static byte[] c3 = {(byte) 0x4F, (byte) 0x29, (byte) 0x71, (byte) 0xD6, (byte) 0x35,
        (byte) 0x1B, (byte) 0x20, (byte) 0x52, (byte) 0xC4, (byte) 0x1C, (byte) 0x0E,
        (byte) 0xF9, (byte) 0x3D, (byte) 0xAE, (byte) 0xDC, (byte) 0x47};

    private static byte[] c4 = {(byte) 0x8B, (byte) 0x12, (byte) 0xD7, (byte) 0xF4, (byte) 0x68,
        (byte) 0x6B, (byte) 0xDE, (byte) 0xE9, (byte) 0x86, (byte) 0xCA, (byte) 0xFF,
        (byte) 0x6C, (byte) 0x75, (byte) 0x07, (byte) 0x85, (byte) 0x1E};


    public static void main(String[] args) {
        // for loop going through each byte possibility
        for (byte i = (byte) 0x00; i <= (byte) 0xff; i++) {
            inkey[0] = i;
            for (byte j = (byte) 0x00; j <= (byte) 0xff; j++) {
                inkey[1] = j;
                for (byte k = (byte) 0x00; k <= (byte) 0xff; k++) {
                    inkey[2] = k;
                    for (byte z = (byte) 0x00; z <= (byte) 0xff; z++) {
                        inkey[3] = z;
                        for (int g = 0; g < 2; g++) {
                            if (g == 0) {
                                inkey[4] = (byte) 0x60;
                            } else {
                                inkey[4] = (byte) 0xf0;
                            }
                        }
                    }
                }
            }
        }
    }

    /**
     * 
     * @param cipherText recieved ciphertext in ascii bytes
     * @param inKey is symmetric key
     * @throws InvalidKeyException 
     */
    private void decrypt(byte[] cipherText, byte[] inKey) throws InvalidKeyException {
        //
			// If you receive the ciphertext, assuming that you have the same symmetric key, how will you decrypt?
			// Below, you only have inKey and cipherText
			//
		System.out.println (System.getProperty ("line.separator") + "Decrypting ......");
        Object decryptRoundKeys = Rijndael_Algorithm.makeKey (Rijndael_Algorithm.DECRYPT_MODE, inKey); // 
        int numOfCiphertextBlocks = cipherText.length / 16 - 1; // Each AES block has 16 bytes and we need to exclude the IV
        byte[] cleartextBlocks = new byte[numOfCiphertextBlocks * 16];

        byte[] receivedIV = new byte[16];
        for (int i = 0; i < 16; i++) receivedIV[i] = cipherText[i];
        byte[] currentDecryptionBlock = new byte[16];

        for (int i=0; i < numOfCiphertextBlocks; i++) {
            for (int j=0; j < 16; j++) currentDecryptionBlock [j] = cipherText[(i+1)*16 + j]; // Note that the first block is the IV

            byte[] thisDecryptedBlock = Rijndael_Algorithm.blockDecrypt2 (currentDecryptionBlock, 0, decryptRoundKeys);
    
            for (int j=0; j < 16; j++) cleartextBlocks[i*16+j] =  (byte) (thisDecryptedBlock[j] ^ cipherText[i*16 + j]);
        }
    }
}
