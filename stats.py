def count_words(text):
    count = 0
    split_text = text.split()
    return len(split_text)

def count_chars(text):
    chars = {'a': 0}
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(items):
    return items["num"]

def report(char_dict):
    char_list = []
    for entry in char_dict:
        char_list.append({"char": entry, "num": char_dict[entry]})
    char_list.sort(reverse=True,key=sort_on)
    return char_list

    
