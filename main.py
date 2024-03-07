def main():
    with open("/home/thaumagist/Bookbot/Books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def letters(text):
    count_letters = {}
    for letter in text:
        # convert to lower case
        lc_letter = letter.lower()
        # check if the character is a letter
        if lc_letter.isalpha():
            if lc_letter in count_letters:
                count_letters[lc_letter] = count_letters[lc_letter] + 1
            else:
                count_letters[lc_letter] = 1
    return count_letters

def sort_on(dict):
    return dict["num"]

file_contents_outside = main()
char_dict = letters(file_contents_outside)
count_letters = [{'name': key, 'num': value} for key, value in char_dict.items()]
print(word_count(file_contents_outside))

count_letters.sort(reverse=True, key=sort_on)
for letter_dict in count_letters:
    name = letter_dict['name']
    num  = letter_dict['num']
    print(f"The '{name}' character was found {num} times")