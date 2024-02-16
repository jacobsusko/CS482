import java.math.BigInteger;
import java.security.InvalidKeyException;
import java.util.Arrays;

/**
 * @author Jacob Susko
 * @author Justin Lacombe
 * @date 2/16/2024
 */

public class CS482_project3_justin_jacob_encrypt {




    public static void main(String[] args) throws InvalidKeyException {
        String k = "DC37471D600000000000000000000003";
        byte[] key = {(byte) 0xDC, (byte) 0x37, (byte) 0x47, (byte) 0x1D, (byte) 0x60, (byte) 0x00,
            (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00,
            (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x03};

        byte[] cbcIV = {(byte) 0x67, (byte) 0xc7, (byte) 0x20, (byte) 0xb7, (byte) 0x2a, (byte) 0x53,
					(byte) 0xb4, (byte) 0xBf, (byte) 0x97, (byte) 0x33, (byte) 0x73, (byte) 0x2f,
					(byte) 0xad, (byte) 0x99, (byte) 0x71, (byte) 0x19};

        String plainText = "Transfer fifty thousand dollars from my bank account to Jane Doe";
        byte[] inText = plainText.getBytes();

        	int numOfBlocks = inText.length / 16; 		// Each AES block has 16 bytes

			Object roundKeys = Rijndael_Algorithm.makeKey (Rijndael_Algorithm.ENCRYPT_MODE, key); // This creates the round keys

			// Now, we are ready and let's start the business

			byte[] cipherText = new byte[cbcIV.length + inText.length];
			byte[] feedback = Arrays.copyOf (cbcIV, cbcIV.length);
			for (int i = 0; i < 16; i++) cipherText[i] = cbcIV[i];
			byte[] currentBlock = new byte[16];

			for (int i = 0 ; i < numOfBlocks; i++) {
				for (int j=0; j < 16; j++) currentBlock[j] = (byte) (inText[i*16 + j] ^ feedback[j]); // CBC feedback

				byte[] thisCipherBlock = Rijndael_Algorithm.blockEncrypt2 (currentBlock, 0, roundKeys);

				feedback = Arrays.copyOf (thisCipherBlock, thisCipherBlock.length);

				for (int j=0; j < 16; j++) cipherText[(i+1)*16 + j] = thisCipherBlock[j];
			}

			System.out.println ("Ciphertext (including IV) is " + convertToString (cipherText));
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
