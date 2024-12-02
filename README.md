#Intellectual Property Protection:

Intellectual property is a category of property that includes intangible creations of the human intellect, such as literary or artistic works and symbols, that are owned through a company or individual. The four main types of intellectual property rights include patents, trademarks, copyrights, and trade secrets. Owners of intellectual property use these IP laws to protect their intangible assets and prevent others from illegally obtaining their creation. Although these laws are employed to secure intellectual property, technology is constantly evolving and enabling bad actors to gain unauthorized access to, distribute, forge, and tamper with intellectual property. 

#Issue: 
Infringement is one major issue for intellectual property since it enables others to use an IP owner’s creations without permission, which can lead to financial penalties, reputational damages, and steals the value of the intellectual property. 

#Solution:
Our approach to address this vulnerability and ensure the integrity and authenticity of data is to implement a solution that leverages post-quantum digital signatures from the Dilithium algorithm. CRYSTALS-Dilithium is a cryptographic solution from the Open Quantum Safe (OQS) library that offers post-quantum digital signatures for authenticating and verifying the integrity of intellectual property documents, patents, and other sensitive files.


#Overview:

The Open Quantum Safe (OQS) project holds the goal of developing and prototyping quantum-resistant cryptography. liboqs-python offers a Python 3 wrapper for the Open Quantum Safe liboqs C library, which is a C library for quantum-resistant cryptographic algorithms. liboqs-python has been extensively tested on Linux, macOS and Windows platforms. The wrapper is written in Python 3, hence it is assumed that you have access to a Python 3 interpreter in the files and directories that the project contains.

The project contains the following files and directories:
oqs/oqs.py: a Python 3 module wrapper for the liboqs C library.
src/sig.py: signature example
Test-Data: Infringement Data.txt and modified_Infringement_Data.txt

#Dilithium2 OQS pre-requisites:
Dilithium OQS Pre-requisites: 
liboqs
git
CMake
C compiler, e.g., gcc, clang, MSVC etc.
Python 3
