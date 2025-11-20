# CSEC ECDSA Workshop

A hands-on introduction to implementing the Elliptic Curve Digital Signature Algorithm (ECDSA) from scratch (no cryptographic dependencies) in Python.

## Prerequisites

- **Python 3.8+** - If not installed, see: https://www.python.org/downloads/
- Basic understanding of programming concepts
- Understanding of the lecture materials
- macOS, Windows, or Linux

## Workshop Structure

This workshop teaches digital signature cryptography by implementing the core ECDSA signing and verification functions from scratch. You'll work with elliptic curve mathematics, cryptographic hashing, and modular arithmetic without relying on external crypto libraries.

This project was started by someone who implemented the elliptic curve point operations and key generation but forgot to implement the signature creation and verification. Your task is to complete their implementation by filling in the missing cryptographic logic.

---

## Quick Start

### Clone and Run

```bash
# Clone the repo
git clone https://github.com/CSEC-President/csec-ecc-workshop

# Navigate to workshop directory
cd /path/to/csec-ecc-workshop

# Run the test, see that it fails
python3 main.py
```

**Expected Output (before implementation):**
```
[!] Verification failed
```

**Expected Output (after correct implementation):**
```
[#] Verification successful
```

---

## Workshop Overview

### What's Already Implemented

The previous developer completed:
- **Elliptic curve point arithmetic** (`workshop/curve_point.py`)
  - Point addition on elliptic curves
  - Scalar multiplication using double-and-add algorithm
  - Point validation on the curve
- **secp256k1 curve parameters** (`workshop/elliptic_curve/secp256k1.py`)
  - The same curve used by Bitcoin and Ethereum
- **Key generation** (`workshop/keys/`)
  - Private key generation (256-bit random number)
  - Public key derivation (scalar multiplication of generator point)

### What You Need to Implement

Your task is to complete two functions:

**1. Signature Creation** (`workshop/signature/signature_creation.py`)
- Implement the ECDSA signing algorithm

**2. Signature Verification** (`workshop/signature/signature_verification.py`)
- Output: True if valid, False otherwise
- Implement the ECDSA verification algorithm

---

### Project Layout

```
workshop/
├── curve_point.py                    # Elliptic curve point operations
├── elliptic_curve/
│   ├── abstract_curve.py             # Curve interface (if you want to add some other curve)
│   └── secp256k1.py                  # Bitcoin/Ethereum curve
├── keys/
│   ├── private_key_generation.py     # Random key generation
│   └── public_key_generation.py      # Public key derivation
└── signature/
    ├── signature_creation.py         # TODO: You implement this
    └── signature_verification.py     # TODO: You implement this
```

---

### Running Tests

```bash
python3 main.py
```


### Debugging Tips

If verification fails:
1. Print intermediate values to check your calculations
2. Verify all arithmetic uses `% curve.order`
3. Check that you're using the correct inverse calculations
4. Ensure point operations use `.multiply()` and `.add()` correctly

---

## Basic Python Reference

Essential Python for the workshop:

### Arithmetic Operations
```python
# Modular arithmetic
(a + b) % n          # Modular addition
(a * b) % n          # Modular multiplication
pow(a, b, n)         # Modular exponentiation: a^b mod n

# Modular inverse (Fermat's Little Theorem)
inverse = pow(x, n-2, n)

# Integer conversion
int.from_bytes(data, 'big')    # Bytes to integer
```

### Working with CurvePoint Objects
```python
# Scalar multiplication
point = generator.multiply(scalar)

# Point addition
result = point1.add(point2)

# Accessing coordinates
x_coord = point.point[0]
y_coord = point.point[1]

# Check if point at infinity
if point.point is None:
    # Handle infinity case
```

### String and Hashing
```python
import hashlib

# Hash a message
message = "Hello, ECDSA!"
hash_bytes = hashlib.sha256(message.encode()).digest()
hash_int = int.from_bytes(hash_bytes, 'big')
```

### Type Hints (used in the code)
```python
from typing import Tuple, Optional

def function(arg: int) -> Tuple[int, int]:
    return (x, y)

# Optional means value can be None
point: Optional[Tuple[int, int]] = None
```

---

## Verification Steps

Once you've implemented both functions:

1. **Run the test**: `python3 main.py`
2. **Check output**: Should see "[#] Verification successful"
3. **Test with different messages**: Modify the message in `main.py`
4. **Try invalid signatures**: Manually change signature values to verify it fails

---

## Disclaimer

**Educational Purpose**: This workshop teaches cryptographic concepts for educational purposes only. The implementation uses insecure random number generation (noted in the code) and is NOT suitable for production use.

**Your Responsibility**: You are solely responsible for your actions. The instructor and workshop organizers accept no responsibility for:
- System instability, crashes, or data loss from running this code
- Use of this code in production systems or real-world applications
- Any consequences arising from misuse of cryptographic techniques learned

**Security Warning**: Never use custom cryptography in production. Always use well-tested libraries like `cryptography`, `pycryptodome`, or `ecdsa` for real applications.

By participating, you acknowledge understanding these terms and accept full responsibility for your use of this code.

---

Author: Sasha Zyuzin

Good luck! 🔐