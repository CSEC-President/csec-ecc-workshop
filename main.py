from workshop.elliptic_curve.secp256k1 import Secp256k1
from workshop.keys import generate_public_key, generate_private_key
from workshop.signature import create_signature, verify_signature

if __name__ == "__main__":
    private_key = generate_private_key(256)
    public_key = generate_public_key(private_key)
    elliptic_curve = Secp256k1()

    message = "It better be working"
    verification_result = False
    try:
        signature = create_signature(message, private_key, elliptic_curve)
        verification_result = verify_signature(message, signature, public_key, elliptic_curve)
    except Exception as e:
        print(f"[!] Your implementation failed with an error \"{e}\"")

    print("[#] Verification successful" if (verification_result == True) else "[!] Verification failed")
