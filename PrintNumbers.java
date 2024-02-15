import java.math.BigInteger;
	/**
	 * @author Jacob Susko
	 * @author Justin Lacombe
	 * @date 2/13/2024
	 */

	public class PrintNumbers {

	    // Not full key is known only partial key is known (3.4 Background story)
	    // possibiliy iterate through all possible symmertric keys given what we know 16^33 for number of possibilities
	    // Need to figure out how to find the key


	    private static String val = "01000000000000000000000000000000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011";
	    private static byte[] knownKeyPart = new BigInteger(val, 2).toByteArray(); // 0 - 32 index are unknown and can be random
	    
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
	    	
//            for (byte b : knownKeyPart) {
//			 	System.out.print(String.format("%02X", b));
//			}
//            System.out.println();
            
	    	System.out.println(val.length());
		    System.out.println(knownKeyPart.length);
		    for (byte b : knownKeyPart) {
			 	System.out.print(String.format("%02X", b));
			}
			System.out.println();
			for (int i = 0; i < 256; i++) {
	            knownKeyPart[0] = (byte) i;
	            for (int j = 0; j < 256; j++) {
	                knownKeyPart[1] = (byte) j;
			            for (byte b : knownKeyPart) {
						 	System.out.print(String.format("%02X", b));
						}
			            System.out.println();
	            }

			}
		    return;

//	        for (int i = 0; i < 16; i++) {
//	            knownKeyPart[0] = (byte) i;
//	            for (int j = 0; j < 16; j++) {
//	                knownKeyPart[1] = (byte) j;
//	                for (int k = 0; k < 16; k++) {
//	                    knownKeyPart[2] = (byte) k;
//	                    for (int l = 0; l < 16; l++) {
//	                        knownKeyPart[3] = (byte) l;
//	                        for (int z = 0; z < 16; z++) {
//	                            knownKeyPart[4] = (byte) z;
//	                            for (int x = 0; x < 16; x++) {
//	                                knownKeyPart[5] = (byte) x;
//	                                for (int c = 0; c < 16; c++) {
//	                                    knownKeyPart[6] = (byte) c;
//	                                    for (int v = 0; v < 16; v++) {
//	                                        knownKeyPart[7] = (byte) v;
//	                                        for (int b = 0; b < 16; b++) {
//	                                            knownKeyPart[8] = (byte) b;
//	                                            for (int n = 0; n < 16; n++) {
//	                                                knownKeyPart[9] = (byte) n;
//	                                                for (int m = 0; m < 16; m++) {
//	                                                    knownKeyPart[10] = (byte) m;
//	                                                    for (int a = 0; a < 16; a++) {
//	                                                        knownKeyPart[11] = (byte) a;
//	                                                        for (int s = 0; s < 16; s++) {
//	                                                            knownKeyPart[12] = (byte) s;
//	                                                            for (int d = 0; d < 16; d++) {
//	                                                                knownKeyPart[13] = (byte) d;
//	                                                                for (int f = 0; f < 16; f++) {
//	                                                                    knownKeyPart[14] = (byte) f;
//	                                                                    for (int g = 0; g < 16; g++) {
//	                                                                        knownKeyPart[15] = (byte) g;
//	                                                                        for (int h = 0; h < 16; h++) {
//	                                                                            knownKeyPart[16] = (byte) h;
//	                                                                            for (int q = 0; q < 16; q++) {
//	                                                                                knownKeyPart[17] = (byte) q;
//	                                                                                for (int w = 0; w < 16; w++) {
//	                                                                                    knownKeyPart[18] = (byte) w;
//	                                                                                    for (int e = 0; e < 16; e++) {
//	                                                                                        knownKeyPart[19] = (byte) e;
//	                                                                                        for (int r = 0; r < 16; r++) {
//	                                                                                            knownKeyPart[20] = (byte) r;
//	                                                                                            for (int t = 0; t < 16; t++) {
//	                                                                                                knownKeyPart[21] = (byte) t;
//	                                                                                                for (int y = 0; y < 16; y++) {
//	                                                                                                    knownKeyPart[22] = (byte) y;
//	                                                                                                    for (int u = 0; u < 16; u++) {
//	                                                                                                        knownKeyPart[23] = (byte) u;
//	                                                                                                        for (int o = 0; o < 16; o++) {
//	                                                                                                            knownKeyPart[24] = (byte) o;
//	                                                                                                            for (int p = 0; p < 16; p++) {
//	                                                                                                                knownKeyPart[25] = (byte) p;
//	                                                                                                                for (int qq = 0; qq < 16; qq++) {
//	                                                                                                                    knownKeyPart[26] = (byte) qq;
//	                                                                                                                    for (int ww = 0; ww < 16; ww++) {
//	                                                                                                                        knownKeyPart[27] = (byte) ww;
//	                                                                                                                        for (int ee = 0; ee < 16; ee++) {
//	                                                                                                                            knownKeyPart[28] = (byte) ee;
//	                                                                                                                            for (int rr = 0; rr < 16; rr++) {
//	                                                                                                                                knownKeyPart[29] = (byte) rr;
//	                                                                                                                                for (int tt = 0; tt < 16; tt++) {
//	                                                                                                                                    knownKeyPart[30] = (byte) tt;
//	                                                                                                                                    for (int yy = 0; yy < 16; yy++) {
//	                                                                                                                                        knownKeyPart[31] = (byte) yy;
//	                                                                                                                                        for (int ii = 0; ii < 16; ii++) {
//	                                                                                                                                            knownKeyPart[32] = (byte) ii;
////	                                                                                                                                            System.out.println(knownKeyPart.toString());
//	                                                                                                                                            // call decrypt with each possible symmetric key
//	                                                                                                                                            // and print out with key until clear text is found
//	                                                                                                                                        }
//	                                                                                                                                    }
//
//	                                                                                                                                }
//	                                                                                                                            }
//	                                                                                                                        }
//	                                                                                                                    }
//	                                                                                                                }
//	                                                                                                            }
//	                                                                                                        }
//	                                                                                                    }
//	                                                                                                }
//	                                                                                            }
//	                                                                                        }
//	                                                                                    }
//	                                                                                }
//	                                                                            }
//	                                                                        }
//	                                                                    }
//	                                                                }
//	                                                            }
//	                                                        }
//	                                                    }
//	                                                }
//	                                            }
//	                                        }
//	                                    }
//	                                }
//	                            }
//	                        }
//	                    }
//	                }
//	            }
//	        }
	    }
}
