from collections import Counter
import string


def letter_distribution(filename):
    with open(filename, 'r') as file:
        text = file.read()
   
    filtered_text = ''.join(filter(str.islower, text))
    return dict(Counter(filtered_text))


def substitution_encrypt(filename, substitution_dict):
    with open(filename, 'r') as file:
        text = file.read()
    filtered_text = ''.join(filter(str.islower, text))
    encrypted_text = ''.join(substitution_dict.get(char, char) for char in filtered_text)
    with open("encrypted.txt", 'w') as file:
        file.write(encrypted_text)
    return encrypted_text


def substitution_decrypt(filename, substitution_dict):
    reverse_dict = {v: k for k, v in substitution_dict.items()}
    with open(filename, 'r') as file:
        encrypted_text = file.read()
    decrypted_text = ''.join(reverse_dict.get(char, char) for char in encrypted_text)
    return decrypted_text

def textstrip(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return ''.join(filter(str.islower, text))


def compare_frequencies(original_freq, encrypted_freq):
    all_letters = string.ascii_lowercase
    comparison = {}
    for letter in all_letters:
        original_count = original_freq.get(letter, 0)
        encrypted_count = encrypted_freq.get(letter, 0)
        comparison[letter] = (original_count, encrypted_count)
    return comparison


if __name__ == "__main__":
    input_file = r"C:\Users\rashm\Downloads\english_random (1).txt"
    substitution_dict = {
        'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r',
        'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
        'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
        'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
        'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l',
        'z': 'm'
    }

    
    original_freq = letter_distribution(input_file)
    print("Original Frequency Distribution:")
    print(original_freq)

    
    encrypted_content = substitution_encrypt(input_file, substitution_dict)
    
   
    encrypted_freq = letter_distribution("encrypted.txt")
    print("Encrypted Frequency Distribution:")
    print(encrypted_freq)

   
    frequency_comparison = compare_frequencies(original_freq, encrypted_freq)
    print("Frequency Comparison:")
    for letter, (orig_count, enc_count) in frequency_comparison.items():
        print(f"{letter}: Original count = {orig_count}, Encrypted count = {enc_count}")

   
    decrypted_content = substitution_decrypt("encrypted.txt", substitution_dict)
    original_text = textstrip(input_file)

    if decrypted_content == original_text:
        print("Substitution cipher successfully decrypted!")
    else:
        print("Decryption failed. Check your dictionary.")
