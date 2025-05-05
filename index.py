import os
import sys
from collections import Counter

def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def clean_text(text):
    for ch in ['.', ',', '!', '?', ';', ':', '(', ')', '"', "'"]:
        text = text.replace(ch, ' ')
    return text.lower()

def count_words(text):
    words = text.split()
    return Counter(words)

def print_top_words(word_counts, top_n=10):
    print(f"\nTop {top_n} most frequent words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word}: {count}")

def save_results(word_counts, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for word, count in word_counts.most_common():
            f.write(f"{word}: {count}\n")
    print(f"\nResults saved to {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <file_to_analyze>")
        return

    input_file = sys.argv[1]
    output_file = "word_counts.txt"

    text = read_file(input_file)
    if text is None:
        return

    cleaned = clean_text(text)
    word_counts = count_words(cleaned)

    print_top_words(word_counts)
    save_results(word_counts, output_file)

if __name__ == "__main__":
    main()
