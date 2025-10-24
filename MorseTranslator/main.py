
morse_words = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', ' ': '/'}

reverse = {value: key for key, value in morse_words.items()}
txt_to_morse = lambda text: ''.join(morse_words.get(c.upper(), '?') for c in text)
morse_to_txt = lambda morse: ''.join(reverse.get(code, '?') for code in morse.strip().split())

def main():
    print("Morse Code Converter\n1. Text to Morse\n2. Morse to Text\n0. Exit")
    while True:
        choice = input("\nYour choice: ")
        if choice == '1':
            print("Morse code:", txt_to_morse(input("Enter text: ")))
        elif choice == '2':
            print("Text:", morse_to_txt(input("Enter Morse code (space-separated): ")))
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()