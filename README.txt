For the most part, the file is commented but here is a brief explanation of 
what was added.

First, we had to set up encryption. Encryption was set up in connect/accept
by letting the other party know that we either wanted or didn't want encryption. If 
there was a discrepancy, the server sent a reset signal. There was a boolean called
is_encrypted that let us know if this was an encrypted session. There was also a variable called
encrypted_flag that was set to 0x0 or 0x1 depending on if we were encrypting. 

Then, after connection, the box was set up. In the function to create data packets, we
encrypted the buffer by using box.encrypt(). This occured only if is_encrypted was True.
The packets were sent like normal. On the receiving end, the packets were decrypted if 
is_encrypted was set to True. When receiving, we had to add 40 to the amount of bytes we wanted 
to receive to account for the nonce. Then, the data was concatenated and returned.