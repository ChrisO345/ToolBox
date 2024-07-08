"""
base32.py

Base32 encoding and decoding
https://en.wikipedia.org/wiki/Base32

Author: Chris Oliver
Date: 08/07/2024
"""


B32_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


def base32_encode(data: bytes) -> bytes:
    """
    Encodes a byte string using the base32 encoding scheme.

    Parameters
    ----------
    data : bytes
           The data to encode in base32

    Returns
    -------
    The base32 encoded data
    """
    binary_data = "".join(bin(ord(d))[2:].zfill(8) for d in data.decode("utf-8"))
    binary_data = binary_data.ljust(5 * ((len(binary_data) // 5) + 1), "0")
    b32_chunks = map("".join, zip(*[iter(binary_data)] * 5))
    b32_result = "".join(B32_CHARSET[int(chunk, 2)] for chunk in b32_chunks)
    return bytes(b32_result.ljust(8 * ((len(b32_result) // 8) + 1), "="), "utf-8")


def base32_decode(data: bytes) -> bytes:
    """
    Decodes a base32 encoded byte string.

    Parameters
    ----------
    data : bytes
           The base 32 encoded data

    Returns
    -------
    The decoded data
    """
    binary_data = "".join(
        bin(B32_CHARSET.index(_d))[2:].zfill(5)
        for _d in data.decode("utf-8").strip("=")
    )
    binary_data = list(map("".join, zip(*[iter(binary_data)] * 8)))
    return bytes("".join([chr(int(_d, 2)) for _d in binary_data]), "utf-8")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
