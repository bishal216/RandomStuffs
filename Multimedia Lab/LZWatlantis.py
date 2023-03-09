# lzw compression algorithm
from string import printable

initial_dictionary = {chr(i): i for i in range(256)}
reverse_initial_dictionary = {v: k for k, v in initial_dictionary.items()}


def encode(input: str):
    duplicate_dict = initial_dictionary.copy()
    output = []
    current = ""
    for char in input:
        if current + char in duplicate_dict:
            current += char
        else:
            output.append(duplicate_dict[current])
            duplicate_dict[current + char] = len(duplicate_dict)
            current = char
    output.append(duplicate_dict[current])
    return output


def decode(input: str):
    duplicate_dict = reverse_initial_dictionary.copy()
    output = ""
    current = input[0]
    output += duplicate_dict[current]
    for i in range(1, len(input)):
        if input[i] in duplicate_dict:
            # this must be true if the encoding is correct
            entry = duplicate_dict[input[i]]
        elif input[i] == len(duplicate_dict):
            # this is the case where the next character is not in the dictionary
            entry = duplicate_dict[current] + duplicate_dict[current][0]
        output += entry
        duplicate_dict[len(duplicate_dict)] = duplicate_dict[current] + entry[0]
        current = input[i]
    return output


if __name__ == "__main__":
    payload = "hellohellohello"
    encoded = encode(payload)
    decoded = decode(encoded)
    assert payload == decoded
    print(f"OriginalLength={len(payload)}")
    print(f"Original: {payload}")
    print(f"EncodedLength={len(encoded)}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")