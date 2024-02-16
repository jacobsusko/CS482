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
    

    public static void main(String[] args) throws InvalidKeyException {
        // for loop going through each byte possibility
        long startTime = System.nanoTime();
        String cipher = "C17728A947CCC9EE21B4EAED9C62C88862FD8D388D65839F79E8A9382B0B14F3E8C955F4864CAE8A0930FF3B73F388524F2971D6351B2052C41C0EF93DAEDC478B12D7F4686BDEE986CAFF6C7507851E";
		BigInteger b =  new BigInteger(cipher, 16);
		byte[] cTemp =  b.toByteArray();
		byte[] cipherText = new byte[80];
		for (int p = 1; p < cTemp.length; p++) {
			cipherText[p-1] = cTemp[p];
		}

        for (int i = 255; i >= 0; i++) {
            inkey[0] = (byte) i;
            for (int j = 255; j >= 0; j++) {
                inkey[1] = (byte) j;
                for (int k = 255; k >= 0; k++) {
                    inkey[2] = (byte) k;
                    for (int z = 255; z >= 0; z++) {
                        inkey[3] = (byte) z;
                        for (int g = 0; g < 2; g++) {
                            if (g == 0) {
                                inkey[4] = (byte) 0x60;
                            } else {
                                inkey[4] = (byte) 0xe0;
                            }
                            String plain = decrypt(cipherText, inkey);
                            if (!plain.equals("")) {
                                System.out.println("Key: " + convertToString(inkey));
                                System.out.println(plain + "\n");
                                long endTime = System.nanoTime();
                                long duration = (endTime - startTime);
                                System.out.println(duration);
                                return;
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
     * @throws InvalidKeyException \\
     */
    private static String decrypt(byte[] cipherText, byte[] inKey) throws InvalidKeyException {
        //
			// If you receive the ciphertext, assuming that you have the same symmetric key, how will you decrypt?
			// Below, you only have inKey and cipherText
			//
            // System.out.println (System.getProperty ("line.separator") + "Decrypting ......");
            Object decryptRoundKeys = Rijndael_Algorithm.makeKey (Rijndael_Algorithm.DECRYPT_MODE, inKey); // 
    
            int numOfCiphertextBlocks = cipherText.length / 16 - 1; // Each AES block has 16 bytes and we need to exclude the IV
            byte[] cleartextBlocks = new byte[numOfCiphertextBlocks * 16];

        byte[] receivedIV = new byte[16];
        for (int i = 0; i < 16; i++) receivedIV[i] = cipherText[i];
        byte[] currentDecryptionBlock = new byte[16];

        for (int i=0; i < numOfCiphertextBlocks; i++) {
            for (int j=0; j < 16; j++) currentDecryptionBlock [j] = cipherText[(i+1)*16 + j]; // Note that the first block is the IV

            byte[] thisDecryptedBlock = Rijndael_Algorithm.blockDecrypt2 (currentDecryptionBlock, 0, decryptRoundKeys);
            if (!isprintable(thisDecryptedBlock)) {
                return "";
            }
            for (int j=0; j < 16; j++) cleartextBlocks[i*16+j] =  (byte) (thisDecryptedBlock[j] ^ cipherText[i*16 + j]);
    }

    String recoveredString = new String (cleartextBlocks);
    return recoveredString;
    }


    private static boolean isprintable(byte[] plain) {
        for (byte b : plain) {
            if (!printable(b)) {
                return false;
            }
        }
        return true;
    }

    private static boolean printable(byte b) {
    return b >= 32 && b < 127;
    }

    public static String convertToString (byte[] data) {
		char[] _hexArray = {'0', '1', '2', '3', '4', '5','6', '7', '8',
			    '9', 'A', 'B', 'C', 'D', 'E', 'F'};

		StringBuffer sb = new StringBuffer();

		for (int i=0; i <data.length; i++) {
			sb.append("" + _hexArray[(data[i] >> 4) & 0x0f] + _hexArray[data[i] & 0x0f]);
		}

		return sb.toString();
	}

}
