def find_different(text: str) -> int:
    """Returns the index of mirrored pairs that hold different values."""
    indexed_pairs = enumerate(zip(text, text[::-1]))
    i = next((i for i, (a, b) in indexed_pairs if a != b), len(text) // 2)
    return i


def encode(msg: str) -> str:
    i = find_different(msg)
    n = len(msg) // 2

    if len(msg) % 2 == 0:
        return msg[:n] + msg[i] + msg[n:]

    middle = msg[n] if msg[i] == "0" else ["1", "0"][int(msg[n])]
    head = msg[: n + 1]
    tail = msg[n + 1 :]
    return head + middle + tail


def decode(msg: str) -> str:
    i = find_different(msg)
    n = len(msg) // 2

    if len(msg) % 2 == 1:
        received = msg[:n] + msg[n + 1 :]
        if msg[i] != msg[n]:
            return received[::-1]
        return received

    head = msg[: n - 1]
    mid1 = msg[n - 1]
    mid2 = msg[n]
    tail = msg[n + 1 :]
    expected = ["0", "1"][mid1 != mid2]
    if msg[i] != expected:
        return (head + mid2 + tail)[::-1]
    return head + mid1 + tail


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
        print(f"FAIL {original} -> {encoded[::-1]} -> {decoded}")


if __name__ == "__main__":
    test_protocol()
