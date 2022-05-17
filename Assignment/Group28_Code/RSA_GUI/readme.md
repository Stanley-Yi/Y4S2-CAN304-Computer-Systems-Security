#### How to start?

- Using python interpreter to run the main.py can open the UI interface.
- Running the exe file can also open the UI interface. The directory of the exe file is "/dist/main/main.exe".



#### How to use it?

The UI interface is like this:

![UI](/figure/UI.png)

There are five functions to process the RSA. 

- "Big Prime Generation" can generate big primes.
- "Improve by Ascii" can transform the plaintext into Ascii format.
- "No treatment" means the plaintext is not going to be transformed before encryption.
- "Quick power" means the RSA uses this function to encrypt and decrypt.
- "Chinese remainder theorem" means the RSA uses this function to encrypt and decrypt.



The process of using RSA:

- First, input the plaintext and select functions.

- After choosing the functions and inputting the plaintext, click the "Encryption" button and then the Ciphertext and Encryption time will show up.
- Next, click "Decryption" button and the Decryption text and Decryption time will show up.
- Click "Refresh" button to initialize the information.
- If you click "Python RSA" button, the system will use the python's RSA function.

Notes: The RSA does not support Chinese plaintext.

