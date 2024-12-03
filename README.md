# Intellectual Property Protection

## Introduction
Intellectual property is a category of property that includes intangible creations of the human intellect, such as literary or artistic works and symbols, that are owned through a company or individual. The four main types of intellectual property rights include patents, trademarks, copyrights, and trade secrets. Owners of intellectual property use these IP laws to protect their intangible assets and prevent others from illegally obtaining their creation. While legally these laws are used to secure intellectual property, technology is constantly evolving and traditional cryptographic methods for digital security have been rendered obsolete, enabling bad actors to gain unauthorized access to, distribute, forge, and tamper with intellectual data. This is where post-quantum cryptography enters to address this looming threat. 

## Issue
Infringement is one major issue for intellectual property since it enables others to use an IP owner’s creations without permission, which can lead to financial penalties, reputational damages, and steals the value of the intellectual property. 

## Solution
Our approach to address this vulnerability and ensure the integrity and authenticity of IP data is to implement a solution that leverages post-quantum digital signatures from the Dilithium2 algorithm. CRYSTALS-Dilithium is a cryptographic solution from the Open Quantum Safe (OQS) library that offers post-quantum digital signatures for authenticating and verifying the integrity of intellectual property documents, patents, and other sensitive files.


## Overview
The Open Quantum Safe (OQS) project holds the goal of developing and prototyping quantum-resistant cryptography. liboqs-python offers a Python 3 wrapper for the [Open Quantum Safe](https://openquantumsafe.org/) [liboqs](https://github.com/open-quantum-safe/liboqs/) C library, which is a C library for quantum-resistant cryptographic algorithms. liboqs-python has been extensively tested on Linux, macOS and Windows platforms. The wrapper is written in Python 3, hence it is assumed that you have access to a Python 3 interpreter in the files and directories that the project contains.

The project contains the following files and directories:

```
src: contains, sig.py, our Python implementation of CRYSTALS-Dilithium
Test-Data: will store the sample infringement data, modified infrigemenet data file (if modified), the signed files, and their private and public keys
```

### Code Breakdown
* The code sig.py is a our Python implementation of CRYSTALS-Dilithium to secure intellectual property infringement data. We first import and install the liboqs-python requirements.
* File Signing: Create signer and verifier with sample signature mechanisms. Intellectual property data files are signed with a quantum-resistant private key, generating a signature that uniquely identifies the file and proves its authenticity. Once generated, the public and private key files will be updated in the Test-Data directory.
* Verification: Using the public key, recipients can then verify the signature to confirm that the file is genuine and untampered, building trust in the IP. The code compares the file’s signature with the public key and the original data stored in the Test-Data directory for verification.
* Update Support: The system allows for legitimate updates to the IP data files by allowing owners to re-sign after changes with their private key, maintaining authenticity across versions. Our implementation uses the original stored private key to sign updated files and produce a new signature.


## Dilithium2 OQS pre-requisites
* [liboqs](https://github.com/open-quantum-safe/liboqs)
* [git](https://git-scm.com/)
* [CMake](https://cmake.org/)
* C compiler, e.g., [gcc](https://gcc.gnu.org/), [clang](https://clang.llvm.org/), [MSVC](https://visualstudio.microsoft.com/vs/) etc.
* [Python 3](https://www.python.org/)


## Installation

### Configure, build and install liboqs

Execute in a Terminal/Console/Administrator Command Prompt

```
cd src
git clone --depth=1 https://github.com/open-quantum-safe/liboqs
cmake -S liboqs -B liboqs/build -DBUILD_SHARED_LIBS=ON
cmake --build liboqs/build --parallel 8
cmake --build liboqs/build --target install
```

The last line may require prefixing it by sudo on UNIX-like systems. Change --parallel 8 to match the number of available cores on your system.

On UNIX-like platforms, you may need to set the `LD_LIBRARY_PATH` (`DYLD_LIBRARY_PATH` on macOS) environment variable to point to the path to liboqs' library directory, e.g.,

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
```

On Windows platforms, you must ensure that you add the `-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE` flag to CMake, and that the liboqs shared library `oqs.dll` is visible system-wide, i.e., set the `PATH` environment variable accordingly by using the "Edit the system environment variables" Control Panel tool or executing in a Command Prompt

```
set PATH=%PATH%;C:\Program Files (x86)\liboqs\bin
```

You can change liboqs' installation directory by configuring the build to use an alternative path, e.g., `C:\liboqs, by passing the -DCMAKE_INSTALL_PREFIX=/path/to/liboqs` flag to CMake, e.g.,
```
cmake -S liboqs -B liboqs/build -DCMAKE_INSTALL_PREFIX="C:\liboqs" -DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE -DBUILD_SHARED_LIBS=ON
```

### Let liboqs-python install liboqs automatically

If liboqs is not detected at runtime by liboqs-python, it will be downloaded, configured and installed automatically (as a shared library). This process will be performed only once, at runtime, i.e., when loading the liboqs-python wrapper. The liboqs source directory will be automatically removed at the end of the process.

This is convenient in case you want to avoid installing liboqs manually, as described in the subsection above.

### Install and activate a Python virtual environment

Execute in a Terminal/Console/Administrator Command Prompt

```
python3 -m venv venv
. venv/bin/activate
python3 -m ensurepip --upgrade
```

On Windows, replace the line `. venv/bin/activate` by `venv\Scripts\activate.bat`

### Configure and install the wrapper

Execute in a Terminal/Console/Administrator Command Prompt

```
git clone --depth=1 https://github.com/open-quantum-safe/liboqs-python
pip install .
```

### Run the example

Execute `python3 sig.py`

## Results

Running the code generates the signed file for the sample data and their private and public keys.
Note: The code also demostrates the case where the owner modifies the file(modifies_infringement Data.txt) and generates a new signed file using the previously generated private key and is verified using the previous public key

## Conclusion
 By focusing on CRYSTALS-Dilithium signatures, we aim to enhance the authenticity and integrity of intellectual property infringement data. Implementing CRYSTALS-Dilithium  provides strong protection against potential future quantum computing threats and ensure that infringement reports and related documents are secure and verifiable. This approach is expected to improve the verification process for IP claims, strengthen the protection of intellectual property assets, and increase overall trust in IP management systems.
