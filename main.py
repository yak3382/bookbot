def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    word_dict = count_characters(text)
    print(text)
    print(f"This text is {word_count} words long")
    print(f"Here is the number of each character: {word_dict}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    letter_dict = {}
    for character in text.lower():
        if character in letter_dict:
            letter_dict[character] += 1
        else:
            letter_dict[character] = 1
    return letter_dict

def count_words(text):
    words = text.split()
    return len(words)
    
main()