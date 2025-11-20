import hashlib
import random


def create_signature(message: str, private_key: int, curve: 'Curve'):
    message_hash = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')

    # This is insecure! Unfortunately, I'm too lazy to implement RFC6979
    secret = random.randint(1, curve.order - 1)

    generator_point = curve.generator
    random_point = generator_point.multiply(secret)

    random_point_x_coordinate = random_point.point[0]

    # Calculating signature proof
    # Using formula R' = (h*s1) * G + (r * s1) * pubKey
    # ============================================================================================================
    # TODO

    return random_point_x_coordinate, # Your computed result goes here
