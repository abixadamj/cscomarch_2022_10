def encode_string(input_string: str) -> bytes:
    from base64 import standard_b64encode
    bytes_from_string = input_string.encode()
    ret_bytes = standard_b64encode(bytes_from_string)
    if len(ret_bytes) == 0:
        return b"NONE"
    return ret_bytes


def uniq_file() -> str:
    from secrets import token_hex
    return f"{token_hex(12)}.txt"

def uniq_link() -> str:
    from secrets import token_urlsafe
    return token_urlsafe(20)

if __name__ == '__main__':
    print(encode_string("Jakiś napis"))
    print(encode_string(""))

    for _ in range(6):
        print(uniq_file())
        print(uniq_link())


