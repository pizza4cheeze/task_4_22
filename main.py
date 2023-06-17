import re


def find_words_with_more_vowels(text):
    vowels = 'аоуэыяёюеиАОУЭЫЯЁЮЕИ'
    result_arr = []

    words = re.split(r'\s|,|!|\?|\.', text)

    for word in words:
        vowel_count = sum(1 for char in word if char in vowels)
        consonant_count = len(word) - vowel_count
        if vowel_count > consonant_count:
            result_arr.append(word)

    return ' '.join(result_arr)


text = open('input.txt', 'r', encoding='utf-8').readlines()
output_file = open('output.txt', 'w', encoding='utf-8')
for line in text:
    result = find_words_with_more_vowels(line)
    output_file.write(result)
    output_file.write('\n')
print(result)
