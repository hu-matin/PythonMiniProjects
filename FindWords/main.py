from colorama import init, Fore, Style

init(autoreset=True)

text = str(input("Enter your text: "))
keys_input = str(input("Enter your keywords | example: Word1, Word2: "))
keys = [key.strip().lower() for key in keys_input.split(",") if key.strip()]

highlighted_text = text
counts = {}

for index, key in enumerate(keys):
    highlighted_text = highlighted_text.replace(key, f"{Fore.RED}{key}{Style.RESET_ALL}")
    counts[key] = text.lower().count(key)

print(f"Result in: ")
print(highlighted_text)

for index, key in enumerate(keys):
    c = counts[key]
    print(f"{key} : {c}")
