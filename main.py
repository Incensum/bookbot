def read(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        # print(file_contents)
    return file_contents

def wordcount(file_contents):
    list_of_words = file_contents.split()
    return len(list_of_words)

def sort_on(dict):
    return dict["num"]

def report(dict):
    list_from_dict = []
    for name in dict:
        temp_dict = {"name":name, "num":dict[name]}
        list_from_dict.append(temp_dict)
    list_from_dict.sort(reverse=True, key=sort_on)
    return list_from_dict

def count_chars(file_contents):
    chars = {}
    lowered_string = file_contents.lower()
    for char in lowered_string:
        if char in chars:
            chars[char] += 1
        elif char.isalpha():
            chars[char] = 1
    return chars

def main(path_to_file):
    file_contents = read(path_to_file)
    count = wordcount(file_contents)
    # print(count)
    char_count = count_chars(file_contents)
    # print(char_count)
    report_result = report(char_count)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count} words found in the document')
    print('')
    for result in report_result:
        print(result)
        # print(f"The '{result.key}' character was found {result.value} times")
    print('--- End report ---')

main("books/frankenstein.txt")