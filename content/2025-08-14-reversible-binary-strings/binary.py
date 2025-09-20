def drop_ith(msg: str, i: int) -> str:
    return msg[:i] + msg[i + 1 :]


def is_ascending(msg: str) -> bool:
    return int(msg) <= int(msg[::-1])


def encode(msg: str) -> str:
    n = len(msg) // 2
    check = is_ascending(msg)

    base = "0" if len(msg) % 2 == 0 else msg[n]
    flip = {"0": "1", "1": "0"}
    bit = base if check else flip[base]

    return msg[:n] + bit + msg[n:]


def decode(msg: str) -> str:
    n = (len(msg) - 1) // 2
    check = is_ascending(drop_ith(msg, n))
    bit = msg[n] == "0" if len(msg) % 2 == 1 else msg[n] == msg[n + 1]
    if check == bit:
        return drop_ith(msg, n)
    return drop_ith(msg[::-1], n)


def test_protocol():
    for n in range(1, 7):
        for i in range(2**n):
            bits = f"{i:0{n}b}"
            assert len(bits) == n
            test_string(bits)


def test_string(original):
    encoded = encode(original)
    decoded = decode(encoded)

    if original != decoded:
        print(f"FAIL {original} -> {encoded} -> {decoded}")

    decoded = decode(encoded[::-1])

    if original != decoded:
        print(f"FAIL {original} -> rev {encoded[::-1]} -> {decoded}")


if __name__ == "__main__":
    test_protocol()
