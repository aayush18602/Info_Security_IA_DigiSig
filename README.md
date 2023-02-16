# Information Security - Implementation of Digital Signature Algorithm

### Made by Samarth(16010120092), Manav(16010120085), Pratham(16010120084) and Aayush(16010120091), K.J. Somaiya College of Engineering

### It was created for Information Security IA 1 in K.J Somaiya College of Engineering.

- **Digital Signature Algorithm (DSA)** : It is one of the Federal Information Processing Standard for making digital signatures depends on the mathematical concept or we can say the formulas of modular exponentiation and the discrete logarithm problem to cryptograph the signature digitally in this algorithm. In the physical world, it is common to use handwritten signatures on handwritten or typed messages at this time.Digital signature is a cryptographic value that is calculated from the data and a secret key known only by the signer or the person whose signature is that.

  **Block Diagram**

![Pic](https://github.com/aayush18602/Info_Security_IA_DigiSig/blob/main/images/img4.jpg)

## The above is the block diagram of the **Digital Signature Algorithm**.

-**Explaination** -

- Each person adopting this scheme has a public-private key pair in cryptography.
- The key pairs used for encryption or decryption and signing or verifying are different for every signature. Here, the private key used for signing is referred to as the signature key and the public key as the verification key in this algorithm.
- Hash value and signature key are then fed to the signature algorithm which produces the digital signature on a given hash of that message.
- Then, the verifier feeds the digital signature and the verification key into the verification algorithm in this DSA. Thus, the verification algorithm gives some value as output as a ciphertext.
- For verification, the signature, this hash value, and output of verification algorithm are compared with each variable. Based on the comparison result, the verifier decides whether the digital signature is valid for this or invalid

**Screenshots**

![Pic](https://github.com/aayush18602/Info_Security_IA_DigiSig/blob/main/images/img1.jpg)

 In the above picture we have created the files which we will require for testing purposes. There are two files created to test the Algorithm

![Pic](https://github.com/aayush18602/Info_Security_IA_DigiSig/blob/main/images/img2.jpg)

 In this image we can see that the alogrithm works correctly for the entered file. It will check the filename and then only the access will be granted.

![Pic](https://github.com/aayush18602/Info_Security_IA_DigiSig/blob/main/images/img3.jpg)

 In the above image we can see that the Algorithm restricts from entering the file. Thus the algorithm works correctly.

**Data Integrity** - A very important concept of Data Integrity is followed here. In fact, in this case, an attacker has access to the data and modifies it, the digital signature verification at the receiver end fails in this algorithm, Thus, the hash of modified data and the output provided by the verification algorithm will not match the signature by this algorithm. Now, the receiver can safely deny the message assuming that data integrity has been breached for this algorithm.
