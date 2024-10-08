"""
Задание 3. Подсчёт количества слов в файле.
Напишите программу, которая подсчитывает количество слов в текстовом файле text_file.txt
и выводит результат на экран.
"""
import re
import string


def read_words_to_list(list_words):
    try:
        with open('text_file.txt', 'r', encoding='utf-8') as source_file:
            for line in source_file:
                line = line.split(' ')
                for word in line:
                    word = remove_trailing_punctuation_and_newline_rstrip(word)
                    if re.match("^[А-Яа-яa-zA-Z]+$", word):
                        list_words.append(word)
    except FileNotFoundError:
        print("Файл source.txt не найден.")
    except OSError as e:
        print(f"Ошибка файловой системы: {e}")
    except UnicodeDecodeError:
        print("Ошибка декодирования файла. Проверьте кодировку.")


def remove_trailing_punctuation_and_newline_rstrip(text):
    chars_to_remove = string.punctuation + '\n\r'
    return text.rstrip(chars_to_remove)

if __name__ == '__main__':
    list_words = []
    read_words_to_list(list_words)
    words_count = len(list_words)
    print(words_count)
