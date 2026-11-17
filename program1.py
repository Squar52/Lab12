import os
FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dictionary.txt")
def read_dict(filename):
    """Зчитує словник із текстового файлу (рядки у форматі ключ:значення)."""
    d = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                d[key.strip()] = value.strip()
    return d
def write_dict(filename, d):
    """Записує словник у текстовий файл."""
    with open(filename, "w", encoding="utf-8") as f:
        for key, value in d.items():
            f.write(f"{key}:{value}\n")
if not os.path.exists(FILE):
    write_dict(FILE, {"apple": "яблуко", "book": "книга", "water": "вода"})
words = read_dict(FILE)
print("Словник із файлу:")
for key, value in words.items():
    print(key, "-", value)
words[input("\nНове слово: ").strip()] = input("Переклад: ").strip()
write_dict(FILE, words)
print("Словник записано у файл.")