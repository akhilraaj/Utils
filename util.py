def shift_char(ch, shift_amount):
    if ch.islower():
        return chr((ord(ch) - ord('a') + shift_amount) % 26 + ord('a'))
    elif ch.isupper():
        return chr((ord(ch) - ord('A') + shift_amount) % 26 + ord('A'))
    elif ch.isdigit():
        return chr((ord(ch) - ord('0') + shift_amount) % 10 + ord('0'))
    else:
        return ch  # special characters unchanged

def encode(s):
    return ''.join(shift_char(ch, 5) for ch in s)

def decode(s):
    return ''.join(shift_char(ch, -5) for ch in s)

def main():
    user_text = input("Enter the text: ").strip()
    action = input("Type 'e' to encode or 'd' to decode: ").strip().lower()
    
    if action == 'e':
        result = encode(user_text)
        print("Encoded text:", result)
    elif action == 'd':
        result = decode(user_text)
        print("Decoded text:", result)
    else:
        print("Invalid option! Please type 'e' or 'd'.")

if __name__ == "__main__":
    main()
