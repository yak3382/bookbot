def main():
    global book_path
    book_path = "books/frankenstein.txt"
    global text
    text = get_book_text(book_path)
    print(f"{text}\n")
    reading_report()

def reading_report():
    word_count = count_words(text)
    letter_dict = count_characters(text)
    print(f"--- Begin report of {book_path} ---\n")
    print(f"This text is {word_count} words long.\n")
    for letter in letter_dict:
        print(f"The '{letter}' character was found {letter_dict[letter]} times.")
    print()
    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    text = ''.join(filter(str.isalpha, text.lower()))
    letter_dict = {}
    for character in text:
        if character in letter_dict:
            letter_dict[character] += 1
        else:
            letter_dict[character] = 1
    dict_keys = list(letter_dict.keys())
    dict_keys.sort()
    sorted_dict = {i: letter_dict[i] for i in dict_keys} 
    return sorted_dict

def count_words(text):
    words = text.split()
    return len(words)

main()