import hashlib
from typing import Tuple

from workshop.curve_point import CurvePoint
from workshop.elliptic_curve.abstract_curve import Curve


def verify_signature(message: str, signature: Tuple[int, int], public_key: CurvePoint, curve: Curve) -> bool:
    message_hash = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')
    signature_x_coordinate = signature[0]
    signature_y_coordinate = signature[1]

    # Calculate the inverse of signature's y coordinate with FLT
    signature_y_coordinate_inverse = pow(signature_y_coordinate, curve.order - 2, curve.order)

    # Recover the random point
    # Using formula R' = (h*s1)*G+(r*s1)*pubKey
    # ============================================================================================================
    # TODO

    return signature_x_coordinate == 0 # Recovered random point [0] goes here instead of 0
