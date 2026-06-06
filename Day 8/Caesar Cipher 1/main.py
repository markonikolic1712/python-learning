

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
final_output = ""

def encrypt(original_text, shift_amount):
    output = ""
    for l in original_text:
        original_index = alphabet.index(l)
        if original_index + shift_amount > len(alphabet)-1:
            new_index = original_index + shift_amount - len(alphabet)
        else:
            new_index = original_index + shift_amount
        # print(f"original_index: {original_index}")
        # print(f"new_index: {new_index}")
        output += alphabet[new_index]
    return output

def decode(original_text, shift_amount):
    output = ""
    for l in original_text:
        original_index = alphabet.index(l)
        if original_index - shift_amount < 0:
            new_index = len(alphabet) + original_index - shift_amount
        else:
            new_index = original_index - shift_amount
        # print(f"original_index: {original_index}")
        # print(f"new_index: {new_index}")
        output += alphabet[new_index]
    return output


def caesar(p_text, p_shift, encode_or_decode):
    if encode_or_decode == "encode":
        print("Encoding...")
        return "Here is encoded result: " + encrypt(original_text=p_text, shift_amount=p_shift)

    if encode_or_decode == "decode":
        print("Decoding...")
        return "Here is decoded result: " + decode(original_text=p_text, shift_amount=p_shift)
    return None


print(caesar(text, shift, direction))


